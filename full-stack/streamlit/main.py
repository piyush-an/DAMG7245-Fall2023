import streamlit as st
import requests
import os
import json
import pandas as pd

BASE_URL = os.getenv("API_URL", "http://localhost:8081")

st.title(':desktop_computer: Full Stack - Demo')

st.header(':mag: Search by Brands')

def fetch_all_brands():
    url = f"{BASE_URL}/api/v1/fetch_brands"
    response = requests.get(url)
    response_json = response.json()
    return response_json['brands']

fetch_all_brands()

with st.form("filter_by_brand"):
   user_selected_brand = st.selectbox('Choose a brand from the list', fetch_all_brands() )

   submitted = st.form_submit_button("Submit")
   if submitted:
       url = f"{BASE_URL}/api/v1/filter_by_brand"
       payload = json.dumps({
          "brand_name": user_selected_brand
          })
       headers = {'Content-Type': 'application/json'}
       response = requests.request("POST", url, headers=headers, data=payload)
       df = pd.read_json(response.text, orient='records')
       st.dataframe(df)    

st.header(':link: Similarity Search')

with st.form("similarity_search"):
   user_prompt = txt = st.text_area(label='Enter short query prompts below', placeholder="\"Bike for small kids\",\n\"Best Mountain bikes for kids\"")

   submitted = st.form_submit_button("Submit")
   if submitted:
        url = f"{BASE_URL}/api/v1/similar"
        payload = json.dumps({
            "queries": [user_prompt]
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        df = pd.read_json(response.text, orient='records')
        st.dataframe(df)

"""Sample Query

"Bike for small kids",
"Best Mountain bikes for kids",
"Cheap Mountain bike for kids",
"Female specific mountain bike",
"Road bike for beginners",
"Commuter bike for people over 60",
"Comfortable commuter bike",
"Good bike for college students",
"Mountain bike for beginners",
"Vintage bike",
"Comfortable city bike"
"""
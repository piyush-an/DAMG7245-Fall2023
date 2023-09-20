import streamlit as st
import datetime # This is a date time object module
import os 
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    d = st.date_input("When's your birthday", datetime.date(2023, 9, 20))
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

st.write(os.environ.get('DATABASE_URL'))
st.write(os.environ.get('DATABASE_USER'))
st.write(os.environ.get('DATABASE_PASSWORD'))


import pandas as pd
import streamlit as st

st.title('Plot Nexrad Data')


@st.cache_data
def get_station_list():
    # read following columns in the nexrad station dataset
    cols = [
        (20, 51),    # Name
        (72, 75),    # ST
        (106, 116),  # Lat
        (116, 127)   # Lon
    ]
    # read the dataset as a pandas dataframe using fixed width format
    df = pd.read_fwf(
        r"https://www.ncei.noaa.gov/access/homr/file/nexrad-stations.txt", colspecs=cols, skiprows=[1])
    # filter rows with are not null
    df = df[df['ST'].notna()]
    return df


data_load_state = st.text('Loading ...')
df = get_station_list()
# data_load_state = st.text('Loaded ...')

# select the unique states for user to filter
options = st.multiselect(label='Filter based on state', options=list(
    df['ST'].sort_values().unique()), default=['MA'])

# show raw data if user wants
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df[df['ST'].isin(options)].sort_values(by='ST'))

if df.empty:
    st.write('No data in db')
else:
    st.map(df[df['ST'].isin(options)][['LAT', 'LON']])

data_load_state.text("Done!")
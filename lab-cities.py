import streamlit as st
import pandas as pd

st.title('California Housing Data(1990) by Rongrong Chen')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
House_value_filter = st.slider('Median House Price',0, 500001, 200000)  # min, max, default

st.subheader('See more filters in the sidebar:')

# create a multi select
Ocean_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a input form
genre = st.sidebar.radio(
    "Chooose income level",
    ('Low', 'Median', 'High'))
if genre == 'Low':
    df = df[df.median_income <= 2.5]
elif genre == 'Median':
    df = df[(df.median_income < 4.5) & (df.median_income >2.5)]
else:
    df = df[df.median_income > 4.5]

# country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
# form.form_submit_button("Apply")

# filter by population
df = df[df.median_house_value >= House_value_filter]

# filter by capital
df = df[df.ocean_proximity.isin(Ocean_filter)]

# show on map
st.map(df)


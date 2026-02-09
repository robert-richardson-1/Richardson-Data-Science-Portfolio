#Instructions:
# 
# Basic Streamlit app using the Data set "Palmer's Penguins." To use
# the app you should load the Streamlit program by downloading the proper
# program and then running the following code in terminal:
# streamlit run basic_streamlit_app/main.py
#

#import needed programs
import streamlit as st
import pandas as pd

#app title
st.title("Palmer's Penguins Data Exploration")

#app description
st.write("""This app allows the exploration of the **Palmer's Penguins dataset**. 
Using the interactive features, you can filter the penguin data by species, island, 
bill length, bill depth, flipper length, body mass, sex, and year to see how different 
penguins compare!""")

st.write("""By adjusting both the selectors, sliders, and physical ordering commands
by clicking on the physical dataset, you can filter the data in
various ways.""")

#load data
@st.cache_data
def load_data():
    return pd.read_csv("penguins.csv")
df = load_data()

#filters
st.sidebar.header("Interactive Filters:")

#select species, island, bill length, bill depth, flipper length, body mass, sex, and year
species = st.sidebar.multiselect(
    "Select Species",
    options=df["species"].unique(),
    default=df["species"].unique()
)

island = st.sidebar.multiselect(
    "Select Island",
    options=df["island"].unique(),
    default=df["island"].unique()
)

bill_length = st.sidebar.slider(
    "Select Bill Length (mm)",
    int(df["bill_length_mm"].min()),
    int(df["bill_length_mm"].max()),
    (int(df["bill_length_mm"].min()), int(df["bill_length_mm"].max()))
)

bill_depth = st.sidebar.slider(
    "Select Bill Length (mm)",
    int(df["bill_depth_mm"].min()),
    int(df["bill_depth_mm"].max()),
    (int(df["bill_depth_mm"].min()), int(df["bill_depth_mm"].max()))
)

flipper_length = st.sidebar.slider(
    "Select Flipper Length (mm)",
    int(df["flipper_length_mm"].min()),
    int(df["flipper_length_mm"].max()),
    (int(df["flipper_length_mm"].min()), int(df["flipper_length_mm"].max()))
)

body_mass = st.sidebar.slider(
    "Select Body Mass Range (g)",
    int(df["body_mass_g"].min()),
    int(df["body_mass_g"].max()),
    (int(df["body_mass_g"].min()), int(df["body_mass_g"].max()))
)

sex = st.sidebar.multiselect(
    "Select sex",
    options=df["sex"].unique(),
    default=df["sex"].unique()
)

year = st.sidebar.multiselect(
    "Select Year",
    options=df["year"].unique(),
    default=df["year"].unique()
)

filtered_df = df[
    (df["species"].isin(species)) &
    (df["island"].isin(island)) &
    (df["bill_length_mm"].between(bill_length[0], bill_length[1])) &
    (df["bill_depth_mm"].between(bill_depth[0], bill_depth[1])) &
    (df["flipper_length_mm"].between(flipper_length[0], flipper_length[1])) &
    (df["body_mass_g"].between(body_mass[0], body_mass[1])) &
    (df["sex"].isin(sex)) &
    (df["year"].isin(year))
]

#display data (with filters if inputed)
st.subheader("Interactive Filtered Penguin Data")
st.write(f"Based on selected inputs, showing {filtered_df.shape[0]} penguins")

st.dataframe(filtered_df)

#show all raw data
st.subheader("Complete Raw Data From Dataset")
st.dataframe(df)
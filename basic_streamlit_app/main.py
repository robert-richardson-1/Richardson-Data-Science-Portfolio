#import needed programs
import streamlit as st
import pandas as pd

#app title
st.title("Palmer's Penguins")

#app description
st.write("""This app allows the exploration of the **Palmer's Penguins dataset**. 
Using the interactive features, you can filter the penguin data by species, 
island, and body mass to see how different penguins compare!""")

#load data
@st.cache_data
def load_data():
    return pd.read_csv("penguins.csv")
df = load_data()

#filters
st.sidebar.header("Filter Penguins")

#selection, island, and mass
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

body_mass = st.sidebar.slider(
    "Select Body Mass Range (g)",
    int(df["body_mass_g"].min()),
    int(df["body_mass_g"].max()),
    (int(df["body_mass_g"].min()), int(df["body_mass_g"].max()))
)

iltered_df = df[
    (df["species"].isin(species)) &
    (df["island"].isin(island)) &
    (df["body_mass_g"].between(body_mass[0], body_mass[1]))
]


filtered_df = df[
    (df["species"].isin(species)) &
    (df["island"].isin(island)) &
    (df["body_mass_g"].between(body_mass[0], body_mass[1]))
]

#display data (with filters if they have it)
st.subheader("Filtered Penguin Data")
st.write(f"Showing {filtered_df.shape[0]} penguins")

st.dataframe(filtered_df)

#show all raw data
st.subheader("Complete Raw Data From Dataset")
st.dataframe(df)
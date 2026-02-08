import streamlit as st

st.write("Hello World")

import pandas as pd

df = pd.read_csv("data/sample_data-1.csv")
st.dataframe(df["Occupation"])

import seaborn as sns

sns.set_theme(style="darkgrid")
sns.boxplot(x=df["City"], y=df["Salary"])


box_plot1 = sns.boxplot(x = df["City"], y=df["Salary"])

st.pyplot(box_plot1.get_figure())
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

st.title("ML Explorer")
st.write("Train a machine learning model on your own data or a sample dataset.")

st.header("1. Choose a Dataset")
source = st.radio("", ["Iris (sample)", "Breast Cancer (sample)", "Upload my own CSV"])

if source == "Iris (sample)":
    raw = load_iris(as_frame=True)
    df = raw.frame
    df["target"] = [raw.target_names[i] for i in df["target"]]
    target_col = "target"

elif source == "Breast Cancer (sample)":
    raw = load_breast_cancer(as_frame=True)
    df = raw.frame
    df["target"] = ["malignant" if t == 0 else "benign" for t in df["target"]]
    target_col = "target"

else:
    file = st.file_uploader("Upload a CSV", type="csv")
    if not file:
        st.stop()
    df = pd.read_csv(file)
    target_col = st.selectbox("Which column is the target (what you're predicting)?", df.columns)

st.write(f"**{df.shape[0]} rows, {df.shape[1]-1} features, {df[target_col].nunique()} classes**")
st.dataframe(df.head(), use_container_width=True)


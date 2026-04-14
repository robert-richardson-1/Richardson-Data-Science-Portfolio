import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

#intro
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

#model
st.header("2. Choose a Model & Settings")
model_name = st.selectbox("Model", ["Decision Tree", "Logistic Regression"])
test_size = st.slider("Test set size", 0.1, 0.5, 0.2, step=0.05)

if model_name == "Decision Tree":
    max_depth = st.slider("Max depth", 1, 20, 4)
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
else:
    C = st.slider("Regularization strength (C) — lower = simpler model", 0.01, 10.0, 1.0)
    model = LogisticRegression(C=C, max_iter=1000, random_state=42)

#train
if not st.button("Train Model"):
    st.stop()

#features and target
X = df.drop(columns=[target_col])
for col in X.select_dtypes(include="object").columns:
    X[col] = LabelEncoder().fit_transform(X[col])

le = LabelEncoder()
y = le.fit_transform(df[target_col])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#results
st.header("3. Results")

avg = "binary" if len(le.classes_) == 2 else "weighted"
col1, col2, col3, col4 = st.columns(4)
col1.metric("Accuracy",  f"{accuracy_score(y_test, y_pred):.2%}")
col2.metric("Precision", f"{precision_score(y_test, y_pred, average=avg, zero_division=0):.2%}")
col3.metric("Recall",    f"{recall_score(y_test, y_pred, average=avg, zero_division=0):.2%}")
col4.metric("F1 Score",  f"{f1_score(y_test, y_pred, average=avg, zero_division=0):.2%}")

st.subheader("Confusion Matrix")
fig, ax = plt.subplots()
ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred), display_labels=le.classes_).plot(ax=ax)
st.pyplot(fig)
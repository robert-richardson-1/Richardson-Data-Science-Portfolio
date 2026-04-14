import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, label_binarize
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, ConfusionMatrixDisplay, roc_curve, auc
)
import matplotlib.pyplot as plt

st.set_page_config(page_title="ML Explorer", layout="wide")
st.title("ML Explorer")
st.write("Train a machine learning model on your own data or a sample " \
"dataset. This app allows you to upload a dataset, experiment with " \
"hyperparameters, namely test size/depth of a decision tree and test sizer/regularization " \
"of a logistic regression, and observe how these affect model training and performance.")
st.divider()

#sidebar controls
with st.sidebar:
    st.header("Exploration Settings")

    st.subheader("1. Dataset")
    source = st.radio("", ["Iris (sample)", "Breast Cancer (sample)", "Upload own CSV"])

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
        target_col = st.selectbox("Target column", df.columns)

    st.subheader("2. Model")
    model_name = st.selectbox("", ["Decision Tree", "Logistic Regression"])
    test_size = st.slider("Test set size", 0.1, 0.5, 0.2, step=0.05)

    if model_name == "Decision Tree":
        max_depth = st.slider("Max depth", 1, 20, 4)
        model = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    else:
        C = st.slider("Regularization (C) — lower = simpler", 0.01, 10.0, 1.0)
        model = LogisticRegression(C=C, max_iter=1000, random_state=42)

    train_btn = st.button("Train Model", use_container_width=True)

#data
st.subheader("Dataset Preview")
col1, col2, col3 = st.columns(3)
col1.metric("Rows", df.shape[0])
col2.metric("Features", df.shape[1] - 1)
col3.metric("Classes", df[target_col].nunique())
st.dataframe(df.head(), use_container_width=True)

if not train_btn:
    st.info("👈 Configure your settings in the sidebar, then click 'Train Model'")
    st.stop()

#train
X = df.drop(columns=[target_col])
for col in X.select_dtypes(include="object").columns:
    X[col] = LabelEncoder().fit_transform(X[col])

le = LabelEncoder()
y = le.fit_transform(df[target_col])
n_classes = len(le.classes_)

#kind of guessing on a bit of this next part. I think that this is correct
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=42, stratify=y
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

#data metrics
st.divider()
st.subheader("Performance Metrics")
avg = "binary" if n_classes == 2 else "weighted"
m1, m2, m3, m4 = st.columns(4)
m1.metric("Accuracy",  f"{accuracy_score(y_test, y_pred):.2%}")
m2.metric("Precision", f"{precision_score(y_test, y_pred, average=avg, zero_division=0):.2%}")
m3.metric("Recall",    f"{recall_score(y_test, y_pred, average=avg, zero_division=0):.2%}")
m4.metric("F1 Score",  f"{f1_score(y_test, y_pred, average=avg, zero_division=0):.2%}")

#confusion matrix and ROC/AUC curves
st.divider()
left, right = st.columns(2)

with left:
    st.subheader("Confusion Matrix")
    fig, ax = plt.subplots()
    ConfusionMatrixDisplay(
        confusion_matrix(y_test, y_pred), display_labels=le.classes_
    ).plot(ax=ax, colorbar=False)
    ax.set_title("Confusion Matrix")
    st.pyplot(fig)

with right:
    st.subheader("ROC Curve")
    fig, ax = plt.subplots()

    if n_classes == 2:
        fpr, tpr, _ = roc_curve(y_test, y_prob[:, 1])
        ax.plot(fpr, tpr, lw=2, label=f"AUC = {auc(fpr, tpr):.2f}")
    else:
        y_bin = label_binarize(y_test, classes=list(range(n_classes)))
        for i, cls in enumerate(le.classes_):
            fpr, tpr, _ = roc_curve(y_bin[:, i], y_prob[:, i])
            ax.plot(fpr, tpr, lw=2, label=f"{cls} (AUC={auc(fpr, tpr):.2f})")

    ax.plot([0, 1], [0, 1], "k--", lw=1)
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("ROC Curve")
    ax.legend(loc="lower right")
    st.pyplot(fig)
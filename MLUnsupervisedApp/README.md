# Unsupervised Machine Learning Streamlit App

This project is an interactive unsupervised machine learning web application built with `Streamlit`. Users can explore two sample datasets (Iris and Breast Cancer), or upload their own .csv file, then run either K-Means Clustering or Principal Component Analysis with adjustable hyperparameters. The app displays a dataset preview, model performance metrics, and visualizations that update in real time.

Key ML concepts applied: unsupervised learning, K-Means clustering, dimensionality reduction, hyperparameter tuning via interactive widgets, and performance evaluation.

---

## How to Run

- **Install dependencies:** `pip install streamlit scikit-learn pandas numpy matplotlib seaborn`
- **Run locally:** in terminal: `streamlit run app.py`
- **Deployed App:** [View on Streamlit Community Cloud](https://richardson-data-science-portfolio-mlunsupervisedapp.streamlit.app/)

---

## Libraries Included

- `streamlit`
- `scikit-learn`
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

---

## Dataset Overview

**Source:** Iris and Breast Cancer datasets are built into scikit-learn (`sklearn.datasets`). Iris classifies flower species by petal and sepal measurements across 3 classes (150 rows, 4 features). Breast Cancer classifies tumors as malignant or benign (569 rows, 30 features). Users may also upload their own labeled, tabular .csv file for clustering and dimensionality reduction tasks.

---

## App Features

- **Dataset selection:** Choose from Iris (sample), Breast Cancer (sample), or upload your own .csv file
- **Algorithm selection:** Switch between K-Means Clustering and PCA
- **Hyperparameter tuning:**
  - K-Means: adjust number of clusters (k), toggle elbow plot, and silhouette plot
  - PCA: adjust number of components, toggle feature loadings heatmap
- **Dataset preview:** Displays row count, feature count, and a live data table
- **Performance metrics:** Inertia, silhouette score, explained variance, and visualizations update after each run

---

## Example of App
**Sample output from the "Iris' dataset, displaying the derived K-Means clustering data from its output:**
    - Here, a user is using the Iris sample data, and based on their selection of the K-Means clustering model using [3] clusters, they received the following: An Inertia (WCSS) of 139.8, Silhouette Score of 0.460, a depiction of how the k=3 clusters are actually grouping the data, and an elbow plot depicting the number of clusters selected and the "goodness of cluster number selection." Additionally, each of these features has a description accompanying them for each attribute.
<img width="1521" height="966" alt="image" src="https://github.com/user-attachments/assets/d9109c85-ff62-4599-95fb-136442bda055" />


---

## References

| Resource | Link |
|---|---|
| Streamlit Documentation | [docs.streamlit.io](https://docs.streamlit.io) |
| scikit-learn User Guide | [scikit-learn.org/stable/user_guide](https://scikit-learn.org/stable/user_guide.html) |
| scikit-learn Datasets | [sklearn.datasets](https://scikit-learn.org/stable/api/sklearn.datasets.html) |
| K-Means Clustering | [sklearn.cluster.KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) |
| PCA | [sklearn.decomposition.PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) |
| Silhouette Score | [sklearn.metrics.silhouette_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html) |

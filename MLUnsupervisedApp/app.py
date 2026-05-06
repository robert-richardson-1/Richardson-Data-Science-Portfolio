import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples

st.set_page_config(page_title="Unsupervised Machine Learning Playground!")
st.title("Unsupervised Machine Learning Playground!")
st.write("Explore your data using unsupervised machine learning techniques!")
st.write("This app allows you to upload a dataset (or use a sample), experiment with "
         "hyperparameters, and observe how they affect model behavior and visualizations!")
st.divider()

#sidebar controls
with st.sidebar:
    st.header("Exploration Settings")

    st.subheader("1. Dataset")
    source = st.radio("", ["Iris (sample)", "Wine (sample)", "Breast Cancer (sample)", "Upload own .csv file"])

    if source == "Iris (sample)":
        raw = load_iris(as_frame=True)
        df = raw.frame.drop(columns=["target"])
        dataset_name = "Iris"
    elif source == "Wine (sample)":
        raw = load_wine(as_frame=True)
        df = raw.frame.drop(columns=["target"])
        dataset_name = "Wine"
    elif source == "Breast Cancer (sample)":
        raw = load_breast_cancer(as_frame=True)
        df = raw.frame.drop(columns=["target"])
        dataset_name = "Breast Cancer"
    else:
        file = st.file_uploader("Upload a CSV", type="csv")
        if not file:
            st.stop()
        df = pd.read_csv(file).select_dtypes(include=[np.number]).dropna()
        dataset_name = "Uploaded Dataset"

    st.subheader("2. Algorithm")
    algo = st.selectbox("", ["K-Means Clustering", "PCA"])

    st.subheader("3. Hyperparameters")
    if algo == "K-Means Clustering":
        k = st.slider("Number of Clusters (k)", 2, 10, 3)
        show_elbow = st.checkbox("Show Elbow Plot", value=True)
        show_silhouette = st.checkbox("Show Silhouette Plot", value=True)
    else:
        n_comp = st.slider("Number of Components", 2, min(10, df.shape[1]), 2)
        show_loadings = st.checkbox("Show Feature Loadings Heatmap", value=True)

#data preview
st.subheader("Dataset Preview")
col1, col2 = st.columns(2)
col1.metric("Rows", df.shape[0])
col2.metric("Features", df.shape[1])
st.dataframe(df.head(), use_container_width=True)
st.divider()

#preprocessing
X = StandardScaler().fit_transform(df)

#k-means
if algo == "K-Means Clustering":
    st.subheader("K-Means Clustering")
    st.write("K-Means partitions data into k groups by minimizing within-cluster variance. "
             "Use the elbow plot to find a good k, and the silhouette score to evaluate how well-separated the clusters are.")

    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(X)
    sil = silhouette_score(X, labels)

    m1, m2 = st.columns(2)
    m1.metric("Inertia (WCSS)", f"{km.inertia_:,.1f}")
    m1.write("Inertia (also called WCSS — within-cluster sum of squares) measures the total distance "
             "between each point and its cluster's centroid. Lower inertia means tighter, more compact clusters. "
             "It will always decrease as k increases, which is why you will need the elbow plot to find a balanced k.")
    m2.metric("Silhouette Score", f"{sil:.3f}")
    m2.write("The silhouette score ranges from -1 to 1. A score close to 1 means points are well-matched "
             "to their own cluster and far from neighboring clusters. A score near 0 means clusters are overlapping, "
             "and a negative score suggests points may be assigned to the wrong cluster.")

    #project to 2d for scatter plot
    pca2 = PCA(n_components=2, random_state=42)
    X_2d = pca2.fit_transform(X)
    centroids_2d = pca2.transform(km.cluster_centers_)

    left, right = st.columns(2)

    with left:
        st.subheader("Cluster Scatter")
        st.write("Each point is colored by its assigned cluster. Since the data may have more than 2 features, "
                 "it is projected down to 2D using PCA so we can visualize it. The X markers show the cluster centroids.")
        fig, ax = plt.subplots()
        colors = plt.cm.tab10.colors
        for i in range(k):
            mask = labels == i
            ax.scatter(X_2d[mask, 0], X_2d[mask, 1], color=colors[i % 10],
                       label=f"Cluster {i}", alpha=0.75, s=30)
        ax.scatter(centroids_2d[:, 0], centroids_2d[:, 1],
                   marker="X", s=180, color="black", zorder=5, label="Centroid")
        ax.set_xlabel(f"PC1 ({pca2.explained_variance_ratio_[0]*100:.1f}%)")
        ax.set_ylabel(f"PC2 ({pca2.explained_variance_ratio_[1]*100:.1f}%)")
        ax.set_title("Clusters (PCA Projection)")
        ax.legend(fontsize=8)
        st.pyplot(fig)

    if show_elbow:
        with right:
            st.subheader("Elbow Plot")
            st.write("The elbow plot shows how inertia drops as k increases. You want to pick the k where "
                     "the curve bends — adding more clusters beyond that point gives diminishing returns. "
                     "The red dashed line marks your currently selected k.")
            inertias = [KMeans(n_clusters=i, n_init=10, random_state=42).fit(X).inertia_
                        for i in range(1, 11)]
            fig, ax = plt.subplots()
            ax.plot(range(1, 11), inertias, marker="o")
            ax.axvline(k, color="red", linestyle="--", label=f"k = {k}")
            ax.set_xlabel("k")
            ax.set_ylabel("Inertia (WCSS)")
            ax.set_title("Elbow Method")
            ax.legend()
            st.pyplot(fig)

    if show_silhouette:
        st.divider()
        st.subheader("Silhouette Plot")
        st.write("Each bar represents one cluster. The width of each slice shows the silhouette coefficient "
                 "for individual points — wider bars mean points are confidently assigned to their cluster. "
                 "Ideally all clusters extend well past the dashed average line, and no cluster has a large "
                 "number of negative (left-side) values, which would indicate misassigned points.")
        sil_vals = silhouette_samples(X, labels)
        fig, ax = plt.subplots()
        y = 0
        for i in range(k):
            vals = np.sort(sil_vals[labels == i])
            ax.fill_betweenx(np.arange(y, y + len(vals)), 0, vals,
                             alpha=0.75, color=colors[i % 10], label=f"Cluster {i}")
            y += len(vals) + 5
        ax.axvline(sil, color="black", linestyle="--", label=f"Avg = {sil:.3f}")
        ax.set_xlabel("Silhouette Coefficient")
        ax.set_title("Silhouette Analysis")
        ax.legend(fontsize=8)
        st.pyplot(fig)

#pca
else:
    st.subheader("Principal Component Analysis (PCA)")
    st.write("PCA finds the directions of maximum variance and projects data onto them. "
             "The scree plot shows how much information each component captures.")

    n_comp_actual = min(n_comp, df.shape[1])
    pca = PCA(n_components=n_comp_actual, random_state=42)
    X_pca = pca.fit_transform(X)
    exp_var = pca.explained_variance_ratio_

    #compute how many components needed for 95% variance
    pca_full = PCA(random_state=42).fit(X)
    n_95 = int(np.searchsorted(np.cumsum(pca_full.explained_variance_ratio_), 0.95)) + 1

    m1, m2, m3 = st.columns(3)
    m1.metric("Components", n_comp_actual)
    m2.metric("Variance Explained", f"{exp_var.sum()*100:.1f}%")
    m2.write("This is the total percentage of the original data's variance captured by your selected components. "
             "Higher is better — if this number is low, consider increasing the number of components.")
    m3.metric("Components for 95% Variance", n_95)
    m3.write("This tells you the minimum number of components needed to retain 95% of the information "
             "in the dataset. It's a common rule of thumb for deciding how many components to keep.")

    left, right = st.columns(2)

    with left:
        st.subheader("Scree Plot")
        st.write("The bars show how much variance each individual component explains. The red line shows the "
                 "cumulative total. Look for where the bars flatten out — components after that point add "
                 "little new information. The gray dashed line marks the 95% threshold.")
        fv = pca_full.explained_variance_ratio_
        n_show = min(15, len(fv))
        fig, ax = plt.subplots()
        ax.bar(range(1, n_show + 1), fv[:n_show] * 100, alpha=0.7, label="Per component")
        ax2 = ax.twinx()
        ax2.plot(range(1, n_show + 1), np.cumsum(fv[:n_show]) * 100,
                 color="red", marker="o", markersize=4, label="Cumulative")
        ax2.axhline(95, color="gray", linestyle="--", alpha=0.6)
        ax2.set_ylabel("Cumulative Variance (%)")
        ax.set_xlabel("Component")
        ax.set_ylabel("Variance (%)")
        ax.set_title("Explained Variance by Component")
        st.pyplot(fig)

    with right:
        st.subheader("PC1 vs PC2")
        st.write("This scatter plot shows your data projected onto the first two principal components. "
                 "Points that appear close together are similar in the original feature space. "
                 "Visible clusters or groupings here suggest natural structure in the data.")
        fig, ax = plt.subplots()
        ax.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6, s=25)
        ax.set_xlabel(f"PC1 ({exp_var[0]*100:.1f}%)")
        ax.set_ylabel(f"PC2 ({exp_var[1]*100:.1f}%)")
        ax.set_title("PCA Projection")
        st.pyplot(fig)

    if show_loadings:
        st.divider()
        st.subheader("Feature Loadings Heatmap")
        st.write("Each cell shows how strongly a feature contributes to a given component. "
                 "Red means a strong positive contribution (the feature increases in that direction), "
                 "blue means a strong negative contribution, and white means little to no influence. "
                 "This helps you interpret what each principal component actually represents.")
        loadings = pd.DataFrame(
            pca.components_.T,
            index=df.columns,
            columns=[f"PC{i+1}" for i in range(n_comp_actual)]
        )
        fig, ax = plt.subplots(figsize=(max(5, n_comp_actual * 1.5), max(4, len(df.columns) * 0.3)))
        sns.heatmap(loadings, annot=len(df.columns) <= 20, fmt=".2f",
                    cmap="coolwarm", center=0, linewidths=0.4, ax=ax)
        ax.set_title("Feature Loadings per Component")
        st.pyplot(fig)

    #variance summary table
    st.divider()
    st.subheader("Variance Summary")
    st.write("A breakdown of how much variance each component explains individually and cumulatively. "
             "Use this to decide whether your selected number of components is sufficient.")
    st.dataframe(pd.DataFrame({
        "Component": [f"PC{i+1}" for i in range(n_comp_actual)],
        "Explained Var (%)": (exp_var * 100).round(2),
        "Cumulative Var (%)": (np.cumsum(exp_var) * 100).round(2),
    }), hide_index=True)
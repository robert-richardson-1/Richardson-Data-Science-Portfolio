# MLStreamlitApp

This project is an interactive supervised machine learning web application built with Streamlit. Users can explore two sample datasets: Iris and Breast Cancer, or upload their own CSV, then train either a Decision Tree or Logistic Regression classifier with adjustable hyperparameters. The app displays a dataset preview and model performance metrics in real time.

Key ML concepts applied: supervised classification, train/test splitting, hyperparameter tuning via interactive widgets, and performance evaluation.

## How to Run

- **Install dependencies:** `pip install streamlit scikit-learn pandas numpy matplotlib seaborn`
- **Run locally:** "streamlit run main.py"
- **Deployed app:** [View on Streamlit Community Cloud](https://richardson-data-science-portfolio-mlapp.streamlit.app/)

## Libraries Included

- streamlit
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn

## App Features

- **Dataset selection:** Choose from Iris (sample), Breast Cancer (sample), or upload your own CSV file
- **Model selection:** Switch between Decision Tree and Logistic Regression classifiers
- **Hyperparameter tuning:**
  - *Decision Tree:* adjust test set size and max depth via sidebar sliders
  - *Logistic Regression:* adjust test set size and regularization strength (C)
- **Dataset preview:** Displays row count, feature count, class count, and a live data table
- **Performance metrics:** Model accuracy score and confusion matrix heatmap update after each training run

## Dataset Overview

**Source:** Iris and Breast Cancer datasets are built into scikit-learn (`sklearn.datasets`). Iris classifies flower species by petal and sepal measurements across 3 classes (150 rows, 4 features). Breast Cancer classifies tumors as malignant or benign (569 rows, 30 features). Users may also supply their own labeled CSV for classification tasks.

## References

- [Streamlit Documentation](https://docs.streamlit.io)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [scikit-learn Datasets](https://scikit-learn.org/stable/datasets.html)
- [Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
- [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

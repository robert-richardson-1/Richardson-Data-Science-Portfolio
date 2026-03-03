#load data
from sklearn.datasets import fetch_california_housing
import pandas as pd

# Load the housing dataset
housing = fetch_california_housing()

#create dataframe
X = pd.DataFrame(housing.data, columns=housing.feature_names) 
y = pd.Series(housing.target, name='med_house_value')

#initial exploration
df = X.copy()
df["med_house_value"] = y

df.head()

#print names
print("Feature Names:")
print(X.columns)

#check for missing values
print("\nMissing Values per Column:")
print(df.isnull().sum())

#summary statistics
print(df.describe())

from sklearn.model_selection import train_test_split

#80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("training set shape:", X_train.shape)
print("test set shape:", X_test.shape)

from sklearn.linear_model import LinearRegression

#initialize and train model
model = LinearRegression()
model.fit(X_train, y_train)

#predict on test set
y_pred = model.predict(X_test)

#view first 5 predictions
print("first 5 predictions:", y_pred[:5])
print("first 5 actual values:", y_test.values[:5])

#MSE, RMSE, R^2
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)
rmse = np.sqrt(mse)
print("RMSE:", rmse)
r2 = r2_score(y_test, y_pred)
print("R² Score:", r2)
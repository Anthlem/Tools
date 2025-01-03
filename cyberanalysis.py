# -*- coding: utf-8 -*-
"""CyberAnalysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18mgS37mvOBCH5acQIBQZDrKIsj6hK9G5
"""

import pandas as pd

# Load the dataset
file_path = 'C:/Users/bhagi/Documents/Data 1202/dataset_Cyber.csv'
data = pd.read_csv(file_path)

# Drop irrelevant columns including 'hash'
cleaned_data = data.drop(columns=["hash"])



# Display the first few rows of the cleaned dataset
print(cleaned_data.head())

# Save the cleaned dataset to a CSV file
cleaned_file_path = 'cleaned_dataset.csv'
cleaned_data.to_csv(cleaned_file_path, index=False)

# Provide the file path for download
print(f"Dataset saved as: {cleaned_file_path}")

#EDA

import matplotlib.pyplot as plt
import seaborn as sns

data.hist(bins=50, figsize=(20,15))
plt.ylabel('Counts')
plt.show()

"""**Logistic Regression**"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns



# Select only numeric columns for features
X = cleaned_data.select_dtypes(include=['number'])

# Encode target column if it's categorical
y = LabelEncoder().fit_transform(cleaned_data['classification'])  # Adjust column name as needed

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100, stratify=y)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train logistic regression
logreg_model = LogisticRegression(random_state=100, solver='liblinear')
logreg_model.fit(X_train_scaled, y_train)
y_pred = logreg_model.predict(X_test_scaled)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Plot confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

"""**Neural Network**"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns


# Select only numeric columns for features
X = cleaned_data.select_dtypes(include=['number'])

# Encode target column if it's categorical
y = LabelEncoder().fit_transform(cleaned_data['classification'])  # Adjust column name as needed

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100, stratify=y)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the neural network model
mlp = MLPClassifier(hidden_layer_sizes=(8, 4, 2),  # Specify the architecture
                    activation='relu',             # Activation function
                    solver='adam',                 # Optimizer
                    max_iter=10000,                # Number of iterations
                    random_state=100)              # Random seed for reproducibility
mlp.fit(X_train_scaled, y_train)

# Make predictions on the test set
predictions = mlp.predict(X_test_scaled)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")

# Plot the confusion matrix
cm = confusion_matrix(y_test, predictions)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

"""**Decision Tree Classifier**"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns


# Select only numeric columns for features
X = cleaned_data.select_dtypes(include=['number'])

# Encode target column if it's categorical
y = LabelEncoder().fit_transform(cleaned_data['classification'])  # Adjust column name as needed

# Split the dataset
X_train, X_test, y_train, y_test1 = train_test_split(X, y, test_size=0.2, random_state=100, stratify=y)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the Decision Tree Classifier
dt_model = DecisionTreeClassifier(random_state=100)
dt_model.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_predict = dt_model.predict(X_test_scaled)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test1, y_predict))

print("\nClassification Report:")
print(classification_report(y_test1, y_predict))

print(f"Accuracy: {accuracy_score(y_test, y_predict):.2f}")

# Plot the confusion matrix
cm = confusion_matrix(y_test, y_predict)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

"""**Random Forest Classifier**"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns


# Select only numeric columns for features
X = cleaned_data.select_dtypes(include=['number'])

# Encode target column if it's categorical
y = LabelEncoder().fit_transform(cleaned_data['classification'])  # Adjust column name as needed

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100, stratify=y)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)

# Make predictions on the test set
predict = rf_model.predict(X_test_scaled)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, predict))

print("\nClassification Report:")
print(classification_report(y_test, predict))

print(f"Accuracy: {accuracy_score(y_test, predict):.2f}")

# Plot the confusion matrix
cm = confusion_matrix(y_test, predict)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

"""**Naive Bayes**"""

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns

# Select only numeric columns for features
X = cleaned_data.select_dtypes(include=['number'])

# Encode target column if it's categorical
y = LabelEncoder().fit_transform(cleaned_data['classification'])  # Adjust column name as needed

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100, stratify=y)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the Naive Bayes model
nvb_model = GaussianNB()
nvb_model.fit(X_train_scaled, y_train)

# Make predictions on the test set
nv_pred = nvb_model.predict(X_test_scaled)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, nv_pred))

print("\nClassification Report:")
print(classification_report(y_test, nv_pred))

print(f"Accuracy: {accuracy_score(y_test, nv_pred):.2f}")

# Plot the confusion matrix
cm = confusion_matrix(y_test, nv_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()


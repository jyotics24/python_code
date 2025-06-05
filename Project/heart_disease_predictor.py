# Importing necessary libraries
import pandas as pd                  # For handling tabular data
import numpy as np                   # For numerical operations
import matplotlib.pyplot as plt      # For plotting accuracy comparison graph

# Importing machine learning tools
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.linear_model import LogisticRegression   # Logistic Regression model
from sklearn.tree import DecisionTreeClassifier       # Decision Tree model
from sklearn.naive_bayes import GaussianNB            # Naive Bayes model
from sklearn.neighbors import KNeighborsClassifier    # K-Nearest Neighbors model
from sklearn.svm import SVC                           # Support Vector Machine model
from sklearn.metrics import accuracy_score            # For calculating model accuracy
import joblib                                          # For saving model to disk

# Step 1: Load the dataset
df = pd.read_csv("D:/Data_set/framingham.csv")  # File Path

# Step 2: Drop unnecessary columns that are not useful for prediction
df.drop(columns=['education', 'diaBP', 'cigsPerDay'], inplace=True)

# Step 3: Handle missing values by replacing them with the median of each column
df.replace(np.nan, df.median(), inplace=True)

# Step 4: Remove duplicate rows to avoid data bias
df.drop_duplicates(inplace=True)

# Step 5: Split data into input features (X) and output label (Y)
X = df.drop(columns=['TenYearCHD'])  # Features
Y = df['TenYearCHD']                 # Target (1 = Heart Disease in 10 years, 0 = No)

# Step 6: Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=40)

# Step 7: Define multiple machine learning models to train and compare
models = {
    'Logistic Regression': LogisticRegression(solver='liblinear'),
    'Decision Tree': DecisionTreeClassifier(random_state=5),
    'Naive Bayes': GaussianNB(),
    'KNN': KNeighborsClassifier(n_neighbors=7),
    'SVM': SVC(C=1, kernel='rbf')
}

# Step 8: Dictionary to store the accuracy of each model
accuracies = {}

# Step 9: Train and evaluate each model
for name, model in models.items():
    model.fit(X_train, Y_train)                    # Train the model
    preds = model.predict(X_test)                  # Predict on test data
    acc = accuracy_score(Y_test, preds)            # Calculate accuracy
    accuracies[name] = round(acc * 100, 2)         # Store rounded accuracy
    print(f"{name} Accuracy: {accuracies[name]}%") # Print model accuracy

# Step 10: Save the best model (Logistic Regression) to a .pkl file
joblib.dump(models['Logistic Regression'], 'model.pkl')
print("Logistic Regression model saved as 'model.pkl'")

# Step 11: Plot a bar graph comparing model accuracies with values on bars
plt.figure(figsize=(10, 6))
bars = plt.bar(accuracies.keys(), accuracies.values(), color=['blue', 'green', 'orange', 'purple', 'red'])
# Add accuracy value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add titles and labels
plt.title("Model Accuracy Comparison")
plt.xlabel("Model")
plt.ylabel("Accuracy (%)")
plt.ylim(0, 110)  # Increase upper limit for visibility of text
plt.grid(axis='y')
plt.tight_layout()
plt.show()
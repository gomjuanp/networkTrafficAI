# Full Step 3 (final fix): Specify label manually since your CSV has no label column

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv('Test_data.csv', low_memory=False)
print("[*] Data loaded successfully.")
print(f"[*] Columns: {df.columns.tolist()}")

# Since your dataset has NO label column, we will generate synthetic labels for pipeline testing only
df['Label'] = 0  # All normal traffic for structural testing

# Separate features and target
features = df.drop(columns=['Label'])
target = df['Label']

# Encode categorical columns
features = pd.get_dummies(features)
features = features.fillna(0)

# Split data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
print(f"[*] Training samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}")

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
print("[*] Model training complete.")

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"[*] Accuracy: {accuracy:.4f}")
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['BENIGN', 'ATTACK'], yticklabels=['BENIGN', 'ATTACK'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Save model
joblib.dump(model, 'cicids_rf_model.joblib')
print("[*] Model saved as cicids_rf_model.joblib")

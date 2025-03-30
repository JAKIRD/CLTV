# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10Wu2jBVl-ZXSBASjnMJVXL2UPMlaisQe
"""

# Install necessary libraries
!pip install pandas scikit-learn joblib gdown

# Import Libraries
import pandas as pd
import gdown
import joblib
from datetime import datetime
import os

# ========== STEP 1: LOAD TRAINED MODEL ==========
model_file = "clv_model.pkl"

if not os.path.exists(model_file):
    # If model is not found, you can manually download it or train it again
    print("Trained model not found. Please train and save the model first.")

else:
    # Load the trained model
    model = joblib.load(model_file)
    print("Model loaded successfully!")

# ========== STEP 2: USER INPUT FOR NEW CUSTOMER ==========
print("\nEnter Customer Details:")

# Get today's date
today = datetime.today()

# Manual input for testing (You can replace this with a UI-based input)
customer_id = input("Enter Customer ID: ")
last_purchase_date = input("Enter last purchase date (YYYY-MM-DD): ")
total_purchases = int(input("Enter total number of purchases: "))
total_spent = float(input("Enter total amount spent: "))

# Convert last purchase date
last_purchase_date = datetime.strptime(last_purchase_date, "%Y-%m-%d")

# Compute RFM Features
recency = (today - last_purchase_date).days  # Days since last purchase
frequency = total_purchases  # Number of purchases
monetary = total_spent  # Total spending

# Display computed RFM values
print(f"\n✅ Computed RFM Values for Customer {customer_id}:")
print(f"📅 Recency: {recency} days")
print(f"🔄 Frequency: {frequency} purchases")
print(f"💰 Monetary: ${monetary:.2f}")

# ========== STEP 3: PREDICT CLTV ==========
# Prepare data for prediction
input_data = pd.DataFrame([[recency, frequency, monetary]], columns=['Recency', 'Frequency', 'CLV'])

# Predict CLV
predicted_clv = model.predict(input_data)[0]

print(f"\n🎯 Predicted CLTV for Customer {customer_id}: ${predicted_clv:.2f}")
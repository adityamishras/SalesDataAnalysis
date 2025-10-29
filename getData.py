# -------------------------------------------
#  SALES DATA ANALYSIS (No Tkinter Required)
# -------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
df = pd.read_csv("dataset/SampleSuperstore.csv", encoding='latin1')

# Step 2: Basic Info
print("Shape of dataset:", df.shape)
print("\n--- Dataset Info ---")
print(df.info())

# Step 3: Check for Missing Values & Duplicates
print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Duplicates ---")
print("Duplicate rows:", df.duplicated().sum())

df.drop_duplicates(inplace=True)
print("Shape after removing duplicates:", df.shape)

# Step 4: Summary Statistics
print("\n--- Statistical Summary ---")
print(df.describe())

# Step 5: Explore Categories
print("\nUnique Categories:", df['Category'].unique())
print("Unique Regions:", df['Region'].unique())
print("Unique Ship Modes:", df['Ship Mode'].unique())

# Step 6: Overall Summary
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_quantity = df['Quantity'].sum()

print("\n--- Overall Summary ---")
print("Total Sales: ₹", round(total_sales, 2))
print("Total Profit: ₹", round(total_profit, 2))
print("Total Quantity Sold:", total_quantity)

# Step 7: Sales and Profit by Category
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

print("\nSales by Category:\n", category_sales)
print("\nProfit by Category:\n", category_profit)

# Step 8: Profit by Region
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print("\nProfit by Region:\n", region_profit)

# Step 9: Top 10 States by Sales
top_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 States by Sales:\n", top_states)

# Step 10: Correlation Matrix
print("\n--- Correlation Matrix ---")
print(df.corr(numeric_only=True))

# -----------------------------
#  VISUALIZATION (Save Charts)
# -----------------------------
output_dir = "charts/"
import os
os.makedirs(output_dir, exist_ok=True)

# 1️ Sales by Category
plt.figure(figsize=(7,4))
sns.barplot(x=category_sales.index, y=category_sales.values, palette='viridis')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(output_dir + "sales_by_category.png")
plt.close()

# 2️ Profit by Region
plt.figure(figsize=(6,4))
sns.barplot(x=region_profit.index, y=region_profit.values, palette='coolwarm')
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig(output_dir + "profit_by_region.png")
plt.close()

# 3️ Top 10 States by Sales
plt.figure(figsize=(10,5))
sns.barplot(x=top_states.index, y=top_states.values, palette='magma')
plt.title("Top 10 States by Sales")
plt.xticks(rotation=45)
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(output_dir + "top_10_states.png")
plt.close()

# 4️ Sales vs Profit
plt.figure(figsize=(7,5))
sns.scatterplot(x='Sales', y='Profit', data=df, hue='Category', palette='Set2')
plt.title("Sales vs Profit by Category")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(output_dir + "sales_vs_profit.png")
plt.close()

# 5️ Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='Blues')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(output_dir + "correlation_heatmap.png")
plt.close()

# Step 11: Save Cleaned Data
df.to_csv("dataset/SampleSuperstore_cleaned.csv", index=False)
print("\n Cleaned dataset saved as 'SampleSuperstore_cleaned.csv'")
print(" Charts saved inside the 'charts/' folder.")

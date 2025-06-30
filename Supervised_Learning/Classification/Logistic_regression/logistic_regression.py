import pandas as pd

# URL for the dataset
DATA_URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"

# Load the dataset into a pandas DataFrame
df = pd.read_csv(DATA_URL)

# Create a copy to keep the original df safe
df_processed = df.copy()

# 1. Encode the target variable 'Churn'
df_processed["Churn"] = df_processed["Churn"].map({"No": 0, "Yes": 1})

# 2. Drop the unnecessary customerID column
df_processed = df_processed.drop("customerID", axis=1)

# 3. Identify all remaining text columns to be one-hot encoded
# We can be clever and ask pandas to find all 'object' type columns
categorical_cols = df_processed.select_dtypes(include=["object"]).columns

# 4. Perform one-hot encoding using pandas get_dummies()
df_processed = pd.get_dummies(df_processed, columns=categorical_cols, drop_first=True)

# 'drop_first=True' is a good practice to avoid redundancy.
# For a 'gender' column (Male/Female), it creates only one new column 'gender_Male'.
# If 'gender_Male' is 1, they are Male. If it's 0, they must be Female.

# Let's look at the result!
print("--- DataFrame after Encoding ---")
print(df_processed.info())

print("\n--- First 5 rows of the new data ---")
print(df_processed.head())

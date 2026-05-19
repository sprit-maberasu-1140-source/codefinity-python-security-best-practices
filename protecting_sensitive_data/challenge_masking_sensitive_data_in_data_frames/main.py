import pandas as pd

def mask_sensitive_data(df, sensitive_columns):
    df_copy = df.copy()
    for col in sensitive_columns:
        if col in df_copy.columns:
            df_copy[col] = "***MASKED***"
    return df_copy

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "ssn": ["123-45-6789", "987-65-4321", "555-66-7777"],
    "email": ["alice@example.com", "bob@example.com", "charlie@example.com"]
}
df = pd.DataFrame(data)

sensitive_columns = ["ssn", "email"]
masked_df = mask_sensitive_data(df, sensitive_columns)
print(masked_df)

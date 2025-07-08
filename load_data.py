import pandas as pd
import sqlite3

# Load CSV into DataFrame
df = pd.read_csv("sales.csv")

# Connect fo SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("sales_data.db")

# Write data to SQL table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("CSV loaded into SQLite database successfully")



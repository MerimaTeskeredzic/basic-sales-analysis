import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Connect to database
conn = sqlite3.connect("sales_data.db")

# SQL query: total quantity sold per product
query = """
SELECT product, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product
ORDER BY total_quantity DESC;
"""

# Load data into DataFrame
df = pd.read_sql(query, conn)
print(df)


# Plot the result - Costumize

plt.style.use("fivethirtyeight")  # optional built-in style
rcParams['font.family'] = 'DejaVu Sans'  # you can change this to any installed font

# Create figure and axis
fig, ax = plt.subplots(figsize=(5, 5))  # size in inches

# Plot with pink bars
ax.bar(df['product'], df['total_quantity'], color="#d62aa5")  # hex code for hot pink

# Titles and labels
ax.set_title("Total Quantity Sold per Product", fontsize=14, fontweight='bold')
ax.set_ylabel("Quantity", fontsize=12)

# Grid and layout tweaks
ax.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# Show chart
plt.show()




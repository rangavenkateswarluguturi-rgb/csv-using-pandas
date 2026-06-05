import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales.csv')

print(df)

# Group by Product and sum Sales
sale = df.groupby("Product")["Sales"].sum()

print("\nTotal Sales by Product:")
print(sale)

# Plot chart
sale.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()
import pandas as pd

df = pd.read_csv("Cleaned_Sales_Dataset.csv")

# Total Revenue
total_revenue = df['Total_Sales'].sum()

# Total Orders
total_orders = df['Order_ID'].nunique()

# Average Order Value
average_order_value = total_revenue / total_orders

# Average Age
average_age = df['Age'].mean()

print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Average Order Value:", round(average_order_value,2))
print("Average Age:", round(average_age,2))
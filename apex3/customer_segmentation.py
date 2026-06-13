import pandas as pd

df = pd.read_csv("Cleaned_Sales_Dataset.csv")

# Customer Revenue
customer_sales = df.groupby(
    'Customer_ID'
)['Total_Sales'].sum().reset_index()

# Segment Customers
customer_sales['Segment'] = pd.cut(
    customer_sales['Total_Sales'],
    bins=[0,50000,150000,500000],
    labels=[
        'Low Value',
        'Medium Value',
        'High Value'
    ]
)

print(customer_sales.head())

customer_sales.to_csv(
    "customer_segments.csv",
    index=False
)
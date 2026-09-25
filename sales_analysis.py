import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Order ID": [
        "O001", "O002", "O003", "O004", "O005",
        "O006", "O007", "O008", "O009", "O010",
        "O011", "O012", "O013", "O014", "O015"
    ],

    "Product": [
        "Laptop", "Mouse", "Keyboard", "Monitor", "Laptop",
        "Headphones", "Mouse", "Keyboard", "Monitor", "Laptop",
        "Headphones", "Mouse", "Keyboard", "Monitor", "Laptop"
    ],

    "Category": [
        "Electronics", "Accessories", "Accessories", "Electronics", "Electronics",
        "Accessories", "Accessories", "Accessories", "Electronics", "Electronics",
        "Accessories", "Accessories", "Accessories", "Electronics", "Electronics"
    ],

    "Date": [
        "2026-01-05", "2026-01-10", "2026-01-15", "2026-01-20", "2026-02-05",
        "2026-02-10", "2026-02-15", "2026-02-20", "2026-03-05", "2026-03-10",
        "2026-03-15", "2026-03-20", "2026-04-05", "2026-04-10", "2026-04-15"
    ],

    "Quantity": [
        2, 10, 5, 3, 1,
        6, 12, 7, 4, 2,
        8, 15, 10, 5, 3
    ],

    "Price": [
        55000, 800, 1500, 12000, 55000,
        2500, 800, 1500, 12000, 55000,
        2500, 800, 1500, 12000, 55000
    ]
}

df = pd.DataFrame(data)

df["Sales Amount"] = df["Quantity"] * df["Price"]

print(df)
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("\nCleaned Dataset:")
print(df)
total_sales = df["Sales Amount"].sum()

print("\nTotal Sales:", total_sales)
total_quantity = df["Quantity"].sum()

print("Total Quantity Sold:", total_quantity)
average_order_value = df["Sales Amount"].mean()

print("Average Order Value:", average_order_value)
product_quantity = df.groupby("Product")["Quantity"].sum()

best_selling_product = product_quantity.idxmax()

print("Best-Selling Product:", best_selling_product)
category_sales = df.groupby("Category")["Sales Amount"].sum()

best_category = category_sales.idxmax()

print("Best-Performing Category:", best_category)
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales Amount"].sum()

print("\nMonthly Sales:")
print(monthly_sales)
plt.figure(figsize=(8, 5))

monthly_sales.plot(kind="bar")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales Amount")

plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()
product_sales = df.groupby("Product")["Sales Amount"].sum()

plt.figure(figsize=(8, 5))

product_sales.plot(kind="bar")

plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales Amount")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("product_sales.png")
plt.show()
category_sales = df.groupby("Category")["Sales Amount"].sum()

plt.figure(figsize=(7, 5))

category_sales.plot(kind="bar")

plt.title("Category Sales")
plt.xlabel("Category")
plt.ylabel("Sales Amount")

plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()
top_products = product_sales.sort_values(ascending=False).head(5)

plt.figure(figsize=(8, 5))

top_products.plot(kind="bar")

plt.title("Top Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales Amount")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("top_products.png")
plt.show()
print("\n--- BUSINESS INSIGHTS ---")

print("Total Sales:", total_sales)
print("Total Quantity Sold:", total_quantity)
print("Average Order Value:", round(average_order_value, 2))
print("Best-Selling Product:", best_selling_product)
print("Best-Performing Category:", best_category)
df.to_csv("cleaned_sales_data.csv", index=False)
print("Cleaned dataset saved successfully.")
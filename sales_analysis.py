import pandas as pd
import numpy as np

# Predefined product catalog with categories
store_catalog = {
    "Electronics": {"laptop": 63000, "phone": 16000, "tablet": 25000},
    "Accessories": {"headphones": 2000, "mouse": 800, "keyboard": 1500},
    "Appliances": {"fridge": 30000, "washing machine": 20000, "microwave": 8000}
}

print("\n🛒 Available Products in Store (by Category):")
for category, products in store_catalog.items():
    print(f"\n📂 {category}:")
    for product, price in products.items():
        print(f"   - {product.capitalize()} : ₹{price}")

orders = []

# Take orders from user
while True:
    order_id = input("\nEnter Order ID (or 'stop' to finish): ")
    if order_id.lower() == "stop":
        break

    product = input("Enter Product Name: ").lower()
    quantity = int(input("Enter Quantity: "))

    # Search in catalog
    found = False
    for category, products in store_catalog.items():
        if product in products:
            price = products[product]
            found = True
            break

    if not found:
        print("❌ Product not found! Please choose from the available list.")
        continue

    orders.append((order_id, product, price, quantity))

# Create DataFrame
df = pd.DataFrame(orders, columns=["OrderID", "Product", "Price", "Quantity"])
df["Total"] = df["Price"] * df["Quantity"]

print("\n📊 Order Details:")
print(df)

# 1. Total revenue
print("\n💰 Total Revenue: ₹", df["Total"].sum())

# 2. Best-selling product
best_seller = df.groupby("Product")["Quantity"].sum().idxmax()
print("🏆 Best-Selling Product:", best_seller)

# 3. Average price & price stats
print("📈 Average Price:", df["Price"].mean())
print("📉 Price Standard Deviation:", np.std(df["Price"]))

# 4. Highest revenue order
highest_order = df.loc[df["Total"].idxmax()]
print("\n💎 Highest Revenue Order:")
print(highest_order)

# 5. Save report
df.to_csv("sales_report.csv", index=False)
print("\n💾 Sales report saved as 'sales_report.csv'")

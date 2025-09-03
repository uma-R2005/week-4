import pandas as pd
import numpy as np

# Initial Inventory
inventory_data = {
    "Product": ["Rice", "Sugar", "Milk", "Bread", "Oil"],
    "Price": [50, 40, 30, 25, 120],
    "Stock": [10, 8, 15, 12, 5]
}

inventory = pd.DataFrame(inventory_data)

print("🏪 Welcome to Supermarket Billing System 🛒")

cart = []

while True:
    print("\n📦 Available Products:")
    print(inventory)

    product = input("\nEnter product to buy (or 'done' to finish): ").capitalize()
    if product.lower() == "done":
        break

    if product not in inventory["Product"].values:
        print("❌ Product not found! Please choose from the list.")
        continue

    quantity = int(input("Enter quantity: "))

    stock = inventory.loc[inventory["Product"] == product, "Stock"].values[0]
    if quantity > stock:
        print(f"⚠️ Only {stock} items available. Try again.")
        continue

    price = inventory.loc[inventory["Product"] == product, "Price"].values[0]
    cart.append([product, price, quantity, price * quantity])

    # Reduce stock
    inventory.loc[inventory["Product"] == product, "Stock"] -= quantity

# Create bill DataFrame
bill = pd.DataFrame(cart, columns=["Product", "Price", "Quantity", "Total"])

print("\n🧾 Purchase Summary:")
print(bill)

# Subtotal
subtotal = bill["Total"].sum()

# Discount: 10% off if bill > 5000
discount = np.where(subtotal > 5000, subtotal * 0.10, 0)

# GST: 5%
tax = (subtotal - discount) * 0.05

final_amount = subtotal - discount + tax

print("\n💰 Billing Details:")
print(f"Subtotal: ₹{subtotal}")
print(f"Discount: ₹{discount}")
print(f"GST (5%): ₹{tax:.2f}")
print("-------------------------")
print(f"Final Amount: ₹{final_amount:.2f}")

print("\n📦 Inventory After Purchase:")
print(inventory)

# Save bill & inventory
bill.to_csv("bill_report.csv", index=False)
inventory.to_csv("updated_inventory.csv", index=False)

print("\n💾 Bill saved as 'bill_report.csv'")
print("💾 Updated inventory saved as 'updated_inventory.csv'")

from itertools import combinations

# Product catalog with prices
products = {
    "Laptop": 800,
    "Mouse": 25,
    "Keyboard": 50,
    "Monitor": 200,
    "Headphones": 75
}

# Desired size of each bundle (e.g., pairs, triplets, etc.)
combo_size = 2

# Optional: Filter bundles under this total price (set to None to disable)
max_total_price = 300

# Generate all combinations of the specified size
product_combos = combinations(products.items(), combo_size)

# Display header
print(f"\nAll product bundles of size {combo_size}", end="")
if max_total_price:
    print(f" under ${max_total_price}:\n")
else:
    print(":\n")

# Loop through and display each valid combo
for combo in product_combos:
    names = [item[0] for item in combo]
    prices = [item[1] for item in combo]
    total = sum(prices)

    if max_total_price is None or total <= max_total_price:
        combo_str = " + ".join(names)
        print(f"{combo_str} = ${total}")

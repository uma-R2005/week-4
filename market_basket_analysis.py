from itertools import combinations
from collections import Counter

# Sample transaction list
transactions = [
    ['milk', 'bread', 'eggs'],
    ['milk', 'bread'],
    ['milk', 'eggs'],
    ['bread', 'eggs'],
    ['milk', 'bread', 'butter'],
]

# Step 1: Generate all item pairs from each transaction
all_pairs = []

for items in transactions:
    # Get all unique 2-item combinations from each transaction
    pairs = combinations(sorted(items), 2)  # sort for consistency
    all_pairs.extend(pairs)

# Step 2: Count how often each pair appears
pair_counts = Counter(all_pairs)

# Step 3: Display the most common pairs
for pair, count in pair_counts.most_common():
    print(f"{pair}: {count} times")

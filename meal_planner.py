from itertools import combinations
from collections import Counter

# Step 1: Define available ingredients
ingredients = [
    'chicken', 'rice', 'broccoli', 'tofu',
    'beans', 'quinoa', 'spinach', 'avocado'
]

# Step 2: Generate all possible 3-ingredient meal combinations
meal_combos = list(combinations(ingredients, 3))

# Optional: Limit to 10 planned meals (for this example)
planned_meals = meal_combos[:10]

# Step 3: Count ingredient usage across all meals
ingredient_usage = Counter()

for meal in planned_meals:
    ingredient_usage.update(meal)

# Step 4: Print meals and ingredient stats
print("🍱 Planned Meals:")
for i, meal in enumerate(planned_meals, 1):
    print(f"Meal {i}: {meal}")

print("\n📊 Ingredient Usage:")
for ingredient, count in ingredient_usage.items():
    print(f"{ingredient}: used in {count} meal(s)")

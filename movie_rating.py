import pandas as pd
import numpy as np

print("🎬 Welcome to Movie Rating & Recommendation System 🎥")

movies = []

while True:
    movie = input("\nEnter movie name (or 'done' to finish): ").title()
    if movie.lower() == "done":
        break
    
    try:
        rating = float(input("Enter your rating (1 to 5): "))
        if rating < 1 or rating > 5:
            print("❌ Rating must be between 1 and 5.")
            continue
    except ValueError:
        print("❌ Invalid input. Please enter a number between 1 and 5.")
        continue
    
    movies.append([movie, rating])

# Convert to DataFrame
df = pd.DataFrame(movies, columns=["Movie", "Rating"])

print("\n⭐ All Ratings:")
print(df)

# Average rating per movie
avg_rating = df.groupby("Movie")["Rating"].mean()
print("\n📊 Average Ratings per Movie:")
print(avg_rating)

# Most watched movie
most_watched = df["Movie"].mode()[0]
print("\n👀 Most Watched Movie:", most_watched)

# Highest rated movie
highest_rated = avg_rating.idxmax()
print("🏆 Highest Rated Movie:", highest_rated)

# Recommendation
df["Recommendation"] = np.where(df["Rating"] >= 4, "👍 Recommended", "👎 Not Recommended")
print("\n✅ Final Ratings with Recommendation:")
print(df)

# Save to CSV
df.to_csv("movie_ratings.csv", index=False)
print("\n💾 Ratings saved as 'movie_ratings.csv'")

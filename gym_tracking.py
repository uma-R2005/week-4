import pandas as pd
import numpy as np

print("🏋️ Welcome to Gym Membership & Workout Tracking System 💪")

members = []
fees = {"Monthly": 1000, "Quarterly": 2500, "Yearly": 9000}  # Example fees

while True:
    name = input("\nEnter member name (or 'done' to finish): ").title()
    if name.lower() == "done":
        break

    membership = input("Enter membership type (Monthly/Quarterly/Yearly): ").title()
    if membership not in fees:
        print("❌ Invalid membership type. Choose Monthly, Quarterly, or Yearly.")
        continue

    try:
        hours = float(input("Enter total workout hours this month: "))
    except ValueError:
        print("❌ Invalid input for hours.")
        continue

    fee = fees[membership]
    members.append([name, membership, fee, hours])

# Convert to DataFrame
df = pd.DataFrame(members, columns=["Name", "Membership", "Fee", "WorkoutHours"])

print("\n📋 Gym Member Details:")
print(df)

# Total revenue
total_revenue = df["Fee"].sum()
print("\n💰 Total Revenue from Memberships:", total_revenue)

# Average workout hours
avg_hours = np.mean(df["WorkoutHours"])
print("📊 Average Workout Hours:", avg_hours)

# Most active member
most_active = df.loc[df["WorkoutHours"].idxmax()]
print("\n🔥 Most Active Member:")
print(most_active)

# Most popular membership type
popular_membership = df["Membership"].mode()[0]
print("\n🏆 Most Popular Membership:", popular_membership)

# Save to CSV
df.to_csv("gym_report.csv", index=False)
print("\n💾 Gym report saved as 'gym_report.csv'")

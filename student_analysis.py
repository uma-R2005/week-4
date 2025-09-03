import pandas as pd
import numpy as np

# Number of students
n = int(input("Enter number of students: "))

students = []
for i in range(n):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Name: ")
    m1 = int(input("Marks in Math: "))
    m2 = int(input("Marks in Science: "))
    m3 = int(input("Marks in English: "))

    students.append([name, m1, m2, m3])

# Create DataFrame
df = pd.DataFrame(students, columns=["Name", "Math", "Science", "English"])

# Add total and average
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Pass/Fail (>= 40 in each subject to pass)
df["Status"] = np.where((df[["Math","Science","English"]] >= 40).all(axis=1), "Pass", "Fail")

print("\n📘 Student Performance Table:")
print(df)

# Top scorer
top_student = df.loc[df["Total"].idxmax()]
print("\n🏆 Top Scorer:")
print(top_student)

# Subject-wise topper
print("\n🔹 Subject-wise Toppers:")
for subject in ["Math", "Science", "English"]:
    topper = df.loc[df[subject].idxmax()]
    print(f"{subject}: {topper['Name']} ({topper[subject]} marks)")

# Class average per subject
print("\n📊 Class Average Marks:")
print(df[["Math", "Science", "English"]].mean())

# Sort by total marks
sorted_df = df.sort_values(by="Total", ascending=False)
print("\n📑 Students Sorted by Total Marks:")
print(sorted_df)

# Save to CSV
df.to_csv("student_report.csv", index=False)
print("\n📁 Student report saved as 'student_report.csv'")

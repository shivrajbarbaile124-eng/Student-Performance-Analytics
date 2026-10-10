
import pandas as pd
import numpy as np

# Read student data
students = pd.read_csv("students.csv")

# Subject names
subjects = [
    "Python",
    "Statistics",
    "Mathematics",
    "AI",
    "Data_Analysis"
]

# Calculate total and average
students["Total"] = students[subjects].sum(axis=1)
students["Average"] = students[subjects].mean(axis=1).round(2)


# Function to calculate grades
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 35:
        return "E"
    else:
        return "F"


# Function to check pass or fail
def calculate_result(row):
    for subject in subjects:
        if row[subject] < 35:
            return "Fail"
    return "Pass"


# Apply functions to every student
students["Grade"] = students["Average"].apply(calculate_grade)
students["Result"] = students.apply(calculate_result, axis=1)

# Display student results
print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 65)

print(
    students[
        ["Name", "Total", "Average", "Grade", "Result"]
    ].to_string(index=False)
)

# Class summary
print("\nCLASS SUMMARY")
print("-" * 40)

print("Total students:", len(students))
print("Class average:", round(students["Average"].mean(), 2))
print("Highest average:", students["Average"].max())
print("Lowest average:", students["Average"].min())

print("Students passed:", (students["Result"] == "Pass").sum())
print("Students failed:", (students["Result"] == "Fail").sum())
pass_percentage = (students["Result"].eq("Pass").sum() / len(students)) * 100
print("Pass percentage:", round(pass_percentage, 2), "%")

# NumPy calculations
averages = students["Average"].to_numpy()
print("Median average:", np.median(averages))

# Save results
students.to_csv("student_results.csv", index=False)
print("\nResults saved to student_results.csv")



# Subject-wise performance analysis
print("\nSUBJECT-WISE PERFORMANCE")
print("-" * 40)

subject_averages = students[subjects].mean().round(2)

for subject, average in subject_averages.items():
    print(subject, "average:", average)

print("Best subject:", subject_averages.idxmax())
print("Lowest-average subject:", subject_averages.idxmin())



# Display the top five students
print("\nTOP FIVE STUDENTS")
print("-" * 40)

top_students = students.nlargest(5, "Average")

print(
    top_students[
        ["Name", "Average", "Grade", "Result"]
    ].to_string(index=False)
)

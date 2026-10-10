
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Performance Analytics System")
st.write(
    "Welcome! Use this dashboard to explore student "
    "marks, grades, attendance, and academic performance."
)


@st.cache_data
def load_data():
    return pd.read_csv("students.csv")


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
    return "F"


def calculate_result(row, subjects):
    for subject in subjects:
        if row[subject] < 35:
            return "Fail"
    return "Pass"


try:
    students = load_data()
except FileNotFoundError:
    st.error("students.csv was not found in the project folder.")
    st.stop()

st.success("Student dataset loaded successfully!")

uploaded_file = st.file_uploader(
    "Upload a student CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        students = pd.read_csv(uploaded_file)
        st.success("Uploaded dataset loaded successfully!")
    except Exception as error:
        st.error(f"Could not read the uploaded CSV: {error}")
        st.stop()

subjects = [
    "Python", "Statistics", "Mathematics",
    "AI", "Data_Analysis"
]

required_columns = [
    "Student_ID", "Name", "Department",
    *subjects, "Attendance"
]

missing_columns = [
    column for column in required_columns
    if column not in students.columns
]

if missing_columns:
    st.error(
        "The dataset is missing these required columns: "
        + ", ".join(missing_columns)
    )
    st.stop()

try:
    students[subjects] = students[subjects].apply(
        pd.to_numeric, errors="raise"
    )
    students["Attendance"] = pd.to_numeric(
        students["Attendance"], errors="raise"
    )
except (ValueError, TypeError):
    st.error("Marks and attendance must contain numeric values.")
    st.stop()

if students.empty:
    st.warning("The uploaded dataset contains no student records.")
    st.stop()

students["Total"] = students[subjects].sum(axis=1)
students["Average"] = students[subjects].mean(axis=1).round(2)
students["Grade"] = students["Average"].apply(calculate_grade)
students["Result"] = students.apply(
    lambda row: calculate_result(row, subjects), axis=1
)

st.subheader("Class Performance Overview")

total_students = len(students)
class_average = students["Average"].mean()
highest_average = students["Average"].max()
pass_percentage = (
    (students["Result"] == "Pass").sum()
    / total_students
) * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", total_students)
col2.metric("Class Average", f"{class_average:.2f}%")
col3.metric("Highest Average", f"{highest_average:.2f}%")
col4.metric("Pass Percentage", f"{pass_percentage:.1f}%")

st.subheader("🏆 Top 5 Performing Students")

top_students = students.nlargest(5, "Average")

st.dataframe(
    top_students[
        ["Student_ID", "Name", "Average", "Grade", "Result"]
    ].reset_index(drop=True),
    use_container_width=True,
    hide_index=True
)

st.subheader("🔎 Search and Filter Students")

search_name = st.text_input("Search by student name or ID")

col_filter1, col_filter2 = st.columns(2)

with col_filter1:
    grade_options = ["All"] + sorted(
        students["Grade"].unique().tolist()
    )
    selected_grade = st.selectbox(
        "Filter by Grade", grade_options
    )

with col_filter2:
    selected_result = st.selectbox(
        "Filter by Result", ["All", "Pass", "Fail"]
    )

filtered_students = students.copy()

if search_name.strip():
    filtered_students = filtered_students[
        filtered_students["Name"].astype(str).str.contains(
            search_name.strip(), case=False, na=False
        )
        | filtered_students["Student_ID"].astype(str).str.contains(
            search_name.strip(), na=False
        )
    ]

if selected_grade != "All":
    filtered_students = filtered_students[
        filtered_students["Grade"] == selected_grade
    ]

if selected_result != "All":
    filtered_students = filtered_students[
        filtered_students["Result"] == selected_result
    ]

st.caption(
    f"Showing {len(filtered_students)} of {len(students)} students"
)

st.dataframe(
    filtered_students,
    use_container_width=True,
    hide_index=True
)

st.download_button(
    label="📥 Download Student Report",
    data=filtered_students.to_csv(index=False).encode("utf-8"),
    file_name="student_performance_report.csv",
    mime="text/csv"
)


st.subheader("Dataset Overview")

col1, col2 = st.columns(2)
col1.metric("Total Students", total_students)
col2.metric("Total Subjects", len(subjects))

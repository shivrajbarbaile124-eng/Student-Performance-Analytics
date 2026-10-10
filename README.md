
# Student Performance Analytics System

## Project Overview
The Student Performance Analytics System is a Python-based project that analyzes student marks and generates useful academic performance reports.

## Objectives
- Calculate total and average marks for students.
- Assign grades based on average marks.
- Identify pass and fail students.
- Calculate class average and pass percentage.
- Analyze subject-wise performance.
- Identify the top five performing students.
- Upload a student dataset in CSV format.
- Search students by name or ID.
- Filter students by grade and result.
- Download analyzed student reports as CSV files.
## Technologies Used
- Python
- NumPy
- Pandas
- Streamlit
- Matplotlib
- CSV dataset
- Visual Studio Code
- GitHub

## Project Files
- `main.py`: Main Python program for student performance analysis.
- `app.py`: Interactive Streamlit dashboard with search, filters, charts, CSV upload, and report download.
- `students.csv`: Fictional sample student dataset.
- `student_results.csv`: Generated student analysis results.
- `requirements.txt`: Required Python libraries.
- `README.md`: Project documentation.
## How to Run
1. Install Python.
2. Open the project folder in VS Code.
3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Python analysis program:

   ```bash
   python main.py
   ```

5. Launch the interactive Streamlit dashboard:

   ```bash
   python -m streamlit run app.py
   ```

6. Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Dataset
The project uses 20 fictional sample student records for educational purposes.

## Output
The program displays student totals, averages, grades, pass/fail results, class statistics, subject-wise averages, and the top five students.

## Conclusion
This project demonstrates how Python, NumPy, and Pandas can be used to analyze student performance and generate reports.

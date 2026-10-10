
# Student Performance Analytics System

## Project Overview
The Student Performance Analytics System is a Python-based project that analyzes student marks and generates useful academic performance reports.

## Objectives
- Calculate total and average marks.
- Assign grades to students.
- Identify pass and fail students.
- Calculate class statistics and pass percentage.
- Analyze subject-wise performance.
- Identify the top five performers.
- Export analyzed results to a CSV file.

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
- main.py: Main Python program.
- students.csv: Sample student dataset.
- student_results.csv: Generated analysis results.
- README.md: Project documentation.

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

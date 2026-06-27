# Student Performance Analyzer

A professional Python data analysis tool that reads student academic records from a CSV file, calculates comprehensive grade statistics, identifies top-performing and at-risk students, and exports visual performance charts.

## Features
* Automated Data Pipeline: Reads and cleans raw student records dynamically.
* Smart Performance Metrics: Calculates individual total scores and averages.
* Actionable Insights: Pinpoints the highest-achieving student and flags at-risk individuals needing academic support.
* Data Visualization: Generates and exports clear, publication-quality bar charts comparing student performance and subject averages.

## Technologies Used
* Python 3
* Pandas: For structural data manipulation and statistical filtering.
* Matplotlib: For programmatic data visualization and chart generation.

## Project Structure
```text
Student-Performance-Analyzer/
│
├── data/
│      └── students.csv         # Raw student grades input file
│
├── images/
│      ├── student_averages.png # Auto-generated student comparison chart
│      └── subject_averages.png # Auto-generated subject average comparison
│
├── src/
│      └── main.py              # Main application script
│
└── requirements.txt            # Project dependencies
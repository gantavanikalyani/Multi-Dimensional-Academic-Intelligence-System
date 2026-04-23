# Multi-Dimensional-Academic-Intelligence-System
## Problem Understanding

This program analyzes student performance using multiple factors such as marks, attendance, and assignment scores. It organizes the data and evaluates student performance levels. Finally, it displays categorized results along with a statistical summary and system insight.

## Logic Used

The program uses a list to store student data. A loop is used to generate data for each student using random values. Each student record includes marks, attendance, and assignment scores.

A performance index is calculated using a formula that combines marks, assignment, and attendance.

Students are classified into categories using conditions:

At Risk (marks < 40 or attendance < 50)
Average (marks between 40 and 70)
Good (marks between 71 and 90)
Top Performer (marks > 90 and attendance > 80)

Statistical analysis is performed:

Mean (calculated manually)
Median
Standard Deviation
Correlation between marks and attendance

Marks are also normalized using a formula.

System insight is determined based on:

Consistency (standard deviation)
Attendance risk
Number of top performers
Personalization Applied

The program uses a personalized rule based on the roll number:

Roll Number: 565
Last digit: 5

The number of students generated is equal to the last digit of the roll number.

## Features
Uses list, tuple, set, and dictionary
Uses functions for modular design
Uses random module for data generation
Uses NumPy and Pandas for analysis
Performs classification of students
Calculates statistical measures
Normalizes data
Generates final system insight

## Learning Outcome

This program helps in understanding how to use Python for data analysis. It improves knowledge of data structures, functions, and libraries like NumPy and Pandas. It also helps in applying statistical concepts and building logical solutions for real-world problems.

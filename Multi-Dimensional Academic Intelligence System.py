import random
import math
import numpy as np
import pandas as pd
roll_number = (input("Enter roll number: "))
last_digit = int(roll_number[-1])
num_students = last_digit if last_digit != 0 else 10

def generate_data(n):
    students = []
    for i in range(n):
        student_id = i + 1
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)

        performance_index = (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)

        students.append((student_id, marks, attendance, assignment, performance_index))

    return students

def classify_students(data):
    categories = {}

    for student in data:
        sid, marks, att, assign, pi = student

        if marks < 40 or att < 50:
            category = "At Risk"
        elif 40 <= marks <= 70:
            category = "Average"
        elif 71 <= marks <= 90:
            category = "Good"
        elif marks > 90 and att > 80:
            category = "Top Performer"
        else:
            category = "Average"

        categories[sid] = category

    return categories

def analyze_data(df):
    marks = df['Marks']

    mean_marks = sum(marks) / len(marks)
    median_marks = np.median(marks)
    std_dev = np.std(marks)

    correlation = df['Marks'].corr(df['Attendance'])

    min_m = min(marks)
    max_m = max(marks)

    df['Normalized Marks'] = [(x - min_m) / (max_m - min_m) for x in marks]

    summary_tuple = (mean_marks, std_dev, max_m)
    return mean_marks, median_marks, std_dev, correlation, summary_tuple

data = generate_data(num_students)

df = pd.DataFrame(data, columns=[
    'Student_ID', 'Marks', 'Attendance', 'Assignment', 'Performance_Index'
])

categories = classify_students(data)

mean_m, median_m, std_m, corr, summary_tuple = analyze_data(df)

consistency = "Consistent" if std_m < 15 else "Not Consistent"

attendance_risk = sum(df['Attendance'] < 50)
high_achievers = sum((df['Marks'] > 90) & (df['Attendance'] > 80))

if std_m < 15 and high_achievers >= 2:
    system_status = "Stable Academic System"
elif attendance_risk > 3:
    system_status = "Critical Attention Required"
else:
    system_status = "Moderate Performance"

print("\nStudent Data:")
print(df)
print("\nCategories:")
print(categories)
print("\nStatistics:")
print("Mean:", mean_m)
print("Median:", median_m)
print("Standard Deviation:", std_m)
print("Correlation (Marks vs Attendance):", corr)
print("\nSummary Tuple (Mean, Std Dev, Max Marks)")
print(summary_tuple)
print("\nSystem Insight")
print(system_status)


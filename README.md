# Project 4 – Attendance Recovery Computation System

## Description
The Attendance Recovery Computation System is a Python-based project that calculates a student's current attendance percentage and determines how many additional classes the student must attend to reach the minimum required attendance percentage of 75%.

## Objectives
- Calculate the current attendance percentage.
- Check attendance eligibility.
- Calculate the minimum additional classes required.
- Determine whether the student is already eligible.
- Display the attendance report.

## Concepts Used
- Variables and Data Types
- User Input
- Arithmetic Operators
- Conditional Statements (if, else)
- Mathematical Calculations

## Attendance Calculation Assumptions
- Minimum required attendance: 75%.
- Total classes and attended classes are entered by the user.
- The student attends every additional class.
- Additional classes are calculated as whole numbers.

## Formula
**Attendance Percentage:**

Attendance = (Attended Classes / Total Classes) × 100

**Additional Classes Required:**

Additional Classes = (0.75 × Total Classes − Attended Classes) / 0.25

The result is rounded up to the next whole number when necessary.

## Sample Output
```text
Enter Total Classes: 100
Enter Attended Classes: 60

Current Attendance: 60.00%
Required Attendance: 75%
Additional Classes Required: 60
Final Attendance: 75.00%
Status: ELIGIBLE AFTER ATTENDING 60 MORE CLASSES
```

## How to Run
1. Open the project folder in VS Code.
2. Open the Python source file.
3. Run the program.
4. Enter the total number of classes.
5. Enter the number of classes attended.
6. View the attendance percentage and additional classes required.

## Conclusion
This project demonstrates how Python can be used to calculate attendance percentages and determine the additional classes required to achieve attendance eligibility. It helps understand variables, arithmetic operators, conditional statements, and mathematical calculations.

# Syntax Exercise #5
# Given n student grades, calculate:
# How many grades are passing (greater than or equal to 70).
# How many grades are failing (less than 70).
# The average of all grades.
# The average of passing grades.
# The average of failing grades.

# Initialize variables
grade_counter = 1
passing_count = 0
failing_count = 0
passing_average_sum = 0
failing_average_sum = 0
overall_average = 0

# Ask how many grades will be entered
total_grades = int(input("Enter the number of grades: "))

# Loop to enter each grade
while grade_counter <= total_grades:
    print(f"Enter grade number {grade_counter}:")
    current_grade = float(input("> "))

    # Classify the grade
    if current_grade < 70:
        failing_count += 1
        failing_average_sum += current_grade
    else:
        passing_count += 1
        passing_average_sum += current_grade

    overall_average += current_grade / total_grades

    grade_counter += 1

# Prevent division errors if there were no passing or failing grades
if passing_count > 0:
    passing_average_sum /= passing_count
else:
    passing_average_sum = 0

if failing_count > 0:
    failing_average_sum /= failing_count
else:
    failing_average_sum = 0

# Display results
print("\n📊 RESULTS 📊")
print(f"✔️ Passing grades: {passing_count}")
print(f"⭐ Average of passing grades: {passing_average_sum:.2f}")

print(f"❌ Failing grades: {failing_count}")
print(f"📉 Average of failing grades: {failing_average_sum:.2f}")

print(f"📌 Overall grade average: {overall_average:.2f}")

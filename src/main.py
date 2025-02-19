def main():
    """Prints 'Hello, World!' to the console."""
    print("Hello, World!")


# Function to calculate student grades
def calculate_grade(scores)
    total = 0
    for score in Scores:  # Variable name case mismatch
        total += score
    
    average = total / len(scores)
    
    if average >= 90
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70
        return 'C'
    else:
        return F  # Missing quotes around string



if __name__ == "__main__":

    # List to store student information
student_data = [
    {'name': 'Alice', 'scores': [85, 92, 88]},
    {'name': 'Bob', 'scores': [78, 85, 80]},
    {'name': 'Charlie' 'scores': [92, 95, 89]}  # Missing comma
]

# Try to process each student
for student in student_data:
    grade = calculate_grade(student['scores']
    print(f"{student['name']}'s grade is: {grade}")
    main()

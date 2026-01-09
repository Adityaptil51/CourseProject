# Program to calculate student grade
import sys

def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3


def assign_grade(average):
    if average >= 90:
        return "S"
    elif average >= 80:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    print("=== Student Grade Calculator ===")

    try:
        # If user gives input through command line
        if len(sys.argv) == 7:
            name = sys.argv[1]
            department = sys.argv[2]
            semester = int(sys.argv[3])
            m1 = float(sys.argv[4])
            m2 = float(sys.argv[5])
            m3 = float(sys.argv[6])
        else:
            # Take user input
            name = input("Enter student name: ")
            department = input("Enter department: ")
            semester = int(input("Enter semester: "))
            m1 = float(input("Enter marks in subject 1: "))
            m2 = float(input("Enter marks in subject 2: "))
            m3 = float(input("Enter marks in subject 3: "))

        print("\n=== Program Parameters ===")
        print(f"Student Name: {name}")
        print(f"Department: {department}")
        print(f"Semester: {semester}")
        print(f"Marks: {m1}, {m2}, {m3}")

        average = calculate_average(m1, m2, m3)
        grade = assign_grade(average)

        print(f"\nAverage Marks: {average:.2f}")
        print(f"Grade: {grade}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
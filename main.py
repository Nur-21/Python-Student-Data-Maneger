# Student class to represent student objects
class Student:
    def __init__(self, student_number, first_name, last_name, date_of_birth, sex, country):
        self.__student_number = student_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__sex = sex
        self.__country = country

    # Getters methods 
    def get_student_number(self):
        return self.__student_number

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_sex(self):
        return self.__sex

    def get_country(self):
        return self.__country

    # Setters
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def set_sex(self, sex):
        self.__sex = sex

    def set_country(self, country):
        self.__country = country


# Add a new student
def add_student(students_data):
    if len(students_data) < 100:
        student_number = input("Enter student number: ")
        first_name = input("Enter student first name: ")
        last_name = input("Enter student last name: ")
        date_of_birth = input("Enter student date of birth (YYYY-MM-DD): ")
        sex = input("Enter student sex: ")
        country = input("Enter student country: ")
        students_data.append(Student(student_number, first_name, last_name, date_of_birth, sex, country))
        print("Student added successfully!")
    else:
        print("Maximum limit of students reached (100 students).")


# Find a student by student number
def find_by_student_number(students_data):
    student_number = input("Enter student number to find details: ")
    found = False
    for student in students_data:
        if student.get_student_number() == student_number:
            found = True
            print("Student Number:", student.get_student_number())
            print("First Name:", student.get_first_name())
            print("Last Name:", student.get_last_name())
            print("Date of Birth:", student.get_date_of_birth())
            print("Sex:", student.get_sex())
            print("Country:", student.get_country())
            # Calculate and print age based on date of birth
            print("Age:", calculate_age(student.get_date_of_birth()))
            break
    if not found:
        print("No student found with the given student number.")


# Show all students    
def show_all_students(students_data):
    if not students_data:
        print("No students data available.")
    else:
        headers = ["Student Number", "First Name", "Last Name", "Date of Birth", "Sex", "Country"]
        values = [[] for _ in range(len(headers))]
        for student in students_data:
            values[0].append(str(student.get_student_number()))
            values[1].append(student.get_first_name())
            values[2].append(student.get_last_name())
            values[3].append(str(student.get_date_of_birth()))
            values[4].append(student.get_sex())
            values[5].append(student.get_country())

        # Calculate the maximum width for each column
        column_widths = [max(len(header), max(len(value) for value in col)) for header, col in zip(headers, values)]
        
        # Print headers
        for header, width in zip(headers, column_widths):
            print(header.ljust(width + 2), end='')
        print()

        # Print values under each header
        for i in range(len(students_data)):
            for value, width in zip(values, column_widths):
                print(value[i].ljust(width + 2), end='') 
            print() 

            
def show_students_by_birth_year(students_data):
    birth_year = input("Enter the birth year to show students born in that year: ")
    found = False
    filtered_students = []
    for student in students_data:
        if student.get_date_of_birth().startswith(birth_year):
            filtered_students.append(student)
            found = True

    if not found:
        print("No students found born in the given year.")
    else:
        headers = ["Student Number", "First Name", "Last Name", "Date of Birth", "Sex", "Country"]
        values = [[] for _ in range(len(headers))]
        for student in filtered_students:
            values[0].append(str(student.get_student_number()))
            values[1].append(student.get_first_name())
            values[2].append(student.get_last_name())
            values[3].append(str(student.get_date_of_birth()))
            values[4].append(student.get_sex())
            values[5].append(student.get_country())

        # Calculate the maximum width for each column
        column_widths = [max(len(header), max(len(value) for value in col)) for header, col in zip(headers, values)]
        
        # Print headers
        for header, width in zip(headers, column_widths):
            print(header.ljust(width + 2), end='')
        print()

        # Print values under each header
        for i in range(len(filtered_students)):
            for value, width in zip(values, column_widths):
                print(value[i].ljust(width + 2), end='') 
            print()


# Modify a student record by student number
def modify_student(students_data):
    student_number = input("Enter student number to modify record: ")
    found = False
    for student in students_data:
        if student.get_student_number() == student_number:
            found = True
            print("Choose field to modify:")
            print("1. First Name")
            print("2. Last Name")
            print("3. Date of Birth")
            print("4. Sex")
            print("5. Country")
            field_choice = input("Enter your choice: ")
            if field_choice == "1":
                new_first_name = input("Enter new first name: ")
                student.set_first_name(new_first_name)
            elif field_choice == "2":
                new_last_name = input("Enter new last name: ")
                student.set_last_name(new_last_name)
            elif field_choice == "3":
                new_date_of_birth = input("Enter new date of birth (YYYY-MM-DD): ")
                student.set_date_of_birth(new_date_of_birth)
            elif field_choice == "4":
                new_sex = input("Enter new sex: ")
                student.set_sex(new_sex)
            elif field_choice == "5":
                new_country = input("Enter new country: ")
                student.set_country(new_country)
            print("Record updated successfully!")
            break
    if not found:
        print("No student found with the given student number.")


# Delete a student with a specific student number
def delete_student(students_data):
    student_number = input("Enter student number to delete record: ")
    found = False
    for student in students_data:
        if student.get_student_number() == student_number:
            found = True
            students_data.remove(student)
            print("Student record deleted successfully!")
            break
    if not found:
        print("No student found with the given student number.")


# Write the contents of the student array to a file callwd students.txt
def write_to_file(students_data, filename):
    try:
        with open(filename, 'w') as f:
            for student in students_data:
                f.write(f"{student.get_student_number()}, {student.get_first_name()}, {student.get_last_name()}, "
                        f"{student.get_date_of_birth()}, {student.get_sex()}, {student.get_country()}\n")
        print("Data written to file successfully!")
    except IOError:
        print("Error writing to file.")


# Read student data from a file and populate the student array
def read_from_file(students_data, filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                data = line.strip().split(", ")
                students_data.append(Student(data[0], data[1], data[2], data[3], data[4], data[5]))
        print("Data read from file successfully!")
    except IOError:
        print("Error reading from file.")


# Calculate age based on date of birth
def calculate_age(date_of_birth):
    import datetime
    today = datetime.date.today()
    birth_date = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Main function to demonstrate functionality using a menu-driven approach
if __name__ == '__main__':
    students_data = []

    while True:
        print("\nSelect an action from the menu below:")
        print("1. Write the contents of the student array to a file")
        print("2. Read student data from a file and populate the student array")
        print("3. Add a new student")
        print("4. Find a student by student number")
        print("5. Show all students")
        print("6. Show all students born in a given year")
        print("7. Modify a student record")
        print("8. Delete a student with a specific student number")
        print("9. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            write_to_file(students_data, "students.txt")
        elif choice == "2":
            read_from_file(students_data, "students.txt")
        elif choice == "3":
            add_student(students_data)
        elif choice == "4":
            find_by_student_number(students_data)
        elif choice == "5":
            show_all_students(students_data)
        elif choice == "6":
            show_students_by_birth_year(students_data)
        elif choice == "7":
            modify_student(students_data)
        elif choice == "8":
            delete_student(students_data)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")

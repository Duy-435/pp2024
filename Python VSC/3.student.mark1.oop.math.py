# student_mark_management.py
# Practical work 3: some maths and decorations
# • Copy your practical work 2 to 3.student.mark.oop.math.py
# • Use math module to round-down student scores to 1-digit
# decimal upon input, floor()
# • Use numpy module and its array to
# • Add function to calculate average GPA for a given student
# • Weighted sum of credits and marks
# • Sort student list by GPA descending
# • Decorate your UI with curses module

import math
import numpy as np

class Student:
    def __init__(self, id, name , dob):
        self.__id = id 
        self.__name = name
        self.__dob = dob
        self.__gpa = 0

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_gpa(self):
        return self.__gpa
    


    def display(self):
        print(f" - Student + Name: {self.__name}")
        print(f"           + ID: {self.__id}")
        print(f"           + DOB: {self.__dob}")

class Course:
    def __init__(self, id, name, credits):
        self.__id = id
        self.__name = name
        self.__credits = credits
        self.__marks = {} # Dict

    def get_name(self):
        return self.__name
    
    def get_mark(self, student_id):
        return self.__marks[student_id]["mark"]

    def get_credits(self):
        return self.__credits
        
    def input_mark(self, student_id, mark):
        self.__marks[student_id] = {"mark": mark}


    def display(self):
        print(f" - Course: + Name: {self.__name}")
        print(f"            + ID: {self.__id}")
        print(f"            + Credits: {self.__credits}")
        

class StudentMarkManagement:
    def __init__(self):
        self.__students = {}
        self.__courses = {}

    def input_student_info(self):
        self.num_students = int(input("\nEnter number of students: "))
        
        for i in range (self.num_students):
            print(f" - Input Student {i+1}:")
            id = input("    + ID: ")
            name = input("    + Name: ")
            dob = input("    + DOB: ")

            student = Student(id, name , dob)
            self.__students[id] = {"student": student}

    def input_course_info(self):
        self.num_courses = int(input("\nEnter number of courses: "))

        for i in range (self.num_courses):
            print(f" - Input Course {i+1} info:")
            id = input("    + ID: ")
            name = input("    + Name: ")
            credits = int(input("    + Credits: "))

            course = Course(id, name, credits)
            self.__courses[id] = {"course": course}

    def input_marks(self):
        course_id = input("\nEnter course ID to input marks: ")
        
        if course_id in self.__courses:
            for i in self.__students:
                mark = math.floor(float(input(f"    + {self.__students[i]["student"].get_id()} - {self.__students[i]["student"].get_name()}: ")))
                self.__courses[course_id]["course"].input_mark(i, mark)
        else:
            print ("Course not found!")

    def list_marks(self):
        course_id = input("\nEnter course ID to view mark: ")

        if course_id in self.__courses:
            for i in self.__students:
                print(f" + {self.__students[i]["student"].get_id()} - {self.__students[i]["student"].get_name()}: {self.__courses[course_id]["course"].get_mark(i)} ")
        else:
            print("Course not found!")

    def list_students(self):
        print("\n *** Student list ***")
        for i in self.__students:
            {self.__students[i]["student"].display()}

    def list_courses(self):
        print("\n *** Course list ***")
        for i in self.__courses:
            print(f"{self.__courses[i]["course"].display()}")

    def calculate_gpa(self):
        self.__gpa_dict = {}
        self.__gpa_list = []

        self.student_gpas = []


        for student_id in self.__students:
            mark_list = []
            credit_list = []

            for course_id in self.__courses:
                mark = self.__courses[course_id]["course"].get_mark(student_id)
                credits = self.__courses[course_id]["course"].get_credits()
                
                mark_list.append(mark)
                credit_list.append(credits)
                
            mark_array = np.array([mark_list])
            credit_array = np.array([credit_list])

            gpa = (np.dot(mark_array,credit_array.T))/(np.sum(credit_array))
            self.__students[student_id]["student"].set_gpa(gpa)

        self.student_gpas.append((student_id, gpa))

    def sort_by_gpa2(self):
        # Sort the dictionary by values (student GPAs)
        sorted_students = sorted(self.__students.items(), key=lambda student: student[1]["student"].get_gpa(), reverse=True)

        # Print sorted students
        print("*** Students Sorted by GPA ***")
        for student_id, student in sorted_students:
            print(f"ID: {student_id}, Name: {self.__students[student_id]["student"].get_name()}, GPA: {self.__students[student_id]["student"].get_gpa()}")

def simple_ui():
    # Simple text-based UI
    print("Welcome to the Student Mark Management System!")
    print("1. Input student information")
    print("2. Input course information")
    print("3. Input marks")
    print("4. List students")
    print("5. List courses")
    print("6. List marks")
    print("7. Calculate GPA")
    print("10. Sort students by GPA 2")
    print("11. Exit")

if __name__ == "__main__":
    mark_management = StudentMarkManagement()

    while True:
        simple_ui()

        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            mark_management.input_student_info()
        elif choice == '2':
            mark_management.input_course_info()
        elif choice == '3':
            mark_management.input_marks()
        elif choice == '4':
            mark_management.list_students()
        elif choice == '5':
            mark_management.list_courses()
        elif choice == '6':
            mark_management.list_marks()
        elif choice == '7':
            mark_management.calculate_gpa()
        elif choice == '8':
            mark_management.sort_students_by_gpa()
        elif choice == '9':
            mark_management.sort_by_gpa()
        elif choice == '10':
            mark_management.sort_by_gpa2()
        elif choice == '11':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice")

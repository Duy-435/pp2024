def input_num_student():
    num_student = int(input("Enter the number of students: "))
    return (num_student)


def input_student_info(num_student):
    students = {}
    for i in range (num_student):
        print(f" - Student #{i+1}:")
        student_id = input("     ID: " )
        student_name = input("     Name: ")
        student_dob = input("     Date of birth: ")

        students[student_id] = {'student_name': student_name, 'student_dob': student_dob }
    return (students)

def input_num_course():
    num_course = int(input("Number of courses: "))
    return (num_course)

def input_course_info(num_course):
    courses = {}
    for i in range(num_course):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")

        courses[course_id] = {'Course name': course_name, 'marks': {}}
    return (courses)


def input_mark(courses, students):
    course_id = input("Enter course ID to input marks: ")
    if course_id in courses:
        print("Enter marks for:")
        for student_id in students:
            mark = float(input(f"    {student_id} - {students[student_id]['student_name']}: "))
            courses[course_id]['marks'][student_id] = mark
        print()
    else:
        print("Course ID not found")
       
'''
def print_mark(students):
    student_id = input("student_id")
    course_id = input(" Course ID")
    print(f"{ students[student_id][course_id] }")
'''

def list_student(students):
    print("Student list:")
    for student_id in students:
        print(f"   {student_id} - {students[student_id]['student_name']} - {students[student_id]['student_dob']}" )




def list_courses(courses):
    print("List of courses:")
    for course_id in courses:
        print(f"    {course_id} - {courses[course_id]['Course name']}")
    print()

#def list_students(students, num_student):
    
def print_course_marks (courses):
    course_id = input("Enter course ID to view marks: ")
    if course_id in courses:
        print(f"Course {course_id} - {courses[course_id]['Course name']} marks: ")
        for student_id in students:
            if course_id in students[student_id]:
                print(f"   {students[student_id]['name']}: {students[student_id][course_id]}")
    else:
        print("Course not found.")

def print_course_marks2 (courses):
    course_id = input("Enter course ID to view marks: ")
    if course_id in courses:
        print(f"Course {course_id} - {courses[course_id]['Course name']} marks: ")
        for course_id in courses:
            print(f"   {courses[course_id]['marks']}")
    else:
        print("Course not found.")
    
''''
def print_student_info(students, courses):
    for student_id, student_info in students.items():
        print(f"Student ID: {student_id}")
        print(f"Name: {student_info['student_name']}")
        print(f"Date of Birth: {student_info['student_dob']}")
        if student_info['marks']:
            print("Marks:")
            for course_id, mark in student_info['marks'].items():
                course_name = courses[course_id]['Course name'] if course_id in courses else "Unknown Course"
                print(f"  {course_name}: {mark}")
        else:
            print("No marks available.")
        print()
'''

# Main
num_student = input_num_student()
students = input_student_info(num_student)
list_student(students)
num_courses = input_num_course()
courses = input_course_info(num_courses)
input_mark(courses, students)
#print_student_info(students, courses)
list_courses(courses)
print_course_marks2(courses)
# Example usage of listing functions




 
class Person:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id

    def __str__(self):
        print (f" - Name: {self.__name}\n   + ID: {self.__id}")

    def input_person_info(self):
        name = input("Enter name: ")
        id = input("Enter ID: ")
        person = Person(name, id)

class Student(Person):
    def __init__(self, name, id, dob):
        super().__init__(name, id)
        self.__dob = dob

    def __str__(self):
        super().__str__()
        print(f"   + DOB: {self.__dob}")

    def input_person_info(self):
        name = input("Enter name: ")
        id = input("Enter ID: ")
        dob = input
        self.person = Person(name, id, dob)


class Course:
    def __init__(self, name , id):
        self.__name = name
        self.__id = id

    def __str__(self):
        print(f" - Course name: {self.__name}\n   + ID: {self.__id}")

class StudentManagementMarkSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def input_num_students(self):
        self.num_students = int(input("Enter number of students: "))


    def input_student_info(self):
        for i in range (self.num_students):
            print(f" - Student #{i+1}:")
            student_id = input("   + ID: ")
            student_name = input("   + Name: ")
            student_dob = input("   + DOB: ")

            student = Student.input_person_info()

            self.students[student.get_id()] = [student]

    def input_num_course(self):
        self.num_course = int(input("Number of courses: "))

    def input_course_info(self):
        for i in range (self.num_course):
            print(f" - Course #{i+1}:")
            course_id = input("   + ID: ")
            course_name = input("   + Name: ")
            marks = {}

            course = Course(course_id, course_name, marks)

            self.courses[course_id] = {'course name': course_name, 'marks' : marks}

    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        if course_id in self.courses:
            print(f"Input marks for course {self.courses[course_id]['course name']}:")
            for i in self.students: # i is student ID
                mark = float(input(f"   + {i} - {self.students[i]['student name']}: "))
                self.courses[course_id]['marks'][i]  = mark
        else:
            print("Course not found!")

    def list_student(self):
        print("Student list:")
        for i in self.students:
            print(f" - Student:\n   + Name: {self.students[i]['student name']}\n   + ID: {i}")

    def list_course(self):
        print("Course list:")
        for i in self.courses:
            print(f" - Course:\n   + Name: {self.courses[i]['course name']}\n   + ID: {i}")

    def list_marks(self):
        course_id = input("Enter course id to view marks: ")
        if course_id in self.courses:
            print(f" - {self.courses[course_id]['course name']} - {course_id} mark list:")
            for i in self.students:
                print(f" -{i} - {self.students[i]['student name']}: {self.courses[course_id]['marks'][i]}")
        else:
            print("Course not found!")

# Main

# tom = Student("Tommy Tom", "22bi1324", "13/43/5423")
# print(tom)

system = StudentManagementMarkSystem()
system.input_num_students()
system.input_student_info()
system.list_student()

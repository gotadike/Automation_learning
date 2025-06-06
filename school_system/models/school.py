from .student import Student
from .teacher import Teacher
from .course import Course

class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.__students = {}
        self.__teachers = {}
        self.__courses = {}

    def add_student(self, id, name, age, grade):
        new_student = Student(id, name, age, grade)
        self.__students[id] = new_student
        print("Student added successfully")
        return new_student

    def add_teacher(self, id, name, age, subject):
        new_teacher = Teacher(id, name, age, subject)
        self.__teachers[id] = new_teacher
        print("Teacher added successfully")
        return new_teacher

    def add_course(self, code, name, credits):
        new_course = Course(code, name, credits)
        self.__courses[code] = new_course
        print("Course added successfully")
        return new_course

    def get_student(self, id):
        if id not in self.__students:
            print("Student ID not found")
            return None
        student = self.__students[id]
        print(f"\nID: {student.id}\nName: {student.name}\nGrade: {student.grade}")
        return student

    def get_teacher(self, id):
        if id not in self.__teachers:
            print("Teacher ID not found")
            return None
        teacher = self.__teachers[id]
        print(f"\nID: {teacher.id}\nName: {teacher.name}\nSubject: {teacher.subject}")
        return teacher 
class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, id, name, age, grade):
        super().__init__(id, name, age)
        self.grade = grade
        self._marks = {}
        self._attendance = 0

    def add_marks(self, subject, marks):
        self._marks[subject] = marks
        print(f"Marks added for {subject}: {marks}")

    def get_marks(self):
        for subject, marks in self._marks.items():
            print(f"{subject}: {marks}")

    def update_attendance(self, days):
        self._attendance += days
        print(f"Attendance updated. Total days present: {self._attendance}")


class Teacher(Person):
    def __init__(self, id, name, age, subject):
        super().__init__(id, name, age)
        self.subject = subject
        self._classes = []

    def assign_class(self, grade):
        self._classes.append(grade)
        print(f"Teacher assigned to grade {grade}")

    def get_assigned_classes(self):
        print(f"Classes assigned to {self.name}: {self._classes}")


class Course:
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = credits
        self._enrolled_students = []

    def enroll_student(self, student):
        self._enrolled_students.append(student)
        print(f"Student {student.name} enrolled in {self.name}")

    def get_enrolled_students(self):
        print(f"\nStudents enrolled in {self.name}:")
        for student in self._enrolled_students:
            print(f"ID: {student.id}, Name: {student.name}")


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


# Example usage
school = School("ABC School", "Bengaluru")

# Adding students
s1 = school.add_student("S001", "John Doe", 15, "10th")
s2 = school.add_student("S002", "Jane Smith", 14, "9th")

# Adding teachers
t1 = school.add_teacher("T001", "Mr. Anderson", 35, "Mathematics")
t2 = school.add_teacher("T002", "Mrs. Wilson", 40, "Science")

# Adding courses
c1 = school.add_course("MATH101", "Advanced Mathematics", 4)
c2 = school.add_course("SCI101", "General Science", 4)

# Demonstrating functionality
s1.add_marks("Mathematics", 85)
s1.add_marks("Science", 90)
s1.update_attendance(5)
s1.get_marks()

t1.assign_class("10th")
t1.assign_class("9th")
t1.get_assigned_classes()

c1.enroll_student(s1)
c1.enroll_student(s2)
c1.get_enrolled_students()

# Getting information
school.get_student("S001")
school.get_teacher("T001") 
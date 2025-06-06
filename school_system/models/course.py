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
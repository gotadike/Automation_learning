from .person import Person

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
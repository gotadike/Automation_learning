from .person import Person

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
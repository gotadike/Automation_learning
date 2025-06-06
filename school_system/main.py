from models import School

def main():
    # Create a new school
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

if __name__ == "__main__":
    main() 
# Association: two way to many relationship

class Student:

    all = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # teacher is protected because it is not a part of the constructor
        self._teacher = None
        Student.all.append(self)

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError("Teacher must be an instance of Teacher class")
        self._teacher = value

class Teacher:
    def __init__(self, name):
        self.name = name

    def students(self):
        return [student for student in Student.all if student.teacher == self]

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student class")
        student.teacher = self



# Initialize the Teacher class
teacher1 = Teacher("Mr. Smith")
teacher2 = Teacher("Ms. Johnson")

# Initialize the Student class and add students
student1 = Student("Alice", 15)
student2 = Student("Bob", 16)
student3 = Student("Charlie", 15)

# Assign students to teachers
teacher1.add_student(student1)
teacher1.add_student(student2)
teacher2.add_student(student3)

# Output the teacher's students
print(f"{teacher1.name}'s students: {[student.name for student in teacher1.students()]}")
print(f"{teacher2.name}'s students: {[student.name for student in teacher2.students()]}")



teacher = Teacher("monalisa")
# Create a non-student object (e.g., a string)
not_a_student = "Not a student"

# Attempt to add the non-student object to the teacher's students
teacher.add_student(not_a_student)  # This will raise a TypeError
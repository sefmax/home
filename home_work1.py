class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, surname, age, student_id):
        super().__init__(name, surname, age)
        self.student_id = student_id

    def get_info(self):
        return f"Student: {self.name} {self.surname}, Age: {self.age}, ID: {self.student_id}"

    def __str__(self):
        return self.get_info()


class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    def find_student_by_surname(self, surname):
        for student in self.students:
            if student.surname == surname:
                return student
        return None

    def remove_student_by_surname(self, surname):
        student = self.find_student_by_surname(surname)
        if student:
            self.students.remove(student)

    def __str__(self):
        if not self.students:
            return "The group is empty."
        return "\n".join(str(student) for student in self.students)


# Example usage:
if __name__ == "__main__":
    student1 = Student("John", "Smith", 20, "S001")
    student2 = Student("Emily", "Johnson", 21, "S002")

    group = Group()
    group.add_student(student1)
    group.add_student(student2)

    print("Group after adding students:")
    print(group)

    print("\nSearching for student with surname 'Smith':")
    found = group.find_student_by_surname("Smith")
    print(found.get_info() if found else "Student not found.")

    group.remove_student_by_surname("Smith")
    print("\nGroup after removing student with surname 'Smith':")
    print(group)
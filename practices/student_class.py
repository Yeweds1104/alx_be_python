class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def student_description(self):
        print(f"Student Name: {self.name}")
        print(f"Student Age: {self.age}")

student1 = Student('Yeweds Dagne', 30)
student2 = Student('Rediet Zelalem', 25)

student1.student_description()
student2.student_description()
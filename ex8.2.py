class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def say_hi(self):
        print('I am a student, my name is', self.name)


s1 = Student('王子', 21, 3)
s1. say_hi()
print(s1. grade)
s2 = Student('公主', 20, 2)
s2. say_hi()
print(s2. grade)

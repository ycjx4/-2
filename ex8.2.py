class Student:  # 定义学生类
    def __init__(self, name, age, grade):  # 构造方法，初始化学生属性
        self.name = name  # 姓名
        self.age = age  # 年龄
        self.grade = grade  # 年级

    def say_hi(self):  # 定义打招呼方法
        print('I am a student, my name is', self.name)


s1 = Student('王子', 21, 3)  # 创建学生对象s1
s1. say_hi()  # 调用say_hi方法
print(s1. grade)  # 输出年级
s2 = Student('公主', 20, 2)  # 创建学生对象s2
s2. say_hi()  # 调用say_hi方法
print(s2. grade)  # 输出年级

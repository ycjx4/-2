#例8.11面向对象之继承
class Person (object):  # 定义父类Person
    def __init__(self, name, gender):  # 构造方法
        self.name= name  # 姓名属性
        self.gender= gender  # 性别属性
        print(" Person类__ini()__。","姓名：",self.name)
class Student(Person):  # 定义子类Student，继承Person
    def __init__ (self, name, gender, score):  # 构造方法
        super (Student,self).__init__ (name, gender)  # 调用父类构造方法
        self.score= score  # 分数属性
        print(" Student类__ini__()。","姓名：",self.name)
if __name__=="__main__":
    person= Person("张三","男")  # 创建Person对象
    student= Student("李四","男",100)  # 创建Student对象

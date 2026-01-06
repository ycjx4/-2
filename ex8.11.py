#例8.11面向对象之继承
class Person (object):
    def __init__(self, name, gender):
        self.name= name
        self.gender= gender
        print(" Person类__ini()__。","姓名：",self.name)
class Student(Person):
    def __init__ (self, name, gender, score):
        super (Student,self).__init__ (name, gender)
        self.score= score
        print(" Student类__ini__()。","姓名：",self.name)
if __name__=="__main__":
    person= Person("张三","男")
    student= Student("李四","男",100)

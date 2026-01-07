class Person:  # 定义人类
    def __init__(self,name):  # 构造方法
        self.PersonName=name  # 初始化姓名属性
    def sayHi(self):  # 定义打招呼方法
        print('大家好，我是{}。'.format(self.PersonName))
p=Person('王子')  # 创建实例对象
p.sayHi()  # 调用方法

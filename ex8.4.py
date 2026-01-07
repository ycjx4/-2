class Person:  # 定义人类
    place = 'Changsha'  # 类属性

    @classmethod  # 类方法，用@classmethod来进行修饰
    def getPlace(cls):  # 类方法
        return cls.place  # 返回类属性


p = Person()  # 创建实例对象
print(p.getPlace())  # 通过实例对象调用
print(Person.getPlace())  # 通过类对象调用

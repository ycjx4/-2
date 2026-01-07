class Person:  # 定义人类
    place='Changsha'  # 类属性
    @staticmethod  # 静态方法装饰器
    def getPlace():  # 静态方法
        return Person.place  # 返回类属性
print(Person.getPlace())  # 调用静态方法

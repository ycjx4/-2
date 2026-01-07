class Person:  # 定义人类
    place='Changsha'  # 类属性
    @classmethod  # 类方法装饰器
    def getPlace(cls):  # 获取地点
        return cls.place  # 返回类属性place
    @classmethod  # 类方法装饰器
    def setPlace(cls,place1):  # 设置地点
        cls.place=place1  # 修改类属性
p=Person()  # 创建实例对象
p.setPlace('Shanghai')  # 修改类属性
print(p.getPlace())  # 输出修改后的类属性
print(Person.getPlace())  # 通过类对象输出

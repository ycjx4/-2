class Person:  # 定义人类
    place = 'Changsha'  # 类属性

    def getPlace(self):  # 实例方法
        return self.place  # 返回地点


p = Person()  # 创建实例对象
print(p.getPlace())  # 通过实例对象调用方法


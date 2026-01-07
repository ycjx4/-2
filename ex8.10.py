class Person:  # 定义人类
    __name='公主'  # 私有属性：姓名
    __age=16  # 私有属性：年龄
    def getName(self):  # 获取姓名的方法
        return self.__name  # 返回私有属性
    def getAge(self):  # 获取年龄的方法
        return self.__age  # 返回私有属性
p=Person()  # 创建实例对象
print(p.getName(),p.getAge())  # 通过方法访问私有属性

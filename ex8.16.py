#例8.16私有方法并不会被覆盖的封装示例
class A:  # 父类A
    def __fm(self):  # 私有方法
        print("from A")
    def test(self):  # 定义test方法
        self.__fm()  # 调用私有方法
class B(A):  # 子类B继承A
    def __fm(self):  # 子类的私有方法
        print("from B")
b = B()  # 创建B的实例
b.test()  # 调用test方法，输出"from A"

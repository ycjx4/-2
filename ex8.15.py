#例8.15封装性示例
class A:  # 父类A
    def fm(self):  # 定义方法fm
        print("from A")
    def test(self):  # 定义test方法
        self.fm()  # 调用fm方法
class B(A):  # 子类B继承A
    def fm(self):  # 重写fm方法
        print("from B")
b=B()  # 创建B的实例
b.test()  # 调用test方法，输出"from B"

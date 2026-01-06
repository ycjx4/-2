#例8.16私有方法并不会被覆盖的封装示例
class A:
    def __fm(self):
        print("from A")
    def test(self):
        self.__fm()
class B(A):
    def __fm(self):
        print("from B")
b = B()
b.test()

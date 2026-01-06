#例8.15封装性示例
class A:
    def fm(self):
        print("from A")
    def test(self):
        self.fm()
class B(A):
    def fm(self):
        print("from B")
b=B()
b.test()

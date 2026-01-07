#例8.12面向对象之多重继承
class P1():  # 父类P1
    def foo(self):  # 定义方法foo
        print("pl-foo")
class P2():  # 父类P2
    def foo(self):  # 定义方法foo
        print("p2-foo")
    def bar(self):  # 定义方法bar
        print("p2-bar")
class C1(P1,P2):  # C1继承P1和P2
    pass
class C2(P1,P2):  # C2继承P1和P2
    def bar(self):  # 重写bar方法
        print ("C2-bar")
class D(C1,C2):  # D继承C1和C2
    pass
if __name__=='__main__':
    d=D()  # 创建D的实例
    d.foo()  # 调用foo方法
    d.bar()  # 调用bar方法

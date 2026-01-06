class Test:
    def __init__(self):
        print('构造方法')
    def __del__(self):
        print('析构方法')
    def myf(self):
        print('调用自定义方法')
obj=Test()
obj.myf()
del obj

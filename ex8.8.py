class Test:  # 定义测试类
    def __init__(self):  # 构造方法
        print('构造方法')
    def __del__(self):  # 析构方法
        print('析构方法')
    def myf(self):  # 自定义方法
        print('调用自定义方法')
obj=Test()  # 创建对象，调用构造方法
obj.myf()  # 调用自定义方法
del obj  # 删除对象，调用析构方法

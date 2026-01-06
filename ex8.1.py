class CC:
    x = 10              # 定义属性
    y = 20              # 定义属性
    z = 30              # 定义属性

    def show(self):        # 定义方法
        print((self.x+self.y+self.z)/3)


b = CC()       # 创建实例对象b
b.x = 30       # 调用属性x
b.show()     # 调用方法show


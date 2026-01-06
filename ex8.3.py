class Person:
    place = 'Changsha'

    def getPlace(self):       # 实例方法
        return self.place


p = Person()
print(p.getPlace())         # 正确，可以用过实例对象引用


class Person:
    place = 'Changsha'

    @classmethod       # 类方法，用@classmethod来进行修饰
    def getPlace(cls):
        return cls.place


p = Person()
print(p.getPlace())         # 可以用过实例对象引用
print(Person.getPlace())    # 可以通过类对象引用

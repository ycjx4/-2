class Person:
    place='Changsha'
    @classmethod
    def getPlace(cls):
        return cls.place
    @classmethod
    def setPlace(cls,place1):
        cls.place=place1
p=Person()
p.setPlace('Shanghai')       #修改类属性
print(p.getPlace())
print(Person.getPlace())

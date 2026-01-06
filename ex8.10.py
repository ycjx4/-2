class Person:
    __name='公主'
    __age=16
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
p=Person()
print(p.getName(),p.getAge())

class Person:
    place='Changsha'
    @staticmethod
    def getPlace():         #静态方法
        return Person.place
print(Person.getPlace())

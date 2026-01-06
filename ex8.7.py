class Person:
    def __init__(self,name):
        self.PersonName=name
    def sayHi(self):
        print('大家好，我是{}。'.format(self.PersonName))
p=Person('王子')
p.sayHi()

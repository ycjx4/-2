#例8.14使用多态的面向对象程序实现
class Dog (object):
    def work(self):
        pass
class ArmyDog(Dog):
    def work(self):
        print("追击敌人。")
class DrugDog(Dog):
    def work(self):
        print("追查毒品。")
class Person (object):
    def work_with_dog(self, dog):
        dog.work()
person= Person()
person.work_with_dog(ArmyDog())
person.work_with_dog(DrugDog())

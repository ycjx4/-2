#例8.14使用多态的面向对象程序实现
class Dog (object):  # 狗的基类
    def work(self):  # 工作方法
        pass
class ArmyDog(Dog):  # 军犬类，继承Dog
    def work(self):  # 重写work方法
        print("追击敌人。")
class DrugDog(Dog):  # 缉毒犬类，继承Dog
    def work(self):  # 重写work方法
        print("追查毒品。")
class Person (object):  # 人类
    def work_with_dog(self, dog):  # 与狗工作，体现多态
        dog.work()  # 调用狗的work方法
person= Person()  # 创建人对象
person.work_with_dog(ArmyDog())  # 与军犬工作
person.work_with_dog(DrugDog())  # 与缉毒犬工作

#例8.13不使用多态的面向对象程序实现
class ArmyDog (object):
    def bite_enemy (self):
        print("追击敌人。")
class DrugDog(object):
    def track_drug(self):
        print("追查毒品。")
class Person (object):
    def work_with_army(self, dog):
        dog.bite_enemy()
    def work_with_drug (self, dog):
        dog.track_drug()
person=Person ()
person.work_with_army(ArmyDog())
person.work_with_drug(DrugDog())

#例8.13不使用多态的面向对象程序实现
class ArmyDog (object):  # 军犬类
    def bite_enemy (self):  # 咬敌人的方法
        print("追击敌人。")
class DrugDog(object):  # 缉毒犬类
    def track_drug(self):  # 追查毒品的方法
        print("追查毒品。")
class Person (object):  # 人类
    def work_with_army(self, dog):  # 与军犬工作
        dog.bite_enemy()  # 调用军犬方法
    def work_with_drug (self, dog):  # 与缉毒犬工作
        dog.track_drug()  # 调用缉毒犬方法
person=Person ()  # 创建人对象
person.work_with_army(ArmyDog())  # 与军犬工作
person.work_with_drug(DrugDog())  # 与缉毒犬工作

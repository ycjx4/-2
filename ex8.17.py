class Animal:  # 动物基类，封装共同属性和方法
    # 所用的知识 Animal类的封装 -> Dog类，Cat类，Person类的继承->多态
    # 把所有的共同属性和方法封装在一个公有类里面让子类继承父类的方法来实现和数据
    # 在创建一个小狗实例的时候，给它设置几个属性
    def __init__(self, name, age=1):  # 构造方法
        self.name = name  # 姓名属性
        self.age = age  # 年龄属性
    def eat(self):  # 吃饭方法
        # print("名字是%s，年龄%d岁的小狗在吃饭"%(self.name,self.age))
        print("%s吃饭"%self)
        return self  # 返回自身，支持链式调用
    def play(self):  # 玩耍方法
        print("%s玩"%self)
        return self  # 返回自身，支持链式调用
    def sleep(self):  # 睡觉方法
        print("%s睡觉"%self)
        return self  # 返回自身，支持链式调用
class Dog(Animal):  # 狗类，继承Animal
    def work(self):  # 狗的工作方法
        print("%s看家"%self)
    def __str__(self):  # 字符串表示方法
        # self对象本身对字符串的一个描述
        return "名字是{}，年龄{}岁的小狗在".format(self.name,self.age)
class Cat(Animal):  # 猫类，继承Animal
    def work(self):  # 猫的工作方法
        print("%s捉老鼠"%self)
    def __str__(self):  # 字符串表示方法
        # self对象本身对字符串的一个描述
        return "名字是{}，年龄{}岁的小猫在".format(self.name, self.age)
class Person(Animal):  # 人类，继承Animal
    def __init__(self, name, pets, age=1):  # 构造方法
        super(Person,self).__init__(name,age)  # 调用父类构造方法
        self.pets = pets  # 宠物列表
    def feed_pets(self):  # 喂养宠物方法
        # 所用的知识就是多态，养宠物，和让宠物工作也都是多态
        for pet in self.pets:  # 遍历宠物列表
            pet.eat()  # 调用宠物的eat方法
            pet.sleep()  # 调用宠物的sleep方法
            pet.play()  # 调用宠物的play方法
    def make_pets_work(self):  # 让宠物工作方法
        for pet in self.pets:  # 遍历宠物列表
            pet.work()  # 调用宠物的work方法
    def __str__(self):  # 字符串表示方法
        # self对象本身对字符串的一个描述
        return "名字是{}，年龄{}岁的人在".format(self.name, self.age)
# d = Dog("小黑",18)
# c = Cat("小红",2)
# p = Person("BruceLong", [d, c], 24 )
# print(p.__dict__)
d = Dog("小黑",18)  # 创建狗对象
# selr中谁调用就是谁 此处d 会去Animal中找到self和里的的属性和方法而Animal里的self就是Dog类
c = Cat("小红",2)  # 创建猫对象
p = Person("BruceLong", [d, c], 24 )  # 创建人对象，拥有两个宠物
p.feed_pets()  # 喂养宠物
p.make_pets_work()  # 让宠物工作

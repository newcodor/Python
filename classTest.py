#!/usr/bin/python
# _*_ coding:utf-8 _*_
"""
Author: newcodor
Time: 2019-1-16
Description: Python 面向对象研究
"""

#父类
class Animal(object):
    #类公共变量
    area="UK"
    #私有变量
    __sex="man"
    #类的构造方法
    def  __init__(self,name,specils):
        self.name=name
        self.specils=specils
        pass

    def printInfo(self):
        print(self.name+"\t"+self.specils)
        pass
    #打印类的属性
    def printClassAttrInfos(self):
        print(Animal.__dict__)
        pass
    #属性get方法
    def get_sex(self):
        return self.__sex

    #属性set方法
    def set_sex(self,sex):
        self.__sex=sex
    #打印类，类似于Java中的toString()方法
    def __str__(self):
        return Animal.__name__+":name="+self.name+",specils="+self.specils



#子类
#Python 可以实现多重继承，可同时继承多个父类，如class Cat(Animal,pet)
class Cat(Animal):
    #子类构造方法
    def  __init__(self,name,specils,hostman):
        # 调用父类构造方法
        Animal.__init__(self,name,specils)
        #或者
        # super(Cat,self).__init__(name,specils)
        self.hostman=hostman
    #重写父类方法,实现多态
    def printInfo(self):
        # super(Cat,self).printInfo(),
        Animal.printInfo(self),
        print(self.name+"\t"+self.specils),
        print(self.hostman)
    #析构函数，默认可不写
    # def __del__(self):
    #     Animal.__del__(self)
    #     pass
def main():
    dog = Animal("dog1","犬科")
    cat = Animal("cat1","猫科")
    #给实例绑定属性,但类没有
    cat.age=15
    #cat有age属性
    cat.printInfo()
    #dog 没有age属性
    dog.printInfo()

    cat2 = Cat("cat2","猫科","Ana")
    print("cat age:"+str(cat.age))
    
    #类的类变量
    print(dog.area)
    #只修改了实现的变量,未修改类变量
    dog.area="11"
    print(dog.area) # 11
    print(cat.area) # UK 说明未修改类变量
    #修改类变量
    Animal.area="11"
    print(cat.area) # 11  说明类变量修改成功

    #公有方法访问类的私有变量
    print(dog.get_sex())
    #公有方法修改类的私有变量
    dog.set_sex("women")

    #虽然私有变量也可以直接在类外访问,但不建议这么做
    print(dog._Animal__sex)

    #判断是否属于某类型
    print(isinstance(1,(int,float)))
    
    #重写父类方法
    cat2.printInfo()
    
    #打印对象,类似toString()
    print(cat2)
    # cat2.printInfo()

    pass

if __name__ == '__main__':
    main()
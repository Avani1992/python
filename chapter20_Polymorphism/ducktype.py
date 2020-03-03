# 1. Method name same for all class....
# class Duck:
#     def talk(self):
#         print('Quack.. Quack..')
#
# class Dog:
#     def talk(self):
#         print('Bow Bow..')
#
# class Cat:
#     def talk(self):
#         print('Moew Moew ..')
#
# class Goat:
#     def talk(self):
#         print('Myaah Myaah ..')
#
# def f1(obj):
#      obj.talk()
#
# #1.
# l=[Duck(),Cat(),Dog(),Goat()]
# for obj in l:
#      f1(obj)

#2.
# l=Duck()
# l.talk()
# l1=Dog()
# l1.talk()
# l2=Cat()
# l2.talk()

#2.Method name different for all class....hasattr(obj,methodname)

class Duck:
    def talk(self):
        print('Quack.. Quack..')

class Dog:
    def bark(self):
        print('Bow Bow..')

class Cat:
    def sound(self):
        print('Moew Moew ..')

def f1(obj):
    if hasattr(obj,'bark'):
        obj.bark()
    elif hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'sound'):
        obj.sound()


l=[Dog(),Cat(),Duck()]

for obj in l:
    f1(obj)
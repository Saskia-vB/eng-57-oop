# OOP Intro Exercise - Create class Cat

from animal_class import *


# to inherit pass the entire parent class to your subclass
class Cat(Animal):
    'nothing'
    def purr(self, frequency=(random.randint(25,150))):
        return f'PuurrrUUUUURRRrrrrUURRrrr and a steady {frequency}'

# gafield= Cat()
# print(garfield)
#
# print(garfield.cat('Lasanhaaa'))
# print(garfield.sleep())
# print(garfield.potty())




## Acceptance Criteria:

# ### create class Cat
# class Cat():
#
#     # init method has at least five attributes and at least two cat specific attributes
#     def __init__(self, name = 'Hiccup'):
#         self.name = name
#         self.age = 8
#         self.age_in_human_years = 48 # cat specific attribute
#         self.fur = 'luxurious black'
#         self.food = 'chicken' # cat specific attribute
#
#     # Cat class has at least five methods with two methods that DO exist in Dog and 2 methods that DO NOT exist in Dog
#     def miaow(self): # NOT in Dog
#         return 'miaow, miaow'
#
#     # one method takes in arguments and Polymorphs
#
#     def hiss(self, annoying_human = ' '): # NOT in Dog
#         print('hiss at ' + annoying_human)
#
#     def eat(self, food): # IN Dog
#         return 'Nom, nom, nom, nom' + food.lower()
#
#     def sleep(self): # IN Dog
#         return 'zzZZZzzZzz ZZzzZZzz'
#
#     def play(self): # NOT in Dog
#         return "chasing shadows"
#
#     def purr(self): # NOT in Dog
#         return "purrrrrrrrrrrrrrrr"

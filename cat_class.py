# Abstract and create the class cat

# In this file you define the class cat and add attributes and methods to the class

class Cat():

    # self refers to the instance of the object
    def __init__(self, name = 'Hiccup'):
        self.name = name
        self.age = 8
        self.age_in_human_years = 48
        self.fur = 'luxurious black'
        self.food = 'chicken'

    # this is a method that can be used by a Cat instance
    def miaow(self):
        return 'miaow, miaow'

    def hiss(self, person = ' ')):
        print('hiss at ' + person)

    def eat(self, food):
        return 'Nom, nom, nom, nom' + food.lower()

    def sleep(self):
        return 'zzZZZzzZzz ZZzzZZzz'

    def play(self):
        return "chasing shadows"

    def purr(self):
        return "purrrrrrrrrrrrrrrr"

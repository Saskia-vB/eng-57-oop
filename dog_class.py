# Abstract and create the class dog

# In this file you define the class dog and add attributes and methods to the class

class Dog():

    # this is a special method
    # it come defined either way but we can rewrite it
    # this method stands for initialise class object AKA the constructor in other languages
    # allows us to set attribute to out Dog objects
        #...Like.. the poor thing doesn't even have a name :(
            # we should giv it a name... possibly Max :)
    # self refers to the instance of the object
    def __init__(self, name = 'Mad Max'):
        self.name = name
        self.age = 17
        self.paws = 4
        self.fur = 'luxurious black and grey'

    # this is a method that can be used by a Dog instance
    def bark(self, person = ' '):
        return 'woof, woof! I see you there ' + person

    def bark_print(self):
        print('woof, woof!')

    def eat(self, food):
        return 'Nom, nom, nom, nom' + food.lower()

    def sleep(self):
        return 'zzZZZzzZzz ZZzzZZzz'

    def fetch(self):
        return "WHERE THAT BALL AT? -- Imma get that ball!!"

    def potty(self):
        return "UHHHH!!! AHHH!! 0_o UHHH!! .... O_O"




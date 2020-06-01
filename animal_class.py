class Animal():

    def __init__(self, species_argument, limbs):
        self.species_parameter = species_argument
        self.limbs = limbs


    def eat(self, food):
        return 'Nom, nom, nom, nom '+ food.lower()

    def sleep(self):
        return 'zzZZZZzzzZZZ ZZZzzzZZZz'

    def potty(self):
        return "UHHHH!!! AHHHHH!! UUUHHHHH"

    def reproduce(self, partner='... sorry you are alone at the moment'):
        return f"offspring of {self} and {partner}"


# create animal instance
# animal_1 = Animal()
#
# print(animal_1)
# print(animal_1.eat('KFC'))
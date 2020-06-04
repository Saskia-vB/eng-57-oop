# Abstract and create the class dog


from animal_class import *

class Dog(Animal):

    # this is a special method
    # it come defined either way but we can rewrite it
    # this method stands for initialise class object AKA the constructor in other languages
    # allows us to set attribute to out Dog objects
        #...Like.. the poor thing doesn't even have a name :(
            # we should giv it a name... possibly Max :)
    # self refers to the instance of the object

    # refers to the instance of the object
    def __init__(self, name='Mad Max', age = 0):
        super().__init__('British bulldog', 'omnivore')
        # setting attribute name to instances of Dog class
        self.__name = name
        # encapsulate age and make it private
        self.__age_dog = age
        self.__human_age = 0
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

    def getter_age(self):
        return self.__age_dog

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name
        return True

    def __increase_dog__and_human_years(self):
        self.__human_age += 1
        # update dog years
        self.__age_dog += 7

    def dog_birthday_incrementer(self):
        # complex block
        #  celebrate the dog's bithday
        print(f'happy birthday! You are a GOOD BOY! GOOD BOY {self.__name}!')
        # update human year
        # update dog years
        self.__increase_dog__and_human_years()
        return f'dog years at {self.__age_dog} and human years {self.__human_age}'


# Encapsulation example
ringo = Dog(name='Ringo')



# print(ringo.name)
print(ringo.get_name())
# print(ringo.age) # age no longer accessible
# print(ringo.__age) # age no longer accessible because it's encapsulated/or private

print(ringo.getter_age())
ringo.dog_birthday_incrementer()
print(ringo.getter_age())
ringo.dog_birthday_incrementer()
print(ringo.getter_age())
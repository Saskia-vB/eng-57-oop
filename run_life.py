# import classes here and initialize objects and run methods
# this separation will maintain your code more organised following separation of concernces

from dog_class import *

# Initializing a Dog object
dog_instance1 = Dog()
max_dog_instance = Dog()
ringo_dog_instance = Dog('Ringo')
#
# from cat_class import *
# # initialize a Cat object
# garfield = Cat(name='Garfield the lasagna monster')

print(max_dog_instance.name)
print(ringo_dog_instance.name)
# Call the method .bark() on method


# print the Dog object
print(dog_instance1)
print(type(dog_instance1))

print(max_dog_instance.bark())
print(max_dog_instance.eat(' BONE'))
print(max_dog_instance.fetch())
print(max_dog_instance.potty())
print(max_dog_instance.bark())
print(max_dog_instance.sleep())

print('walk the dog home')

print(max_dog_instance.sleep())
print(max_dog_instance.sleep())
print(max_dog_instance.bark("creepy stranger"))


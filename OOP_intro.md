# Intro to OOP

What is OOP?
- Object Oriented Programming
- a programming paradigm which provides a means of structuring programs so that properties and behaviors are bundled into individual objects.
- an object could represent a person with a name property, age, address, etc., with behaviors like walking, talking, breathing, and running. Or an email with properties like recipient list, subject, body, etc., and behaviors like adding attachments and sending.

Why OOP?
- object-oriented programming is an approach for modeling concrete, real-world things like cars as well as relations between things like companies and employees, students and teachers, etc. OOP models real-world entities as software objects, which have some data associated with them and can perform certain functions.


### Class
What is a class? A class is like a cookie cutter. The cookie cutter is not the cookie. It's a blueprint for objects but not the object itself. 
- focusing on the data, each thing or object is an instance of some class. 

What can you do with a cookie? 
    - eat it!

### Methods
The actions or how an object behaves. 

So in the above example, .eat_cookie() could be a method inside the class Cookie.

### Instance
- while the class is the blueprint, an instance is a copy of the class with actual values, literally an object belonging to a specific class. 
- occurence
- is the cookie
- class is like a form or questionnaire, it defines the needed information but 

### Syntax
```python

class Dog():

    def __init__(self, attr1, attr2, optional_attri='default'):
        self.attribute_1= attri1, 
        self.attribute_2= attri2,
        self.attribute_3= optional_attri,

    def method_name(self, arg1):
        #complex block
        arg1 += arg1 + 1
        return arg1


```


### convention
- to be completed
- capitals are for classes

## 4 Pillars

### Inheritance
The ability of subclass to inherit all the behaviour and method from parent class. 
One of the core reasons to use OOP, because it means you write less code. In reality this is debatable, as you end up having to adapt a lot of methods.It also depends how good of a coder you are and your ability to abstract effectively. 

### Abstraction
- good naming
- good documentation - mention what methods and how to use them
- use of inheritance

### Polymorphism
- what is class polymorphism?
- what is method polymorphism?
1. completely override parent methods by just redefining them in the subclass
2. completely override parent methods by just redefining them in the subclass **AND use super() to call parent class and parent method** - keep previous functionality and you add new functionality

### Encapsulation
- the ability to limit access from the exterior to methods and/or attributes. 
Hence, making them 'private'.
```python

class Dog():

    def __init__(self, dog_name, attri2):
        self.name = attri1,
        self.attribute_2 = attri2,
        self.dog_years = 0,
        self.human_years = 0

    def dog_birthday_incrementer(self):
        # complex block
        #  celebrate the dog's bithday 
        # update human year
        # update dog years
        print(f'happy birthday! You are a GOOD BOY! GOOD BOY {self.name}!')
        return self.dog_years 

```






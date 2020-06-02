# create a parent class called Monster

class Monster():

# define monster characteristics with __init__
    def __init__(self, name, tax_number, fur):
        self.name = name
        self.__tax_number = tax_number
        self.fur = fur


# ask for input so that administrative user can create a student monster
    def get_name(self, name):
        self.name= print(input("Please enter your name:"))
        return name

    def get_tax_number(self, tax_number):
       self.__tax_number= print(input("Please enter your tax number:"))
       return tax_number

    def get_fur(self, fur):
        self.fur = print(input("Please describe your fur:"))
        return fur



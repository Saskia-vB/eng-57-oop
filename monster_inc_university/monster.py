# create a parent class called Monster

class Monster():

# define monster characteristics with __init__
    def __init__(self, name, tax_number, fur):
        self.__name = name
        self.__tax_number = tax_number
        self.fur = fur


# ask for input so that administrative user can create a student monster
    def set_name(self, name):
        self.__name = name
        return "name set to: " + self.__name

    def get_name(self):
        return self.__name

    def get_tax_number(self):
        return self.__get_tax_number

    def set_tax_number(self, tax_number):
       password = 'Saskia123'
       user_input = input('Please enter password:')
       if password == user_input:
            self.__tax_number = tax_number
            return self.__tax_number
       else:
            return 'sorry wrong password'

    def get_fur(self, fur):
        self.fur = print(input("Please describe your fur:"))
        return fur


# sully = Monster(name='Sully', tax_number='23343', fur='yes')
# print(sully.get_name())
# new_name = input("Please enter your name:")
# print(sully.set_name(new_name))
# print(sully.get_name())
#
# print(sully.set_tax_number('3000'))
from monster import *

# create a Student_monster class with Monster as a parent class
class Student_monster(Monster):
    def __init__(self, name, tax_number, fur, student_no, skill_list = []):
        super().__init__(name, tax_number, fur)
        self.student_no = student_no
        self.skill_list = skill_list

    def get_student_no(self):
        return self.student_no

    def set_student_no(self, student_no):
        self.student_no = student_no
        return self.student_no

    # allow administrative user to input new skills
    # def get_skill_list(self, skill_list):
    #     self.skill_list = print(input("Please enter your skills:"))
    #     return self.skill_list


    def add_skill(self, new_skill):
        self.skill_list.append(new_skill)
        return self.skill_list
     #
     # def get_skill(self):
     #     return self.skill_list
     #

#
# monster_1 = Student_monster()
# print(monster_1)
# print(monster_1.student_no('57632'))

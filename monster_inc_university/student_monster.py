from monster import *

# create a Student_monster class with Monster as a parent class
class Student_monster(Monster):
    def __init__(self, student_no, skill_list):
        super().__init__('James P. Sullivan', '5588888999000', 'light blue with pink polka dots')
        self.student_no = student_no
        self.skill_list = skill_list

    def get_student_no(self, student_no):
        self.student_no = print(input("Please enter your student number:"))
        return 'Your student number is ' + str(self.student_no)

    # allow administrative user to input new skills
    def get_skill_list(self, skill_list):
        self.skill_list = print(input("Please enter your skills:"))
        return self.skill_list





#
# monster_1 = Student_monster()
# print(monster_1)
# print(monster_1.student_no('57632'))
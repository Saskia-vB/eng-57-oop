from monster_inc_university.student_monster import *


# start initialize two monsters with name
student_1 = Student_monster(name='James P. Sullivan', tax_number='23243', fur='light blue', student_no='123')
student_2 = Student_monster(name='Mike', tax_number='6532', fur='green', student_no='456')
print(student_1.get_name())
print(student_2.get_name())


# add new skill
user_input = input('What new skill do you want to add? ')
# print(student_1.add_skill(user_input))

# print(student_1.get_skill())
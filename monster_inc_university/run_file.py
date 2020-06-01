from monster import *


monster_1 = Monster(name='John P. Sullivan', tax_number='67658', fur='light blue fur with pink polka dots')
print(monster_1.get_name(name=''))
print(monster_1.get_tax_number(tax_number=''))
print(monster_1.get_fur(fur=''))
#
# print(monster_1.name)
# print(monster_1.tax_number)
# print(monster_1.fur)

from student_monster import *

student_monster_1= Student_monster(student_no='124', skill_list='presentation')
print(student_monster_1.get_student_no(student_no=''))
print(student_monster_1.get_skill_list(skill_list=''))
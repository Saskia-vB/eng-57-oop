from monster import *

from student_monster import *

from course import Course


# test the instance of the class Monster

monster_1 = Monster(name='John P. Sullivan', tax_number='67658', fur='light blue fur with pink polka dots')

# ask for input to add a new monster

# print(monster_1.get_name(name=''))
# print(monster_1.get_tax_number(tax_number=''))
# print(monster_1.get_fur(fur=''))



# test the instance of the class Student_monster

student_monster_1= Student_monster(student_no='124', skill_list='presentation')
print(student_monster_1.get_student_no(student_no=''))
print(student_monster_1.get_skill_list(skill_list=''))

# test the instance of the class Course
create_course = Course


print(create_course.module_name(''))
module_name = create_course(start_date='03/09/2020')
print(module_name.start_date)








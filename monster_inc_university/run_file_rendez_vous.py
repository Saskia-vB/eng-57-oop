from student_monster import *
from course import *

# create two student objects

nathan = Student_monster(name='Nathan', tax_number='23243', fur='light blue', student_no='123')
jonathan = Student_monster(name='Jonathan', tax_number='6532', fur='green', student_no='456')

# add a skill to each of your students
nathan.add_skill('strong')
jonathan.add_skill('discreet')


# Create(initialize) a course
course_1 = Course('how to scare 101', '3rd Sep. 2020')

# Append student objects /instances to list of students attribute in one of the courses
course_1.add_student(nathan)
course_1.add_student(jonathan)


# Extra: get the list of students, iterate over it and print each of the students name
for student in course_1.list_of_students:
    print(student.get_name())
    print(student.get_student_no())
    print(student.skill_list)
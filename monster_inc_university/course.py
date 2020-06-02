
class Course:
    def __init__(self, module_name, start_date, list_of_students=[]):
        self.module_name = module_name
        self.list_of_students = list_of_students
        self.start_date = start_date

    def module_name(self):
        self.module_name = module_name

    def get_module_name(self):
        return self.module_name

    def add_student(self, student):
        self.list_of_students.append(student)
        return 'Student Added'

    def get_students(self):
        return self.list_of_students

    def get_name(self):
        all_students = []
        for student in self.list_of_students:
            all_students.append(student.get_name())
        return all_students



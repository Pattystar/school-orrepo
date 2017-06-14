class Course(object):
    instances = {}
    def __init__(self, name, auditorium):
        self.name = name
        self.aauditorium = auditorium

    def get_info(self):
        return '{}, преподвавтель {}, аудитория {}'.format(self.name, self.teacher, self.auditorium)

  
class Person(object):   
    def __init__(self, firstname, lastname, sex, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.phone = phone

    def get_info(self):
        return '{} {} {}, телефон: {}'.format(self.sex, self.lastname, self.firstname, self.course, self.phone)


class Teacher(Person):
    def __init__(self, firstname, lastname, course, sex, phone):
        super().__init__(firstname, lastname, sex, phone)
        self.course = course
        

    def get_info(self):
        return '{} {} {}, преподаватель курса: {}, телефон: {}'.format(self.sex, self.lastname, self.firstname, self.course, self.phone)
    

class Student(Person):
    def __init__(self, firstname, lastname, year_of_education, course, sex, phone):
        super().__init__(firstname, lastname, sex, phone)
        self.year_of_education = year_of_education
        self.course = course
           

    def add_student(self, student):
        if not isinstance(student, Student):
            raise OrderException('Это не студент данного курса.')

        self.students.append(student)
        

    def get_info(self):
        return '{} {} {}, студент {} курса, учебная группа {}, телефон: {}'.format(self.sex, self.lastname, self.firstname, self.year_of_education, self.course, self.phone)

course1 = Course('Разработчик Python', '2531')
teacher1 = Teacher('Господин', 'Кирилл', 'Vercetti', course1, '+79112790246')
student1 = Student('Господин', 'Дмитрий', 'Манташев', '1', course1, '+79045103861')



        
    

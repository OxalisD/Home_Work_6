class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {average_grades(self.grades)}
Курсы в процессе изучения: {" " if not self.courses_in_progress else ", ".join(self.courses_in_progress)}
Завершенные курсы: {" " if not self.finished_courses else self.finished_courses}"""

    def __eq__(self, other):
        if isinstance(other, Student):
            return average_grades(self.grades) == average_grades(other.grades)

    def __lt__(self, other):
        if isinstance(other, Student):
            return average_grades(self.grades) < average_grades(other.grades)

    def __le__(self, other):
        if isinstance(other, Student):
            return self.__eq__(other) or self.__lt__(other)

    def add_lec_grades(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached\
                and 0 < grade < 10:
            lecturer.grades.setdefault(course, [])
            lecturer.grades[course].append(grade)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grades(self.grades)}"

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return average_grades(self.grades) == average_grades(other.grades)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return average_grades(self.grades) < average_grades(other.grades)

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.__eq__(other) or self.__lt__(other)


class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_grades(grades : dict, course=None):
    """Подсчитывает средний бал. Работает и со студентами и с лекторами.
    Если не передать курс, то будет считать по всем"""
    if not grades:
        return 0
    grades_sum = 0
    grades_len = 0
    if course == None:
        for grade in list(grades.values()):
            grades_sum += sum(grade)
            grades_len += len(grade)
        return  grades_sum / grades_len
    elif course in grades.keys():
        return sum(grades[course]) / len(grades[course])
    else:
        print("Неверный курс")


def stud_average(persons : list, course):
    """Подсчитывает средний бал по всем студентам или лекторам."""
    sum_grades = 0
    len_pers = 0
    for person in persons:
        if course in person.grades.keys():
            sum_grades += average_grades(person.grades, course)
            len_pers += 1
    return sum_grades / len_pers


stud = Student("Danila", "Kislitsa", "male")
stud2 = Student("Maria", "Biryukova", "female")
stud.courses_in_progress = ["Python"]
stud2.courses_in_progress = ["Python" , "Java"]
stud.finished_courses = "Введение в программирование"
stud2.finished_courses = "Введение в программирование"
lect = Lecturer("Artem", "Egorof")
lect2 = Lecturer("Mick", "Jagger")
lect.courses_attached = "Python"
lect2.courses_attached = "Python"
stud.add_lec_grades(lect,"Python", 10)
stud2.add_lec_grades(lect,"Python", 9)
stud.add_lec_grades(lect2, "Python", 3)
stud2.add_lec_grades(lect2, "Python", 7)
rev = Reviewer("Jim", "Morrison")
rev2 = Reviewer("David", "Gilmour")
rev.courses_attached = "Java"
rev2.courses_attached = "Python"
rev2.rate_hw(stud, "Python", 6)
rev2.rate_hw(stud, "Python", 10)
rev2.rate_hw(stud2, "Python", 8)
rev2.rate_hw(stud2, "Python", 10)
print(stud_average([stud,stud2], "Python"))
print(stud_average([lect,lect2],"Python"))
print(lect)
print(stud)
print(stud2)
print(lect == lect2)
print(stud == stud2)
print(average_grades(stud.grades, "Python"))
print(lect2)

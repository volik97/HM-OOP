class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
        self.courses_in_progress.remove(course_name)  
    
    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _middle_grade(self):
        grades_list = []
        for values in self.grades.values():
            for value in values:
                grades_list.append(value)
        middle_grade = sum(grades_list)/len(grades_list)
        return middle_grade
    
    def __str__(self):
        res = f'Имя: {self.name} \n' \
            f'Фамилия: {self.surname} \n' \
            f'Средняя оценка за домашние задания: {self._middle_grade():.1f} \n' \
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
            f'Завершенные курсы: {", ".join(self.finished_courses)} \n'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Нельзя сравнить")
            return
        return self._middle_grade() < other._middle_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
    
    def _middle_grade(self):
        grades_list = []
        for values in self.grades.values():
            for value in values:
                grades_list.append(value)
        middle_grade = sum(grades_list)/len(grades_list)
        return middle_grade
    
    def __str__(self):
        res = f"Имя: {self.name} \n" \
            f"Фамилия: {self.surname} \n" \
            f"Средняя оценка за лекции: {self._middle_grade():.1f}"
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Нельзя сравнить")
            return
        return self._middle_grade() < other._middle_grade()

class Reviewer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        res =  f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n'
        return res


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

 
first_student = Student("Vasya", "Pupkin", "м")
first_student.courses_in_progress += ["GIT"]
first_student.courses_in_progress += ["Python"]
first_student.finished_courses += ["JS"]

second_student = Student("Petya", "Gubkin", "м")
second_student.courses_in_progress += ["Python"]
second_student.finished_courses += ["C#"]

first_lecturer = Lecturer("Ivan", "Vasilyev")
first_lecturer.courses_attached += ["Python"]
first_lecturer.courses_attached += ["GIT"]

second_lecturer = Lecturer("Vitaliy", "Tsal")
second_lecturer.courses_attached += ["GIT"]

first_reviewer = Reviewer("Anton", "Kozlov")
first_reviewer.courses_attached += ["Python"]

second_reviewer = Reviewer("Jhon", "Price")
second_reviewer.courses_attached += ["GIT"]
second_reviewer.courses_attached += ["Python"]

students_list = [first_student, second_student]
lecturer_list = [first_lecturer, second_lecturer]

def _middle_rate_students(students, course):
    grades_list = []
    for student in students:
        for values in student.grades.values():
            for value in values:
                grades_list.append(value)
        middle_grade = sum(grades_list)/len(grades_list)
        return middle_grade

def _middle_rate_lecturer(lecturer, course):
    grades_list = []
    for lector in lecturer:
        for values in lector.grades.values():
            for value in values:
                grades_list.append(value)
        middle_grade = sum(grades_list)/len(grades_list)
        return middle_grade

first_student.rate_lector(second_lecturer, "GIT", 9)
first_student.rate_lector(second_lecturer, "GIT", 10)
first_student.rate_lector(first_lecturer, "GIT", 8)
first_student.rate_lector(first_lecturer, "GIT", 8)
first_student.rate_lector(first_lecturer, "Python", 9)
second_student.rate_lector(first_lecturer, "Python", 10)
second_student.rate_lector(first_lecturer, "Python", 10)

second_reviewer.rate_hw(first_student, "Python", 10)
second_reviewer.rate_hw(first_student, "GIT", 8)
second_reviewer.rate_hw(first_student, "GIT", 10)
first_reviewer.rate_hw(first_student, "Python", 10)
first_reviewer.rate_hw(second_student, "Python", 7)
first_reviewer.rate_hw(second_student, "Python", 7)
first_reviewer.rate_hw(second_student, "Python", 8)

print(f"Список студентов: \n\n{first_student} \n\n{second_student}" \
      f"\n\nСписок лекторов: \n\n{first_lecturer} \n\n{second_lecturer}" \
      f"\n\nСписок проверяющих: \n\n{first_reviewer} \n\n{second_reviewer}")

print(f"Средняя оценка за дз у {first_student.surname} больше, чем у {second_student.surname} - {second_student < first_student}")
print(f"Средняя оценка за лекции у {first_lecturer.surname} меньше, чем у {second_lecturer.surname} - {second_lecturer < first_lecturer}\n")

print(f'Средняя оценка студентов за курс GIT: {_middle_rate_students(students_list, "GIT")}')
print(f'Средняя оценка студентов за курс Python: {_middle_rate_students(students_list, "Python")}')
print(f'Средняя оценка лекторов за курс Python: {_middle_rate_lecturer(lecturer_list, "Python")}')
print(f'Средняя оценка лекторов за курс GIT: {_middle_rate_lecturer(lecturer_list, "GIT")}')
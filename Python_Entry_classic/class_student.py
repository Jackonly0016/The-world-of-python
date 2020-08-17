class Student(object):
    def __init__(self, name="", school="", grade=""):
        if not name:
            name = input("What is the student's name?")
        if not school:
            school = input("What is the student's school?")
        if not grade:
            grade = self.get_grade()
        self.name = name
        self.school = school
        self.grade = grade

    def get_grade(self):
        while True:
            grade = input("What is the student's grade? [K, 1-5] ")
            if grade.lower() not in ['k', '1', '2', '3', '4', '5']:
                print("I'm sorry, but {} isn't valid".format(grade))
            else:
                return grade

    def print_student(self):
        print("Name: {}".format(self.name))
        print("School: {}".format(self.school))
        print("Grade: {}".format(self.grade))

def print_roster(students):
    print("Students in the system:")
    for student in students:
        print("*"*15)
        student.print_student()

def main():
    student1 = Student(name="Carrie Kale", grade="3", school="Marshall")
    student2 = Student(name="Byron Bale", grade="2", school="Minnieville")
    student3 = Student(name="Sarah Chandler", grade="K", school="Woodbridge")
    students = [student1, student2, student3]
    print_roster(students)

if __name__ == "__main__":
    main()



from typing import List
students = []

def get_students_name():
    students_name = []
    for iemand in students:
        students_name = iemand.capitalize()
    return students_name


def print_students_name():
    students_name = get_students_name()
    print(students_name)


def add_student(name):
    students.append(name)


def add_student2(name, id=111):
    if id != 111:
        students.append(name)


def add_student3(name, id=111):
    studentmetid = {"naam": name, "nr": id}
    students.append(studentmetid)
    print(studentmetid)



student_list = get_students_name()
add_student("simone")
add_student("marco")
add_student("marcel")
add_student(name="lieke")
print(students)
studentennaam = get_students_name()
print(studentennaam)
add_student2("marthe")
print_students_name()
add_student2("inge", 222)
add_student2("arnoud")
print_students_name()
print(students)
add_student3(name="jurgen", id=777)

print("tekst", "tekst2")




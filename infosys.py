class InformationSystem:
    student_list = []
    teacher_list = []
    course_list = []

    def create_student(self):
        InformationSystem.student_list.append(self)

    def create_teacher(self):
        InformationSystem.teacher_list.append(self)

    def create_course(self):
        InformationSystem.course_list.append(self)


"""pomocne funkcie"""


def choosing_teacher_for_course(temp2):
    temp = temp2.split()
    raise_error(0)
    while True:
        for teacher in InformationSystem.teacher_list:
            if teacher.name == temp[0] and teacher.surname == temp[1]:
                return teacher
        else:
            print("No teacher with that name exist in database")



def choosing_student_for_course(temp3):
    list_of_students = []
    raise_error(temp3)
    while len(list_of_students) != temp3:
        temp = input("select students")
        temp1 = temp.split()
        for student in InformationSystem.student_list:
            if student.name == temp1[0] and student.surname == temp1[1]:
                list_of_students.append(student)
                break
        else:
            print("No student with that name exist in database")
    return list_of_students


def raise_error(value):
    if len(InformationSystem.teacher_list) == 0:
        raise RuntimeError("There are no teachers")
    if len(InformationSystem.student_list) < value:
        raise RuntimeError("There is not enough students")





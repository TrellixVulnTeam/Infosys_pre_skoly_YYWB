from course import Course
from person import Teacher, Student
import infosys as inf
while True:

    command = str(input("Choose option ")).lower().strip()

    if command == "create teacher":
        temp = input("insert name ").lower().strip()
        temp2 = input("insert surname ").lower().strip()
        temp3 = input("insert degree ").lower().strip()
        inf.InformationSystem.create_teacher(Teacher(temp, temp2, temp3))

    elif command == "check teacher list":
        for teacher in inf.InformationSystem.teacher_list:
            print(f'{teacher.degree} {teacher.name} {teacher.surname}')

    elif command == "create student":
        temp = input("insert name ").lower().strip()
        temp2 = input("insert surname ").lower().strip()
        temp3 = input("insert grade ").lower().strip()
        inf.InformationSystem.create_student(Student(temp, temp2, temp3))

    elif command == "check student list":
        for student in inf.InformationSystem.student_list:
            print(f'{student.name} {student.surname} {student.grade}')

    elif command == "create course":
        temp = input("insert course name ").lower().strip()
        temp2 = input("select teacher ").lower().strip()
        try:
            temp3 = int(input("how many students will be in course? "))
        except ValueError:
            print("Value has to be a number")
            continue
        inf.InformationSystem.create_course\
            (Course(temp,inf.choosing_teacher_for_course(temp2), inf.choosing_student_for_course(temp3)))

    elif command == "check course list":
        for course in inf.InformationSystem.course_list:
            print(course.name)
            print(f'Teacher {course.teacher.degree} {course.teacher.name} {course.teacher.surname}')
            for student in course.student_list:
                print(f'{student.name} {student.surname} {student.grade}')

    elif command == "exit":
        break

    elif command == "help":
        print("create teacher\n"
              "check teacher list\n"
              "create student\n"
              "check student list\n"
              "create course\n"
              "check course list\n"
              "exit")
    else:
        print("choose the proper command")

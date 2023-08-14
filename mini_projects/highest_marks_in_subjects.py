def highest_marks_in_maths():
    max_marks_in_maths = 0
    student_with_hightest_marks_in_maths = ''
    for student in students_list:
        if (student.get('maths')) > max_marks_in_maths:
            max_marks_in_maths = student.get('maths')
            student_with_hightest_marks_in_maths = student.get('name')
    print(f"maximum marks in maths is {max_marks_in_maths} and it is scored by {student_with_hightest_marks_in_maths}")

def highest_marks_in_science():
    max_marks_in_science = 0
    student_with_hightest_marks_in_science = ''
    for student in students_list:
        if (student.get('science')) > max_marks_in_science:
            max_marks_in_science = student.get('science')
            student_with_hightest_marks_in_science = student.get('name')
    print(f"maximum marks in science is {max_marks_in_science} and it is scored by {student_with_hightest_marks_in_science}")

def highest_marks_in_social():
    max_marks_in_social = 0
    student_with_hightest_marks_in_social = ''
    for student in students_list:
        if (student.get('social')) > max_marks_in_social:
            max_marks_in_social = student.get('social')
            student_with_hightest_marks_in_social = student.get('name')
    print(f"maximum marks in social is {max_marks_in_social} and it is scored by {student_with_hightest_marks_in_social}")

student1 = {'name': 'sooraj','maths':76,'science':59,'social':67}
student2 = {'name': 'dheeraj','maths':94,'science':45,'social':50}
student3 = {'name': 'thanmay','maths':34,'science':99,'social':93}

students_list = [student1,student2,student3]

highest_marks_in_maths()
highest_marks_in_science()
highest_marks_in_social()

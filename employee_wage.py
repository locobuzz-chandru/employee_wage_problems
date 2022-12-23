import random


def attendance():
    """
    Function checks employee attendance
    :return: Employee Attendance
    """
    is_present = 1
    emp_check = random.randrange(0, 2)
    if emp_check == is_present:
        print("Employee is present")
    else:
        print("Employee is absent")


attendance()

import random


def daily_wage():
    """
    Function calculates daily wage
    :return: Employee Attendance
    """
    is_present = 1
    emp_rate_per_hour = 20
    emp_hrs = 0
    emp_check = random.randrange(0, 2)
    if emp_check == is_present:
        print("Employee is present")
        emp_hrs = 8
    else:
        print("Employee is absent")

    emp_wage = emp_hrs * emp_rate_per_hour
    print("Employee Wage : ", emp_wage)


daily_wage()
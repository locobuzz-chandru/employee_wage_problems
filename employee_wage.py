import random


def daily_wage():
    """
    Function calculates daily wage
    :return: Employee Attendance
    """
    is_full_time = 1
    is_part_time = 2
    emp_rate_per_hour = 20
    emp_hrs = 0
    emp_check = random.randrange(0, 3)
    if emp_check == is_full_time:
        print("Full time")
        emp_hrs = 8
    elif emp_check == is_part_time:
        print("Part time")
        emp_hrs = 4
    else:
        print("Employee is absent")

    emp_wage = emp_hrs * emp_rate_per_hour
    print("Employee Wage : ", emp_wage)


daily_wage()

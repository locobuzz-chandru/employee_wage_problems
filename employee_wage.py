import random


def calc_wage():
    """Function to calculate wage"""
    total_emp_hrs = 0
    max_working_hrs = 100
    total_emp_days = 0
    max_working_days = 20
    total_wage = 0
    emp_wage_per_hr = 15
    while total_emp_hrs < max_working_hrs and total_emp_days < max_working_days:
        emp_check = random.randrange(0, 3)
        emp_hrs = check_attendance(emp_check)
        if emp_hrs != 0:
            total_emp_days = total_emp_days + 1
        total_emp_hrs += emp_hrs
        total_wage += emp_hrs * emp_wage_per_hr
    print(f'Total wage is : {total_wage}')


def check_attendance(emp_check):
    """Function to check employee working hours"""
    switcher = {
        0: 0,
        1: 8,
        2: 4
    }
    return switcher.get(emp_check)


if __name__ == '__main__':
    calc_wage()

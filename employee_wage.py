import random


def calculate_wage(emp_rate_per_hr):
    """
    Function to calculate wage
    """
    r = random.randint(0, 2)
    emp_hrs = get_emp_hrs(r)
    emp_wage = emp_hrs * emp_rate_per_hr
    print(f'Employee wage is {emp_wage}')


def get_emp_hrs(r):
    """
    Function to check employee working hours
    """
    switcher = {
        0: 0,
        1: 8,
        2: 4,
    }
    return switcher.get(r)


emp_rate_per_hr = 20
calculate_wage(emp_rate_per_hr)

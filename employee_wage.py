# Program to calculate Employee Wage
import random


def wage_for_month():
    """
    Function calculates wage of month
    """
    is_full_time = 1
    is_part_time = 2
    emp_rate_per_hour = 20
    num_of_working_days = 20
    total_emp_wage = 0
    for days in range(num_of_working_days):
        emp_check = random.randrange(0, 3)
        if emp_check == is_full_time:
            emp_hrs = 8
        elif emp_check == is_part_time:
            emp_hrs = 4
        else:
            emp_hrs = 0

        emp_wage = emp_hrs * emp_rate_per_hour
        total_emp_wage += emp_wage

    print(f'Daily wage is : {total_emp_wage}')


wage_for_month()

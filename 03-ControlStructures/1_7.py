def calculate_salary(is_bonus, bonus_rate):
    basic_salary = 5000

    if is_bonus:
        total_salary = basic_salary + (basic_salary * bonus_rate)
    else:
        total_salary = basic_salary

    return basic_salary, total_salary

if __name__ == "__main__":
    is_bonus_1 = False
    bonus_rate_1 = 0

    is_bonus_2 = True 
    bonus_rate_2 = 0.30

    basic_2, total_2 = calculate_salary(is_bonus_2, bonus_rate_2)
    print(f'Basic salary: {basic_2}')
    print(f'Bonus included? {is_bonus_2}')
    print(f'Total salary: {total_2}')

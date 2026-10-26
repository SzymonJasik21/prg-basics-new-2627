def check_even_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    test_numbers = [4,5,10,13,21,25]

    for number in test_numbers:
        is_even = check_even_odd(number)

        if is_even:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
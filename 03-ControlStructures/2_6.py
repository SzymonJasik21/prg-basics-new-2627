def f(number):
    if number > 0:
        return f'Number {number} is positive'
    elif number < 0:
        return f'Number {number} is negative'
    else:
        return 'Number is 0'

if __name__ == "__main__":
    print(f(7))
    print(f(1))
    print(f(0))
    print(f(-1))
    print(f(-4))
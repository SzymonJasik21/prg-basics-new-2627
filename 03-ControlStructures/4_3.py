def f(month, day):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        return 1 <= day <= 28
    return False

if __name__ == "__main__":
    print(f(3, 17))
    print(f(9, 31))
    print(f(2, 30))
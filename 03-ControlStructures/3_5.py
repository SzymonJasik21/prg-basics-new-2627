def f(month):
    if month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

if __name__ == "__main__":
    print(f(1))
    print(f(2))
    print(f(4))
    print(f(12))
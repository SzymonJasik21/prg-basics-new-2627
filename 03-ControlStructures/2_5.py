def f(month):
    if month >= 10:
        return 4
    elif month >= 7:
        return 3
    elif month >= 4:
        return 2
    else:
        return 1

if __name__ == "__main__":
    print(f(12))
    print(f(10))
    print(f(9))
    print(f(1))
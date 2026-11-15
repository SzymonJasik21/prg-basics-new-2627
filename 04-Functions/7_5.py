def f(number, x, y):
    result = (x <= number <= y)
    return result


if __name__ == "__main__":
    print(f(7, 2, 15))
    print(f(20, 2, 15))
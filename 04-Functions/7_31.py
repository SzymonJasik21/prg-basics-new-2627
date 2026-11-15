def power(x, n):
    if n == 0:
        result = 1
    else:
        result = x * power(x, n - 1)
    return result


if __name__ == "__main__":
    print(power(5, 3))
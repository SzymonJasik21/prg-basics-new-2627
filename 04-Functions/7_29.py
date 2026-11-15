def factorial(n):
    if n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result


if __name__ == "__main__":
    print(factorial(5))
    print(factorial(4))
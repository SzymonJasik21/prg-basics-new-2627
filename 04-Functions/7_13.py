def f(n):
    result = ""
    for i in range(1, n + 1):
        result = result + str(i)
    return result


if __name__ == "__main__":
    print(f(11))
    print(f(4))
    print(f(30))


def f(n):
    result = ""
    current = 1
    while current <= n:
        result = result + str(current)
        current = current + 1
    return result


if __name__ == "__main__":
    print(f(11))
    print(f(4))
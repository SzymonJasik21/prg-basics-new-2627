def f(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0:
        result = True
    else:
        result = False
    return result


if __name__ == "__main__":
    print(f(11, 6, -4))
    print(f(5, 4, 14))


def f(n1, n2, n3):
    smallest = min(n1, n2, n3)
    result = (smallest < 0)
    return result


if __name__ == "__main__":
    print(f(11, 6, -4))
    print(f(5, 4, 14))
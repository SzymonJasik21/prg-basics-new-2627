def sum_natural(n):
    if n == 1:
        result = 1
    elif n== 0:
        result = 0
    else:
        result = n + sum_natural(n - 1)
    return result


if __name__ == "__main__":
    print(sum_natural(10))
    print(sum_natural(0))
    print(sum_natural(1))
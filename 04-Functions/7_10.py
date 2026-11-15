def f(x, y):
    count = 0
    for num in range(x, y + 1):
        if num < 0 and num % 2 == 0:
            count = count + 1
    return count


if __name__ == "__main__":
    print(f(-7, 8))
    print(f(-1, 11))
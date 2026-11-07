def f(start, end):
    total = 0
    for i in range(start, end + 1):
        if not i % 2 == 0:
            continue
        total += i
    return total

if __name__ == "__main__":
    print(f(1, 10))
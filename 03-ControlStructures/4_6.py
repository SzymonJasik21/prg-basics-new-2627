def f(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

if __name__ == "__main__":
    print(f(5, 10))
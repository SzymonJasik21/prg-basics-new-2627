def f(n):
    return "* " * n

if __name__ == "__main__":
    for i in range(1, 6):
        print(f(i))
    for i in range(4, 0, -1):
        print(f(i))
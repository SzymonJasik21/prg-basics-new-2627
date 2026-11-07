def f(x, y):
    if x >= 0 or y >= 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(f(5, -3))
    print(f(-2, -4))
    print(f(0, -1))
def f(i, j):
    return i + 7 * j

if __name__ == "__main__":
    for i in range(1, 8):
        for j in range(7):
            print(f(i, j), end=" ")
        print()
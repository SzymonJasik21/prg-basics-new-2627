def f(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    for i in range(1, 21):
        print(f(i), end=" ")

def f(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    N = 5
    count = 0
    num = 2
    print("Prime numbers:", end=" ")
    while count < N:
        if f(num):
            print(num, end=" ")
            count += 1
        num += 1
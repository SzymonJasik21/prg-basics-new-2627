def f(n):
    sum_even = 0
    i = 1
    while i <= n:
        if i % 2 == 0:
            sum_even += i
        i += 1
    return sum_even

if __name__ == "__main__":
    print(f(10))
def f(n):
    primes_found = 0
    candidate = 1
    while primes_found < n:
        candidate = candidate + 1
        divisors = 0
        for i in range(1, candidate + 1):
            if candidate % i == 0:
                divisors = divisors + 1
        if divisors == 2:
            primes_found = primes_found + 1
    return candidate

if __name__ == "__main__":
    print(f(1))
    print(f(5))

#2 3 5 7 9 11 13 17 19 23 29 31 37 39 41 43 47 51 53 57 
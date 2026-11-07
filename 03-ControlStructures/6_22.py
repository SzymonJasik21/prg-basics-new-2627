def f(n):
    if n % 3 == 0 and n % 5 == 0:
        return "BINGO"
    elif n % 3 == 0:
        return "THREE"
    elif n % 5 == 0:
        return "FIVE"
    return n

if __name__ == "__main__":
    for i in range(1, 31):
        print(f(i), end=" ")
def f(amount):
    c5 = amount // 5
    remainder = amount % 5
    c2 = remainder // 2
    c1 = remainder % 2
    return c5, c2, c1

if __name__ == "__main__":
    amount = 18
    c5, c2, c1 = f(amount)
    print(f"The amount of PLN {amount} in coins:")
    print(f"5 PLN coins: {c5}")
    print(f"2 PLN coins: {c2}")
    print(f"1 PLN coins: {c1}")
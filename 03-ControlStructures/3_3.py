def f(age):
    if age < 18 or age >= 65:
        return True
    else:
        return False

if __name__ == "__main__":
    print(f(72))
    print(f(65))
    print(f(64))
    print(f(18))
    print(f(17))
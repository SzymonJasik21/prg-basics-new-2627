def f(hours):
    if hours <= 2:
        return 5
    elif hours <= 6:
        return 15
    else:
        return 20

if __name__ == "__main__":
    print(f"{f(4)} PLN")
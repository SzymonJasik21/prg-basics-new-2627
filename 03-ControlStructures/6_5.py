def f(temperature):
    if temperature > 35:
        return "It is extremely hot"
    elif temperature > 30:
        return "It is hot"
    elif temperature >= 15:
        return "It is warm"
    elif temperature >= 0:
        return "It is cold"
    else:
        return "Warning, frost"

if __name__ == "__main__":
    print(f(33))
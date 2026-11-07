def f(age):
    if age < 13:
        return "Child"
    elif 13 <= age <= 19:
        return "Teen"
    elif 20 <= age <= 64:
        return "Adult"
    elif age >= 65:
        return "Senior"

if __name__ == "__main__":
    print(f(15))
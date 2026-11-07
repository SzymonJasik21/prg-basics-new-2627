def f(person1_name, person1_age, person2_name, person2_age):
    if person1_age >= 18 and person2_age >= 18:
        return True
    else:
        return False

if __name__ == "__main__":
    print(f("Anna", 20, "Peter", 19))
    print(f("Anna", 20, "Peter", 15))
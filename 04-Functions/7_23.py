def f(password):
    has_min_length = (len(password) >= 6)
    has_unique_chars = (len(set(password)) == len(password))
    is_valid = has_min_length and has_unique_chars
    return is_valid


if __name__ == "__main__":
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))
    print(f("qwerty"))
    print(f(""))
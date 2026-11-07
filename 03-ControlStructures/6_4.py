def f(password):
    return len(password) >= 12

if __name__ == "__main__":
    password_test = "short"
    if not f(password_test):
        print("Password too short (min. 12 chars)")
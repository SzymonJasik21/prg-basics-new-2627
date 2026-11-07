def f(a, b):
    return a * b

if __name__ == "__main__":
    number = 6
    for i in range(1, 11):
        print(f"{number} x {i} = {f(number, i)}")
import random

def f(a, b):
    return random.randint(a, b)

if __name__ == "__main__":
    for _ in range(20):
        print(f(5, 10), end=" ")
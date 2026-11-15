def f(number1, number2, number3):
    largest = max(number1, number2, number3)
    smallest = min(number1, number2, number3)
    difference = largest - smallest
    return difference


if __name__ == "__main__":
    print(f(7, 4, 9))
    print(f(2, 12, 8))
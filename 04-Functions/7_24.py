def f(expression):
    total = 0
    sign = 1
    for char in expression:
        if char == "+":
            sign = 1
        elif char == "-":
            sign = -1
        else:
            digit = int(char)
            total = total + sign * digit
    return total

if __name__ == "__main__":
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))
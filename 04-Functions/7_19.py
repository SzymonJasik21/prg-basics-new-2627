def f(number):
    digits_str = str(number)
    total_sum = 0
    for char in digits_str:
        if digits_str.count(char) > 1:
            total_sum = total_sum + int(char)
    return total_sum


if __name__ == "__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))
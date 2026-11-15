def f(product_code):
    d1 = int(product_code[0])
    d2 = int(product_code[1])
    d3 = int(product_code[2])
    control_digit = int(product_code[3])
    digits_sum = d1 + d2 + d3
    is_valid = (digits_sum % 7 == control_digit)
    return is_valid


if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))
import math

def calculate_math_operations():
    square_root = math.sqrt(16)

    natural_log = math.log(5)

    sine_90 = math.sin(math.radians(90))


    return (square_root, natural_log, sine_90)

if __name__ == "__main__":

    #results = calculate_math_operations()

    square_root, natural_log, sine_90 = calculate_math_operations()

    print('A square root of 7 is', square_root)
    print('A natural logarithm of 5 is', natural_log)
    print('A sine of 90 degrees is', sine_90)

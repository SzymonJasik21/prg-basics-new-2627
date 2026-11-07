def convert_number(number):

    binary_num = bin(number)
    

    hex_num = hex(number)
    
    return binary_num, hex_num

if __name__ == "__main__":

    number = 125
    
    binary_num, hex_num = convert_number(number)
    
    print(f"Enter number: {number}")
    print(f"Binary number: {binary_num}")
    print(f"Hexadecimal number: {hex_num}")
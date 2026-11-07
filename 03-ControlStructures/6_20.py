def f(n):
    if n == 0:
        return "0"
    
    binary_str = ""
    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str
        n = n // 2
        
    return binary_str

if __name__ == "__main__":
    n = 12
    result = f(n)
    print(f"{n}(10) = {result}(2)")
def check_clothing_size(size):
    
    if size == 'S':
        return 'S: Small size'
    elif size == 'M':
        return 'M: Medium size'
    elif size == 'L':
        return 'L: Large size'
    elif size == 'XL':
        return 'XL: Extra large size'
    else:
        
        return 'Incorrect symbol'


if __name__ == "__main__":

    symbols_to_test = ['S', 'M', 'L', 'XL', 'X', 'XXL']
    
    for symbol in symbols_to_test:
        result = check_clothing_size(symbol)
        print(f"Enter size symbol: {symbol}")
        print(result)

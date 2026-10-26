def test_builtin_functions(keyboard_letter):
    # Największa liczba
    max_number = max(7, 5, 6, 3, 8, 2)
    
    # Najmniejsza liczba
    min_number = min(4, 7, 2, 3, 9, 8)
    
    # Długość frazy
    str_length = len("computer science")
    
    # Znak z klawiatury (przekazany jako argument, aby uniknąć input() w funkcji)
    letter = keyboard_letter
    
    # Zamiana stringa na liczbę całkowitą
    number_from_str = int("20303")
    
    # Zamiana liczby na system binarny
    binary_str = bin(304)
    
    # Zamiana liczby na system heksadecymalny
    hex_str = hex(304)
    
    # Kod Unicode dla znaku €
    unicode_val = ord('€')
    
    # Wartość bezwzględna
    abs_val = abs(-17)
    
    return (max_number, min_number, str_length, letter, 
            number_from_str, binary_str, hex_str, unicode_val, abs_val)


# --- BLOK TESTUJĄCY ---
if __name__ == "__main__":
    # Symulacja wczytania litery z klawiatury (np. litery 'X')
    simulated_input = 'X' 
    
    # Wywołanie funkcji i rozpakowanie zwróconych wyników do zmiennych
    results = test_builtin_functions(simulated_input)
    (max_number, min_number, str_length, letter, 
     number_from_str, binary_str, hex_str, unicode_val, abs_val) = results
     
    # Wypisywanie wyników (częściowo odtwarzające format ze zdjęcia)
    print('Max number of 7,5,6,3,8,2 is', max_number)
    print('Min number of 4,7,2,3,9,8 is', min_number)
    print('The number of characters in "computer science" is', str_length)
    print('Letter read from the keyboard is', letter)
    print('Number representing the string "20303" is', number_from_str)
    print('Binary string representing decimal number 304 is', binary_str)
    print('Hexadecimal string representing decimal number 304 is', hex_str)
    print('Integer representing the Unicode code of the € sign is', unicode_val)
    print('Absolute value of -17 is', abs_val)
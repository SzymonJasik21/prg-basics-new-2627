def convert_temperature(celsius):
    # Krok 1: Obliczenie temperatury w Kelvinach (dodanie 273.15 do wartości w Celsjuszach)
    kelvin = celsius + 273.15
    
    # Krok 2: Obliczenie temperatury w Fahrenheitach (pomnożenie przez 9/5 i dodanie 32)
    fahrenheit = (celsius * 9/5) + 32
    
    # Krok 3: Zwrócenie obu wyliczonych wartości
    return kelvin, fahrenheit

if __name__ == "__main__":
    # Test 1: dla 25 stopni Celsjusza
    kelvin1, fahrenheit1 = convert_temperature(25)
    print(f"25 stopni C to {kelvin1} K oraz {fahrenheit1} F.")
    
    # Test 2: dla 0 stopni Celsjusza
    kelvin2, fahrenheit2 = convert_temperature(0)
    print(f"0 stopni C to {kelvin2} K oraz {fahrenheit2} F.")
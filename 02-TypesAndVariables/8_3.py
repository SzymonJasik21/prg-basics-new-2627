def convert_temperature(celsius):
    
    kelvin = celsius + 273.15
    
    
    fahrenheit = (celsius * 9/5) + 32
    
   
    return kelvin, fahrenheit

if __name__ == "__main__":
    
    kelvin1, fahrenheit1 = convert_temperature(25)
    print(f"25 stopni C to {kelvin1} K oraz {fahrenheit1} F.")
    
    
    kelvin2, fahrenheit2 = convert_temperature(0)
    print(f"0 stopni C to {kelvin2} K oraz {fahrenheit2} F.")
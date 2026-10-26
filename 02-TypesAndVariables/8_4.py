def convert_height(cm):
    # Przeliczenie centymetrów na całkowitą liczbę cali (1 cal to 2.54 cm)
    total_inches = round(cm / 2.54)
    
    # Obliczenie liczby stóp przy użyciu dzielenia bez reszty (1 stopa to 12 cali)
    feet = total_inches // 12
    
    # Obliczenie pozostałych cali przy użyciu operatora reszty z dzielenia (modulo)
    inches = total_inches % 12
    
    return feet, inches

if __name__ == "__main__":
    cm = 170
    feet, inches = convert_height(cm)
    print(f"I am {cm}cm tall, i.e. {feet} feet and {inches} inches")
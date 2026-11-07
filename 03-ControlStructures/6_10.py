def calculate_dog_years(human_years):
    if human_years <= 2:
        return human_years * 10.5
    return 21 + (human_years - 2) * 4

if __name__ == "__main__":
    hy = 15
    dy = calculate_dog_years(hy)
    dy_formatted = int(dy) if dy == int(dy) else dy  # ucina .0 jeśli wynik jest całkowity
    
    print(f"Enter the dog's age in human years: {hy}")
    print(f"The dog's age in dog's years is {dy_formatted} years.")
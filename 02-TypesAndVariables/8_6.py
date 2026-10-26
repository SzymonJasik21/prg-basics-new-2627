def calculate_transport_cost(distance, fuel_price, fuel_consumption):
    # Obliczenie całkowitego zużycia paliwa (spalanie jest podane na 100 km)
    total_fuel_consumption = (distance / 100) * fuel_consumption
    
    # Obliczenie całkowitego kosztu transportu
    total_cost = total_fuel_consumption * fuel_price
    
    return total_fuel_consumption, total_cost

if __name__ == "__main__":
    # Przykładowe dane do przetestowania funkcji
    distance = 350          # dystans w km
    fuel_price = 6.50       # cena za litr
    fuel_consumption = 8.0  # spalanie w litrach na 100 km
    
    total_fuel, total_cost = calculate_transport_cost(distance, fuel_price, fuel_consumption)
    
    print(f"Dystans: {distance} km")    
    print(f"Całkowite zużycie paliwa: {total_fuel} l")
    print(f"Całkowity koszt transportu: {total_cost} PLN")
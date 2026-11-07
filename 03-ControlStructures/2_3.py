def calculate_fuel_consumption(driving_mode, distance):
    if driving_mode == 'A':
        fuel_consumption = 7
    elif driving_mode == 'M':
        fuel_consumption = 9
    elif driving_mode == 'E':
        fuel_consumption = 6
        
    total_consumption = (distance / 100) * fuel_consumption
    return total_consumption

if __name__ == "__main__":
    driving_mode = 'M'
    distance = 200
    total_consumption = calculate_fuel_consumption(driving_mode, distance)
    print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')
    
    driving_mode = 'A'
    distance = 400
    total_consumption = calculate_fuel_consumption(driving_mode, distance)
    print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')
    
    driving_mode = 'E'
    distance = 350
    total_consumption = calculate_fuel_consumption(driving_mode, distance)
    print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')
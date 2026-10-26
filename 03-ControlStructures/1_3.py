def check_speed_limit(car_speed):
    # Limit prędkości na polskiej autostradzie
    speed_limit = 140
    
    # Instrukcja warunkowa sprawdzająca, czy prędkość została przekroczona
    if car_speed > speed_limit:
        return True
    else:
        return False

# --- BLOK TESTUJĄCY ---
if __name__ == "__main__":
    # Test 1: Prędkość przekraczająca limit
    car_speed_1 = 158
    is_exceeded_1 = check_speed_limit(car_speed_1)
    
    if is_exceeded_1:
        print(f'Your speed is {car_speed_1}km/h')
        print('Warning: speed limit exceeded!!')
        
    print("-" * 20)
    
    # Test 2: Prędkość w granicach limitu
    car_speed_2 = 120
    is_exceeded_2 = check_speed_limit(car_speed_2)
    
    if is_exceeded_2:
        print(f'Your speed is {car_speed_2}km/h')
        print('Warning: speed limit exceeded!!')
    else:
        print(f'Your speed is {car_speed_2}km/h - speed is within the limit.')
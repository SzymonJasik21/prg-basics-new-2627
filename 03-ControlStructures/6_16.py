def calculate_washing_time(product, extra_rinse, extra_spin):
    base_time = 0
    if product in ["jacket", "j"]:
        base_time = 40
    elif product in ["underwear", "u"]:
        base_time = 70
    elif product in ["shoes", "s"]:
        base_time = 20

    if extra_rinse:
        base_time += 15
    if extra_spin:
        base_time += 9
        
    return base_time

if __name__ == "__main__":
    washing_product = "shoes"
    rinse = True
    spin = False
    
    total_time = calculate_washing_time(washing_product, rinse, spin)
    
    print(f'washing_product = "{washing_product}"')
    print(f"rinse = {rinse}")
    print(f"spin = {spin}")
    print(f"Total washing time: {total_time} minutes")
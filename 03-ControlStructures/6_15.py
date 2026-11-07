def is_valid_ean(ean):
    return len(ean) == 13 and ean.isdigit()

def is_from_poland(ean):
    return ean.startswith("590")

if __name__ == "__main__":
    ean = "5901230094938"
    print(f"Enter EAN-13 article number: {ean}")
    
    if is_valid_ean(ean):
        print("Article number is correct")
        if is_from_poland(ean):
            print("Article manufactured in Poland")
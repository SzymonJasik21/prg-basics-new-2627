def get_swift_info(swift):
    # Bank Code to pierwsze 4 znaki (indeksy od 0 do 3)
    bank_code = swift[0:4]
    
    # Country Code to kolejne 2 znaki (indeksy od 4 do 5)
    country_code = swift[4:6]
    
    return bank_code, country_code

if __name__ == "__main__":
    # Kody SWIFT podane do sprawdzenia w zadaniu
    swift_codes = ["BPKOPLPW", "CHASUS33", "DEUTDEFF"]
    
    for swift in swift_codes:
        bank_code, country_code = get_swift_info(swift)
        print(f"SWIFT: {swift}")
        print(f"Bank Code: {bank_code}")
        print(f"Country Code: {country_code}")
        print("-" * 20)
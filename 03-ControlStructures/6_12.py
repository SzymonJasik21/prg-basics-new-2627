def calculate_total(amount, price):
    if amount <= 2:
        return amount * price
    return (2 * price) + ((amount - 2) * price * 0.75)

if __name__ == "__main__":
    amount = 5
    price = 40
    total = calculate_total(amount, price)
    
    print(f"Number of products purchased: {amount}")
    print(f"Product price: {price}")
    print(f"Amount to pay: {total:.2f}")
def get_reduction_percentage(current_price, previous_price):
    return ((previous_price - current_price) / previous_price) * 100

if __name__ == "__main__":
    curr = 140.00
    prev = 200.00
    reduction = get_reduction_percentage(curr, prev)
    
    print(f"Current product price: {curr:.2f}")
    print(f"Previous product price: {prev:.2f}")
    
    if reduction >= 10:
        print("Buy the product!!")
        print(f"Product price reduced by {int(reduction)}%")
def process_payment(total_payment):
    # Początkowy stan konta zgodnie z treścią zadania
    account_balance = 500
    
    # Sprawdzenie, czy kwota do zapłaty jest mniejsza lub równa stanowi konta
    if total_payment <= account_balance:
        return True
    else:
        return False

# --- BLOK TESTUJĄCY ---
if __name__ == "__main__":
    # Lista kwot do przetestowania
    test_payments = [140, 499, 500, 501, 720]
    
    for payment in test_payments:
        print(f"Total payment: {payment}")
        
        # Wywołanie funkcji i przypisanie wyniku do zmiennej
        is_successful = process_payment(payment)
        
        # Wyświetlenie odpowiedniego komunikatu na podstawie zwróconej wartości
        if is_successful:
            print('Payment completed')
        else:
            print('No funds')
            
        print("-" * 20)
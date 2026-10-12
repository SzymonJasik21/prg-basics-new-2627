   #23% VAT was paid from an amount. Write a program that reads an amount from the keyboard. Then, it calculates and prints both the amount and its VAT. Apply formatting with two decimal places. Sample result:

amount = float(input('Enter product price: '))
vat = amount * 0.23

print(f'Amount  : {amount:.2f}')
print(f'VAT 23% : {vat:.2f}')
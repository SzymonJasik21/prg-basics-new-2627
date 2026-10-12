 #The price of the product on the price tag is given before and after the discount is applied. Write a program that allows you to enter the product price and discount. Print the product price, discount, discounted product price, and the difference between the product price before and after the discount. Print all prices with two decimal places. Sample result:

 #Enter price: 24.72
 #Enter discount %: 15
 #Price with discount: 21.01
 #Reduction: 3.71

amount = float(input('Enter product price: '))
discount = float(input('Enter discount %: '))

discount_amount = amount * (discount / 100)
final_price = amount - discount_amount

print(f'Price with discount: {final_price:.2f}')
print(f'Reduction: {discount_amount:.2f}')

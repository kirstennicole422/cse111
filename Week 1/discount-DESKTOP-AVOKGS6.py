from datetime import datetime


price = float(input("Please enter the price: "))
subtotal = 0
# quantity = input("please enter the quantity:")
# subtotal = price * quantity
# print(f"The subtotal is: {subtotal}")

while price != 0:
    quantity = int(input("please enter the quantity: "))
    subtotal += (price * quantity)
    print(f"The subtotal is: ${subtotal:.2f}")
    price = float(input("Please enter the price: "))


# subtotal = float(input("Please enter the subtotal: "))
discount = 0

date_and_time = datetime.now()
# print(date_and_time)
day = date_and_time.weekday()
# print(day)

    
# day = datetime.weekday()
if (day == 1 or day == 2) and subtotal >= 50:
    discount = 0.1 * subtotal
    subtotal = subtotal - discount
    sales_tax = 0.06 * subtotal
    total = subtotal + sales_tax
    print(f"Discount amount: {discount:.2f}")
    print(f"Sales tax amount: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
elif (day == 1 or day == 2) and subtotal < 50:
    amount_to_discount = 50 - subtotal
    print(f"Spend {amount_to_discount:.2f} more to receive a 10% discount,")
else:
    sales_tax = 0.06 * subtotal
    total = subtotal + sales_tax
    print(f"Sales tax amount: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
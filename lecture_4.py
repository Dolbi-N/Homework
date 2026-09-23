# ######################
# Task 1: Smart Movie Theater Ticket Pricing
# ######################

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age entered.")
elif age < 5:
    print("Your ticket price is $0.")
elif age <= 12:
    print("Your ticket price is $8.")
elif age <= 64:
    print("Your ticket price is $15.")
else:
    print("Your ticket price is $10.")


# ##########################
# Task 2: E-Commerce Discount & Free Shipping
# ##########################

cart_total = 40.0
is_vip = True
is_guest = False
promo_code = "SAVE10"

if cart_total >= 50 or is_vip:
    print("Free Shipping!")
else:
    print("Shipping is not free.")

if promo_code and not is_guest:
    discount = cart_total * 0.10
    final_total = cart_total - discount
    print("10% discount applied!")
    print("Final total:", final_total)
else:
    final_total = cart_total
    print("No discount applied.")
    print("Final total:", final_total)


# ##########################
# Task 3: Smart ATM Cash Withdrawal
# ##########################

correct_pin = 5599
balance = 750.50

entered_pin = int(input("Enter your PIN: "))

if entered_pin == correct_pin:
    requested_amount = int(input("Enter withdrawal amount: "))

    if requested_amount <= balance:
        balance = balance - requested_amount
        print("Withdrawal successful! Remaining balance:", balance)
    else:
        print("Amount of your balance isn't enough.")
else:
    print("Incorrect PIN. Access Denied.")

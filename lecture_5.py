# ###################
# Task 01   “Secret PIN Code”
# ###################


correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. Remaining attempts: {attempts}")

if attempts == 0:
    print("Card blocked!")


# ###################
# Task 02  “Sum of Even Numbers”
# ###################

n = int(input("Enter a positive integer: "))

total = 0

for number in range(2, n + 1, 2):
    total += number

print(f"The sum of even numbers from 1 to {n} is: {total}")


# ########################
# Task 03  “Text Filter — Skip Digits”
# ########################

text = input("Enter a text: ")

for char in text:
    if char.isdigit():
        continue
    print(char, end="")


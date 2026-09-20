# ###################
# Variables_and_types
# #######################

customer_name = 'Natia'
customer_age = 15
customer_balance = 10.3
is_active = True

print(customer_name)
print(type(customer_name))

print(customer_age)
print(type(customer_age))

print(customer_balance)
print(type(customer_balance))

print(is_active)
print(type(is_active))

# ########################
# input_converter
# ########################

birth_year = int(input('Enter Your Birth Year:'))

age = 2026 - birth_year

print('Your age is:', age)


# ###################
# bool_practice
# ###################

number = int(input("Enter a number: "))

print("Positive:", number > 0)
print("Negative:", number < 0)
print("Zero:", number == 0)

print("Even:", number % 2 == 0)
print("Odd:", number % 2 != 0)

# #####################
# Task1
# #####################

first_name = input("First name: ")
last_name = input("Last name: ")

first_name = first_name.strip().capitalize()
last_name = last_name.strip().capitalize()
print(first_name, last_name)

# ###################
# Task2
# ###################

text = "My favorite thing is Python"

new_text = text.replace("thing", "language")
print(new_text)

python_index = text.find("Python")
print(python_index)

print(text[12:])

# ##################
# Task3
# ##################

name = input("Enter your name: ")
company = input("Enter your company: ")

print(f"Hello {name}, your workspace is {company}.")
try:
    birth_year = int(input("Enter your birth year: "))
    age = 2026 - birth_year
    print(age)
except ValueError:
    print("Please enter only digits!")



try:
    password = input("Enter a password: ")

    if len(password) < 6:
        raise ValueError("Password is too short!")

    print("Password accepted.")
except ValueError as e:
    print(e)

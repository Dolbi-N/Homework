# ########################
# Task1
# ########################

class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0

    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price

        MovieTicket.total_tickets_sold += 1

ticket1 = MovieTicket("Odyssey", "A1", 25)
ticket2 = MovieTicket("Avatar", "B5", 30)
ticket3 = MovieTicket("Interstellar", "C3", 35)


print("Ticket 1:")
print("Cinema:", ticket1.cinema_name)
print("Movie:", ticket1.movie_title)
print("Seat:", ticket1.seat_number)
print("Price:", ticket1.price, "GEL")

print("\nTicket 2:")
print("Cinema:", ticket2.cinema_name)
print("Movie:", ticket2.movie_title)
print("Seat:", ticket2.seat_number)
print("Price:", ticket2.price, "GEL")

print("\nTicket 3:")
print("Cinema:", ticket3.cinema_name)
print("Movie:", ticket3.movie_title)
print("Seat:", ticket3.seat_number)
print("Price:", ticket3.price, "GEL")


print("\nTotal tickets sold:", MovieTicket.total_tickets_sold)


# #######################
# Task2
# #######################

class User:
    status = "Active"

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def get_info(self):
        print("Username:", self.username)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Status:", self.status)


user1 = User("Natia", "natiadolb99@gmail.com", 31)
user2 = User("Anano", "Anano_1234@gmail.com", 30)

user1.get_info()
print()

user2.get_info()
print()

print("User 1 status:", user1.status)
print("User 2 status:", user2.status)


# ###################
# Task3
# ###################

class Product:
    shop_name = "MegaShop"

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, quantity):
        self.stock -= quantity
        print(f"Sold {quantity} {self.name}, remaining: {self.stock}")


product1 = Product("Laptop", 2700, 15)

# Print product information
print("Shop:", product1.shop_name)
print("Product:", product1.name)
print("Price:", product1.price)
print("Stock before sale:", product1.stock)

product1.sell(3)

print("Stock after sale:", product1.stock)
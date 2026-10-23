
# ##################
# Task1
# ##################

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Salary cannot be negative!")

    @salary.deleter
    def salary(self):
        del self.__salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")


manager1 = Manager("Natia", 4000, "IT")

manager1.get_info()


manager1.salary = 7000
print("Updated salary:", manager1.salary)

try:
    print(manager1.__salary)
except AttributeError:
    print("Direct access is not allowed!")



# ###############
# Task2
# ###############

class Payment:
    def process_payment(self, amount):
        print("Processing payment...")


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid by credit card: {amount} GEL")


class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid with PayPal: {amount} GEL")


payment1 = CreditCardPayment()
payment2 = PayPalPayment()

payment1.process_payment(200)
payment2.process_payment(300)


# ##################
# Task3
# ##################

class SmartDevice:
    def __init__(self, brand):
        self.brand = brand
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True
        print(f"{self.brand} device is ON")

    def turn_off(self):
        self.__is_on = False
        print(f"{self.brand} device is OFF")


class SmartLight(SmartDevice):
    def __init__(self, brand, brightness):
        super().__init__(brand)
        self.brightness = brightness

    def turn_on(self):
        super().turn_on()
        print(f"Brand: {self.brand}")
        print(f"Brightness: {self.brightness}%")

    def get_status(self):
        return self._SmartDevice__is_on


light1 = SmartLight("HP", 80)

light1.turn_on()

print("Device status:", light1.get_status())
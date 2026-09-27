class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        return self.price * self.quantity


class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self, total):
        return self.amount >= total


class Order:
    def __init__(self):
        self.products = []
        self.payment = None

    def add_product(self, product):
        self.products.append(product)

    def set_payment(self, payment):
        self.payment = payment

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.subtotal()
        return total

    def display(self):
        for product in self.products:
            print("Product:", product.name)
            print("Price:", product.price)
            print("Quantity:", product.quantity)
            print("Subtotal:", product.subtotal())
            print()

        total = self.calculate_total()
        print("Total Order Amount:", total)

        if self.payment.process(total):
            print("Payment: Successful")
        else:
            print("Payment: Failed")


order = Order()

p1 = Product("Laptop", 50000, 1)
p2 = Product("Mouse", 1000, 2)

order.add_product(p1)
order.add_product(p2)

payment = Payment(52000)
order.set_payment(payment)

order.display()
class LoginMixin:
    def login(self, username, password):
        if username == "admin" and password == "1234":
            print("Login Successful")
            return True
        else:
            print("Invalid Username or Password")
            return False


class Admin(LoginMixin):
    def show(self):
        print("Welcome Admin")


class Customer(LoginMixin):
    def show(self):
        print("Welcome Customer")


username = input("Enter Username: ")
password = input("Enter Password: ")
user_type = input("Enter User Type (Admin/Customer): ")

if user_type.lower() == "admin":
    user = Admin()
elif user_type.lower() == "customer":
    user = Customer()
else:
    print("Invalid User Type")
    exit()

if user.login(username, password):
    user.show()
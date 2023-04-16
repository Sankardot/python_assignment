You have to design a Food Ordering app for a restaurant
The application will have a log-in for admin and users to log-in
-------------------------------- Admin ----------------------------------

➡️ Admin will have the following functionalities: ⬅️

👉 1. Add new food items. Food Item will have the following details:
        🔴 FoodID //It should be generated automatically by the application.
        🔴 Name
        🔴 Quantity. For eg, 100ml, 250gm, 4pieces etc
        🔴 Price
        🔴 Discount
        🔴 Stock. Amount left in stock in the restaurant.

👉 2. Edit food items using FoodID.

👉 3. View the list of all food items.

👉 4. Remove a food item from the menu using FoodID.
--------------------------------- User ----------------------------------

➡️ The user will have the following functionalities: ⬅️

👉 1. Register on the application. Following to be entered for registration:
        🔴 Full Name
        🔴 Phone Number
        🔴 Email
        🔴 Address
        🔴 Password

👉 2. Log in to the application

👉 3. The user will see 3 options:
        🔴 Place New Order
        🔴 Order History
        🔴 Update Profile

👉 4. Place New Order: The user can place a new order at the restaurant.
        🔵 Show list of food. The list item should as follows:
            🔴 Tandoori Chicken (4 pieces) [INR 240]
            🔴 Vegan Burger (1 Piece) [INR 320]
            🔴 Truffle Cake (500gm) [INR 900]

👉 5. Users should be able to select food by entering an array of numbers. For example, if the user wants to order Vegan Burger and Truffle Cake they should enter [2, 3]

👉 6. Once the items are selected user should see the list of all the items selected. The user will also get an option to place an order.

👉 7. Order History should show a list of all the previous orders

👉 8. Update Profile: the user should be able to update their profile.

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

class Admin:
    def __init__(self):
        self.users = []

    def register_user(self, full_name, phone_number, email, address, password):
        user = User(full_name, phone_number, email, address, password)
        self.users.append(user)

    def login_user(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None  

    def show_menu(self):
        print("Menu:")
        print("1. Tandoori Chicken (4 pieces) [INR 240]")
        print("2. Vegan Burger (1 Piece) [INR 320]")
        print("3. Truffle Cake (500gm) [INR 900]")

    def place_order(self, user, item_numbers):
        items = []
        for number in item_numbers:
            if number == 1:
                items.append("Tandoori Chicken (4 pieces) [INR 240]")
            elif number == 2:
                items.append("Vegan Burger (1 Piece) [INR 320]")
            elif number == 3:
                items.append("Truffle Cake (500gm) [INR 900]")
        order = {"user": user.full_name, "items": items}
        user.orders.append(order)

    def view_order_history(self, user):
        print("Order History:")
        for index, order in enumerate(user.orders):
            print(f"{index + 1}. {order['user']}: {', '.join(order['items'])}")

    def update_profile(self, user, full_name, phone_number, email, address, password):
        user.full_name = full_name
        user.phone_number = phone_number
        user.email = email
        user.address = address
        user.password = password

restaurant = Admin()

restaurant.register_user("sankar narayana", "1234567890", "sankarnarayana40gmail.com", "123 Main St, Anytown, INDIA", "password9663")

user = restaurant.login_user("sankarnarayana40gmail.com", "password9663")

restaurant.show_menu()

restaurant.place_order(user, [2, 3])

restaurant.view_order_history(user)

restaurant.update_profile(user, "sankar narayana", "0987654321", "sankarnarayana40gmail.com", "456 Second St, Othertown, INDIA", "newpassword123")

#Output:
#1. Tandoori Chicken (4 pieces) [INR 240]
#. Vegan Burger (1 Piece) [INR 320]
#3. Truffle Cake (500gm) [INR 900]
#Order History:
#1. sankar narayana : Vegan Burger (1 Piece) [INR 320], Truffle Cake (500gm) [INR 900]

class MenuItem:
    def __init__(self, code, name, quantity, price):
        self.code = code
        self.name = name
        self.quantity = quantity
        self.price = price

class Restaurant:
    def __init__(self):
        self.menu = []
        self.orders = []

    def add_item_to_menu(self, code, name, quantity, price):
        item = MenuItem(code, name, quantity, price)
        self.menu.append(item)

    def display_menu(self):
        print("\nMenu:")
        print("Code  Name                   Quantity   Price")
        for item in self.menu:
            print(f"{item.code}     {item.name:20} {item.quantity:5}      {item.price}")

    def place_order(self, items):
        order_total = 0
        for code, quantity in items.items():
            item = next((x for x in self.menu if x.code == code), None)
            if item is None:
                print(f"Invalid item code: {code}")
                return
            if item.quantity < quantity:
                print(f"Insufficient quantity for item: {item.name}")
                return
            order_total += quantity * item.price
        self.orders.append((items, order_total))
        for code, quantity in items.items():
            item = next((x for x in self.menu if x.code == code), None)
            item.quantity -= quantity
        print(f"Order placed successfully. Total: {order_total}")

    def display_orders(self):
        print("\nOrders:")
        for order in self.orders:
            items, order_total = order
            print(f"Items: {items}  Total: {order_total}")

# Sample usage
restaurant = Restaurant()

restaurant.add_item_to_menu("001", "Burger", 10, 5.99)
restaurant.add_item_to_menu("002", "Pizza", 5, 9.99)
restaurant.add_item_to_menu("003", "Fries", 20, 2.99)
restaurant.add_item_to_menu("004", "Hot Dog", 8, 3.99)
restaurant.add_item_to_menu("005", "Soda", 30, 1.99)

restaurant.display_menu()

restaurant.place_order({"001": 2, "003": 3, "005": 1})
restaurant.place_order({"001": 1, "002": 2, "003": 1})
restaurant.display_orders()
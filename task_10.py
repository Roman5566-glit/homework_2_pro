def create_product(name, price, quantity):
    """Creates product and allows price modification"""
    def change_price(new_price):
        """Changes product price"""
        nonlocal price
        price = new_price
        print(f"Нова ціна для {name}: {price}")

    def show_product():
        """Shows product info"""
        print(name, price, quantity)

    return change_price, show_product


change_price, show = create_product("Laptop", 1000, 5)

show()

change_price(900)

show()

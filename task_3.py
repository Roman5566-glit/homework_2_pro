discount = 0.1


def create_order(price):
    """Creates order and calculates price with discount"""
    final_price = price - price * discount

    print("Ціна після основної знижки:", final_price)

    def apply_additional_discount():
        """Additional VIP discount"""
        nonlocal final_price
        final_price = final_price - final_price * 0.05

    apply_additional_discount()

    print("Фінальна ціна:", final_price)


create_order(1000)

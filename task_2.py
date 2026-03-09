subscribers = []


def subscribe(name):
    """Adds a new subscriber"""
    subscribers.append(name)

    def confirm_subscription():
        """Confirms subscription"""
        return f"Підписка підтверджена для {name}"

    print(confirm_subscription())


def unsubscribe(name):
    """Removes subscriber from the list."""
    if name in subscribers:
        subscribers.remove(name)
        return f"{name} успішно відписаний"
    else:
        return "Користувача не знайдено"


subscribe("Олена")
subscribe("Ігор")

print(subscribers)

print(unsubscribe("Ігор"))

print(subscribers)

total_expense = 0


def add_expense(amount):
    """Adds expense to total"""
    global total_expense
    total_expense += amount


def get_expense():
    """Returns total expenses"""
    return total_expense


add_expense(100)
add_expense(250)

print("Загальні витрати:", get_expense())

def my_sum(*args):
    """ Custom function that imitates overriding built-in sum. It only prints a message"""
    print("This is my custom sum function!")


my_sum(1, 5, 8)

numbers = [1, 2, 3, 4, 5]

results = sum(numbers)

print("Sum of numbers:", results)

def create_calculator(operator):
    """Returns calculator function based on operator"""

    def calculate(a, b):
        """Performs calculation"""
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b

    return calculate


add = create_calculator("+")
sub = create_calculator("-")

print(add(5, 3))
print(sub(10, 4))

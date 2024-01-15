"""module contains a calculator class"""


class Calculator:
    """creates an instance of a calculator"""
    def add(self, x, y):
        """adds arguments x, y"""
        return x + y

    def subtract(self, x, y):
        """subtract arguments x, y"""
        return x - y

    def multiply(self, x, y):
        """multiply arguments x, y"""
        return x * y

    def divide(self, x, y):
        """divides arguments x, y"""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

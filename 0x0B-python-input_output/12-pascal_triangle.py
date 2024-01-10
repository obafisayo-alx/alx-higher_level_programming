#!/usr/bin/python3
"""pascals Triangle"""


def pascal_triangle(n):
    """creates a pascal triangle with n rows"""
    triangle = []
    prow = []
    for i in range(n):
        crow = [1] + [sum(prow[el:el + 2]) for el in range(len(prow - 1))]
        if i > 0:
            crow = crow + [1]
        triangle.append(crow)
        prow = crow
    return triangle

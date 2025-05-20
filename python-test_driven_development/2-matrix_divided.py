#!/usr/bin/python3
"""
Module that contains the matrix_divided function to divide all elements
of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or rows are not all the same size,
                   or div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists of floats: New matrix with divided elements
    """
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix) or
            any(
                not all(isinstance(el, (int, float)) for el in row)
                for row in matrix
            )):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0]) if matrix else 0
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(el / div, 2) for el in row]
        new_matrix.append(new_row)

    return new_matrix

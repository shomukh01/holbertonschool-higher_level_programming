#!/usr/bin/python3
"""This module multiplies two matrices.

It validates that both matrices are lists of lists.
It also checks empty matrices, element types, rectangular shape,
and whether the matrices can be multiplied.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices after validating all requirements.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Returns:
        A new matrix containing the product of m_a and m_b.
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(type(row) is list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(type(num) in (int, float) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(type(num) in (int, float) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    row_size = len(m_a[0])
    if not all(len(row) == row_size for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_size = len(m_b[0])
    if not all(len(row) == row_size for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for row_a in m_a:
        new_row = []
        for col in range(len(m_b[0])):
            total = 0
            for i in range(len(m_b)):
                total += row_a[i] * m_b[i][col]
            new_row.append(total)
        result.append(new_row)

    return result

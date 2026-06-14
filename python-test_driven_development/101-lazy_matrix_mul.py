#!/usr/bin/python3
"""Module that provides lazy matrix multiplication using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy."""

    if type(m_a) is str or type(m_b) is str:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    return np.dot(m_a, m_b)

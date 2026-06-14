#!/usr/bin/python3
"""Module that provides lazy matrix multiplication using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy."""

    if type(m_a) is str or type(m_b) is str:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    try:
        return np.dot(m_a, m_b)
    except Exception as e:
        msg = str(e)
        if "data type must provide an itemsize" in msg:
            raise TypeError("invalid data type for einsum")
        if "setting an array element with a sequence" in msg:
            raise ValueError("setting an array element with a sequence.")
        raise

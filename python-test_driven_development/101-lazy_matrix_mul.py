#!/usr/bin/python3
"""Module that provides lazy matrix multiplication using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy."""

    return np.array(m_a).dot(np.array(m_b))

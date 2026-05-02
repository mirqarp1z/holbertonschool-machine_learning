#!/usr/bin/env python3
"""Module for calculating the cofactor matrix of a matrix."""
minor = __import__('1-minor').minor


def cofactor(matrix):
    """Calculate the cofactor matrix of a matrix.

    Args:
        matrix: a list of lists whose cofactor matrix should be calculated.

    Returns:
        The cofactor matrix of matrix.

    Raises:
        TypeError: if matrix is not a list of lists.
        ValueError: if matrix is not a non-empty square matrix.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    if matrix == [[]] or len(matrix) == 0:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")

    minors = minor(matrix)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(((-1) ** (i + j)) * minors[i][j])
        result.append(row)
    return result

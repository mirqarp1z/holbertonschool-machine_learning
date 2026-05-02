#!/usr/bin/env python3
"""Module for calculating the minor matrix of a matrix."""
determinant = __import__('0-determinant').determinant


def minor(matrix):
    """Calculate the minor matrix of a matrix.

    Args:
        matrix: a list of lists whose minor matrix should be calculated.

    Returns:
        The minor matrix of matrix.

    Raises:
        TypeError: if matrix is not a list of lists.
        ValueError: if matrix is not a non-empty square matrix.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a list of lists")
    if len(matrix) == 0 or matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    result = []
    for i in range(n):
        row = []
        for j in range(n):
            sub = [
                [matrix[r][c] for c in range(n) if c != j]
                for r in range(n) if r != i
            ]
            row.append(determinant(sub))
        result.append(row)
    return result

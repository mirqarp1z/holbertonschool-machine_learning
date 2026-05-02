#!/usr/bin/env python3
"""Module for calculating the adjugate matrix of a matrix."""
cofactor = __import__('2-cofactor').cofactor


def adjugate(matrix):
    """Calculate the adjugate matrix of a matrix.

    Args:
        matrix: a list of lists whose adjugate matrix should be calculated.

    Returns:
        The adjugate matrix of matrix.

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

    cof = cofactor(matrix)
    return [[cof[j][i] for j in range(n)] for i in range(n)]

"""External excercise for lab_2."""

from typing import List

import pytest


def is_matrix_square(mat: List[List[int]]) -> bool:
    """
    Check if given matrix is a square one.

    :param mat: given matrix

    :return: true if matrix is square one, otherwise false
    """
    n_rows = len(mat)
    return all(len(row) == n_rows for row in mat)


def get_minor_matrix(mat: List[List[int]], i: int, j: int) -> List[List[int]]:
    """
    Generate a minor matrix of M for row 'i' and column 'j'.

    :param mat: matrix to obtain a minor one by crossing out the row 'i' and
        the column 'j'
    :param i: index of row
    :param j: index of column

    :return: minor matrix
    """
    
    n_rows, n_cols = len(mat), len(mat[0])
    minor = [[mat[r_i][c_i] for c_i in range(n_cols) if c_i != j] 
             for r_i in range(n_rows) if r_i != i]
    return minor 



def matrix_determinant(mat: List[List[int]]) -> int:
    """
    Compute matrix determinant using Laplace method.

    :param mat: matrix to compute determinant for

    :return: determinant
    """
    if is_matrix_square(mat):

        # base case for recursion 
        if len(mat) == 1:
            return mat[0][0]

        else:
            multiplier = 1
            r_i_cross = 0
            determinant = 0

            for c_i_cross in range(len(mat)):
                determinant += multiplier * mat[r_i_cross][c_i_cross] * matrix_determinant(get_minor_matrix(mat, r_i_cross, c_i_cross))
                multiplier *= -1
            return determinant 

    else:
        raise ValueError("Matrix is not square!: ", mat)    
    

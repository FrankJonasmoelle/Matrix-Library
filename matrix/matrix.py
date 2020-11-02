"""own implementation of a matrix class that allows the creation of matrices and matrix operations.
"""
from __future__ import annotations

from typing import Union


class Matrix(MD_Operators):


    def __init__(self, lis: list): 
        """Creates a matrix object out of a list

        Args:
            lis (list): 

        Raises:
            TypeError: Input has to be a list
        """
        if isinstance(lis, list):
            self.matrix = lis
            self.num_rows = len(lis)
            self.num_cols = len(lis[0])
        else:
            raise TypeError("Input has to be a list")

    def __str__(self) -> str:
        return "The matrix consists of {} rows and {} colums".format(self.num_rows, self.num_cols)

    def __eq__(self, other_matrix: object) -> bool:

    def is_matrix(self, matrix2) -> bool:
        # checks if self and matrix2 are matrices

    def __add__(self, matrix2: Matrix) -> Matrix:
        # check if second matrix is indeed a matrix
        if is_matrix(matrix2):
            # multiply

    def __sub__(self, matrix2: Matrix) -> Matrix:
        # check if second matrix is indeed a matrix
        if is_matrix(matrix2):
            # multiply

    def __mul__(self, other: Union[Matrix, int]) -> Matrix:
        # check if second matrix is indeed a matrix
        if is_matrix(matrix2):
            if isinstance(matrix2, int):
                # multiply by constant 
            if isinstance(matrix2, Matrix):
                # multiply by matrix 

    #def __truediv__(self, matrix2: int) -> Matrix:
        # check if second matrix is indeed a matrix
    #    return -1
    
    def create_identity(self) -> Matrix:
     
    def transpose(self) -> Matrix:

    def inverse(self) -> Matrix:

    

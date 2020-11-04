"""own implementation of a matrix class that allows the creation of matrices and matrix operations.
"""
from __future__ import annotations

from typing import Union


class Matrix():


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

    def is_matrix(self, matrix2: Matrix) -> bool:
        # checks if self and matrix2 are matrices

    def has_same_dimension(self, matrix2: Matrix) -> bool:
        # checks if self and matrix2 have same number of rows and columns

    def __add__(self, matrix2: Matrix) -> Matrix:
        
        if is_matrix(matrix2) and has_same_dimension(matrix2):
            num_rows = len(matrix2)
            num_cols = len(matrix2[0])

            my_matrix = [[self[row_idx][col_idx] + other_matrix[row_idx][col_idx] for col_idx in range(num_cols)] for row_idx in range(num_rows)]
            return my_matrix
        else: 
            raise TypeError("Input needs to be a matrix")


    def __sub__(self, matrix2: Matrix) -> Matrix:
        
        if is_matrix(matrix2) and has_same_dimension(matrix2):
            num_rows = len(matrix2)
            num_cols = len(matrix2[0])

            my_matrix = [[self[row_idx][col_idx] - other_matrix[row_idx][col_idx] for col_idx in range(num_cols)] for row_idx in range(num_rows)]
            return my_matrix
        else: 
            raise TypeError("Input needs to be a matrix")
          

    def __mul__(self, other: Union[Matrix, int]) -> Matrix:
        # multiply by constant 
         
        # multiply by matrix 

    
    def create_identity(self, size: int) -> Matrix:
        """Creates the identity matrix of a specific size

        Args:
            size (int): Specifies the size of the identity matrix, corresponding to the row and column size.

        Raises:
            ValueError: size parameter has to be specified
            ValueError: size of identity matrix has to be larger than 1

        Returns:
            Matrix: Identity matrix of specified size
        """
  
        if size is None:
            raise ValueError("Please specify the size!")

        if size < 2:
            raise ValueError("Size parameter needs to be at least larger than 2")
        
        id_matrix = [[1 if col_idx == row_idx else 0 for col_idx in range(size)] for row_idx in range(size)]
        return id_matrix
        

    def transpose(self) -> Matrix:


    def inverse(self) -> Matrix:

    

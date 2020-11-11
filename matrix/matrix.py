"""own implementation of a matrix class that allows the creation of matrices and matrix operations.
"""
from __future__ import annotations

from typing import Union


class Matrix():
    def __init__(self, lis: list): 
        """Creates a matrix object out of a list

        Args:
            lis (list): List which represents matrix 

        Raises:
            TypeError: Input has to be a list with shape of a valid matrix
        """
        if self.is_matrix(lis):
            self.matrix = lis
            self.num_rows = len(lis)
            self.num_cols = len(lis[0])
        else:
            raise TypeError("Input has to be a valid matrix")

    def __len__(self):
        """Returns the length (amount of rows) of the matrix"""
        return len(self.matrix)

    def __repr__(self):
        """Prints a visual representation of the matrix"""
        out = ""
        for row in self.matrix:
            out += str(row)
            out += "\n"
        return out


    def __str__(self) -> str:
        """Prints a visual representation of the matrix"""
        out = ""
        for row in self.matrix:
            out += str(row)
            out += "\n"
        return out


    def __eq__(self, other_matrix: Matrix) -> bool:
        """Checks whether two matrices are identical or not

        Args:
            other_matrix (Matrix): Comparison matrix

        Returns:
            bool: True if given matrix is identical, false if not
        """
        if (self.num_cols != other_matrix.num_cols) or (self.num_rows != other_matrix.num_rows):
            return False

        is_equal = True
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.matrix[i][j] != other_matrix.matrix[i][j]:
                    is_equal = False
        return is_equal


    def __add__(self, other_matrix: Matrix) -> Matrix:
     """Adds two matrices 

        Args:
            other_matrix (Matrix): Other matrix

        Raises:
            TypeError: Matrices have to be of same shape

        Returns:
            Matrix: Output matrix
        """
        if self.is_matrix(other_matrix.matrix) and self.has_same_dimension(other_matrix):
            my_matrix = [[self.matrix[row_idx][col_idx] + other_matrix.matrix[row_idx][col_idx] 
                            for col_idx in range(other_matrix.num_cols)] for row_idx in range(other_matrix.num_rows)]
            return Matrix(my_matrix)
        else: 
            raise TypeError("Input needs to be a matrix")


    def __sub__(self, other_matrix: Matrix) -> Matrix:
        """Subtract two matrices 

        Args:
            other_matrix (Matrix): Other matrix

        Raises:
            TypeError: Matrices have to be of same shape

        Returns:
            Matrix: Output matrix
        """
        if self.is_matrix(other_matrix.matrix) and self.has_same_dimension(other_matrix):
            my_matrix = [[self.matrix[row_idx][col_idx] - other_matrix.matrix[row_idx][col_idx] 
                        for col_idx in range(other_matrix.num_cols)] 
                        for row_idx in range(other_matrix.num_rows)]
            return Matrix(my_matrix)
        else: 
            raise TypeError("Input needs to be a matrix of same shape")
          

    def __mul__(self, other: Union[Matrix, int]) -> Matrix:
        """Implements matrix multiplications and multiplication by scalar

        Args:
            other (Union[Matrix, int]): Either a matrix or an integer input

        Raises:
            ValueError: "Shape" of matrices has to fit in order to multiply them
            TypeError: Input has to be a matrix or a scalar

        Returns:
            Matrix: Output matrix after multiplication
        """
        if isinstance(other, int):
            # perform scalar multiplication
            new_matrix = [[self.matrix[row_idx][col_idx] * other for col_idx in range(self.num_cols)] 
                            for row_idx in range(self.num_rows)]
            return Matrix(new_matrix)

        if self.is_matrix(other.matrix):
            # perform matrix multiplication
            n_self = self.num_cols
            n_other = other.num_rows
        
            if n_self != n_other:
                raise ValueError("Cannot multiply matrices of this shape")

            output_matrix = self.create_matrix_of_shape(num_rows=self.num_rows, num_cols=other.num_cols) 
            
            for i in range(self.num_rows):
                for j in range(other.num_cols):
                    for k in range(other.num_rows):
                        output_matrix.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return output_matrix
        else:
            raise TypeError("Input needs to either be a matrix, or a scalar")

    @staticmethod
    def is_matrix(lis: list) -> bool:
        """Checks whether an input list is a matrix or not. 

        The fallowing requirements have to be fullfilled:
        1) Dimension has to be 2
        2) Length of every inner list (len(mat[0...i])) is the same
        3) Each element has to be an int 

        Args:
            lis (list): lis gets checked whether it is a matrix or not

        Returns:
            bool: True if lis is a matrix, False if not
        """
        is_a_matrix = True
        # 1) check if list is 2 dimensional
        if not isinstance(lis[0], list) and not isinstance(lis[0][0], int):
            is_a_matrix = False

        # 2) check if length of inner lists is equal (the column size is equal for all rows)
        length_inner_list = len(lis[0])

        for i in range(len(lis)):
            if len(lis[i]) != length_inner_list:
                is_a_matrix = False

        # 3) Each element has to be an integer 
        for i in range(len(lis)):
            for j in range(len(lis[i])):
                if not isinstance(lis[i][j], int):
                    is_a_matrix = False

        return is_a_matrix


    def has_same_dimension(self, matrix2: Matrix) -> bool:
        """checks if self and matrix2 have same number of rows and columns

        Args:
            matrix2 (Matrix): Other matrix

        Returns:
            bool: True if both matrices have same dimension, False otherwise
        """
        if len(self.matrix[0]) == len(matrix2.matrix[0]) and len(self.matrix) == len(matrix2.matrix):
            return True
        else: 
            return False
         
    @staticmethod
    def create_matrix_of_shape(num_rows: int, num_cols: int) -> Matrix:
        """Creates a matrix of 0's with a specified number of rows and columns

        Args:
            num_rows (int): Number of rows
            num_cols (int): Number of columns

        Raises:
            ValueError: Both parameters have to be specified
            ValueError: Both parameters need to be larger than 0

        Returns:
            Matrix: Matrix of 0's of specified size
        """
        if num_rows is None or num_cols is None:
            raise ValueError("Needs num_rows and num_cols as input")

        if num_rows < 1 or num_cols < 1:
            raise ValueError("num_rows and num_cols has to be larger than 0")

        new_matrix = [[0 for col_idx in range(num_cols)] for row_idx in range(num_rows)]
        return Matrix(new_matrix)

    @staticmethod
    def create_identity(size: int) -> Matrix:
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
        return Matrix(id_matrix)
        

    def transpose(self) -> Matrix:
        """Transposes the given matrix

        Returns:
            Matrix: Transposed matrix
        """
        transposed_matrix = self.create_matrix_of_shape(num_rows=self.num_cols, num_cols=self.num_rows)

        for i in range(transposed_matrix.num_rows):
            for j in range(transposed_matrix.num_cols):
                transposed_matrix.matrix[i][j] = self.matrix[j][i]
        return transposed_matrix

    def is_symmetric(self) -> bool:
        """Checks whether the given matrix is symmetric or not

        Returns:
            bool: True if matrix is symmetric, otherwise False
        """
        if self.num_cols != self.num_rows:
            return False
        else:
            is_symm = True
            for row in range(self.num_rows):
                for col in range(self.num_cols):
                    if self.matrix[row][col] != self.matrix[col][row]:
                        is_symm = False
            return is_symm    


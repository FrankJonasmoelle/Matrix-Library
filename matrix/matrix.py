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
        if self.is_matrix(lis):
            self.matrix = lis
            self.num_rows = len(lis)
            self.num_cols = len(lis[0])
        else:
            raise TypeError("Input has to be a valid matrix")

    def __len__(self):
        return len(self.matrix)

    def __repr__(self):
        return "The matrix consists of {} rows and {} colums".format(self.num_rows, self.num_cols)


    def __str__(self) -> str:
        for row in self.matrix:
            print(row)


    def __eq__(self, other_matrix: Matrix) -> bool:
        """Checks whether two matrices are identical or not

        Args:
            other_matrix (Matrix): Comparison matrix

        Returns:
            bool: True if given matrix is identical, false if not
        """
        is_equal = True
        for i in range(len(self)):
            for j in range(len(self[0])):
                if self[i][j] != other_matrix[i][j]:
                    is_equal = False
        return is_equal

    def __getitem__(self):


    def __setitem__(self):
        


    def __add__(self, other_matrix: Matrix) -> Matrix:
        
        if self.is_matrix(other_matrix) and self.has_same_dimension(other_matrix):
            num_rows = len(other_matrix)
            num_cols = len(other_matrix[0])

            my_matrix = [[self[row_idx][col_idx] + other_matrix[row_idx][col_idx] for col_idx in range(num_cols)] for row_idx in range(num_rows)]
            return my_matrix
        else: 
            raise TypeError("Input needs to be a matrix")


    def __sub__(self, other_matrix: Matrix) -> Matrix:
        
        if self.is_matrix(other_matrix) and self.has_same_dimension(other_matrix):
            num_rows = len(other_matrix)
            num_cols = len(other_matrix[0])

            my_matrix = [[self[row_idx][col_idx] - other_matrix[row_idx][col_idx] for col_idx in range(num_cols)] 
                            for row_idx in range(num_rows)]
            return my_matrix
        else: 
            raise TypeError("Input needs to be a matrix")
          

    def __mul__(self, other: Union[Matrix, int]) -> Matrix:
        """Implements matrix multiplications

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
            num_rows = len(self)
            num_cols = len(self[0])

            new_matrix = [[self[row_idx][col_idx] * other for col_idx in range(num_cols)] for row_idx in range(num_rows)]
            return new_matrix

        if self.is_matrix(other):
            # perform matrix multiplication
            n_self = len(self[0])
            n_other = len(other)
        
            if n_self != n_other:
                raise ValueError("Cannot multiply matrices of this shape")

            output_matrix = self.create_matrix_of_shape(num_rows=len(self), num_cols=len(other[0])) 
            
            for i in range(len(self)):
                for j in range(len(other[0])):
                    for k in range(len(other)):
                        output_matrix[i][j] += self[i][k] * other[k][j]
            return output_matrix
        else:
            raise TypeError("Input needs to either be a matrix, or a scalar")

    def is_matrix(self, lis: list) -> bool:
        """Checks whether an input list is a matrix, or not. 

        Args:
            lis (list): lis gets checked whether it is a matrix or not

        Returns:
            bool: True if lis is a matrix, False if not
        """
        # 1) Dimension has to be 2
        # 2) Length of every inner list (len(mat[0...i])) is the same
        # 3) Each element has to be an int 
        is_a_matrix = True

        # 1) check if list is 2d
        if not isinstance(lis[0], list) and not isinstance(lis[0][0], int):
            is_a_matrix = False

        # 2) check if length of inner lists is equal (the column size is equal for all rows)
        length_inner_list = len(lis[0])

        for i in range(len(lis)):
            if len(lis[i]) != length_inner_list:
                is_a_matrix = False

        # 3) Each element has to be an int 
        for i in range(len(lis)):
            for j in range(len(lis[i])):
                if not isinstance(lis[i][j], int):
                    is_a_matrix = False

        return is_a_matrix


    def has_same_dimension(self, matrix2: Matrix) -> bool:
        # checks if self and matrix2 have same number of rows and columns
        if len(self[0]) == len(matrix2[0]) and len(self) == len(matrix2):
            return True
        else: 
            return False
         
    def create_matrix_of_shape(self, num_rows: int, num_cols: int) -> Matrix:
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
        return new_matrix


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
        """Returns transpose of the matrix

        Returns:
            Matrix: Transposed matrix
        """
        n_rows = len(self)
        n_cols = len(self[0])
        # define matrix with swapped shape
        transposed_matrix = self.create_matrix_of_shape(num_rows=n_cols, num_cols=n_rows)

        for i in range(len(transposed_matrix)):
            for j in range(len(transposed_matrix[0])):
                transposed_matrix[i][j] = self[j][i]
        return transposed_matrix

    #def inverse(self) -> Matrix:

    
    #def determinant(self) -> int:


    def is_symmetric(self) -> bool:
        is_symm = True
        for row in range(len(self)):
            for col in range(len(self[0])):
                if self[row][col] != self[col][row]:
                    is_symm = False
        return is_symm    


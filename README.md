# Matrix-Library
This library implements matrix operations without using the NumPy library. 
It provides a direct interface between python lists and matrix operations. 

### Purpose
This is a training for setting up a whole python project myself. 
Further, I wanted to train the python technologies listed below. 

### Technologies used
* Type Annotations
* Tests with PyTest
* Error Handling
* Logging
* Sphinx Documentation

### Supported Operations
* Matrix addition
* Matrix subtraction
* Matrix multiplication
* Check if list is matrix
* Create matrix of specific shape
* Create identity matrix
* Transpose a matrix
* Check for symmetry

### Usage
```Python
from matrix import *
# create new matrices 
m1 = Matrix([[1,2,3], [4,5,6]])
m2 = Matrix([[1,1,1], [1,1,1]])
m3 = Matrix([[1,2], [4,5], [6,7]])
```
Basic matrix operations
```Python
# add
out1 = m1 + m2
print(out1)
# subtract
out2 = m1 - m2
print(out2)
# multiply
out3 = m1 * 3
print(out3)
out4 = m1 * m3
print(out4)
```
Further useful operations
```Python
# empty matrix with 4 rows, 3 columns
empty_matrix = Matrix.create_matrix_of_shape(4,3)
print(empty_matrix)
# identiy matrix of size 3
identity = Matrix.create_identity(3)
print(identity)
# check for symmetry
m1.is_symmetric()
# transpose
transpose = m1.transpose()
print(transpose)
```
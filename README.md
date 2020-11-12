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

# create a new matrix
m1 = Matrix([[1,2,3], [4,5,6]])
print(m1)
print(m1.num_cols)
print(m1.num_rows)
```


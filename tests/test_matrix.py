import pytest

from matrix.matrix import *


@pytest.fixture
def dummy_matrix_1():
    return Matrix([[1,2,3],[4,5,6]])

@pytest.fixture
def dummy_matrix_2():
    return Matrix([[1,1,1],[1,1,1]])

@pytest.fixture
def dummy_matrix_3():
    return Matrix([[1,2],[3,4],[5,6]])
    

def test_add(dummy_matrix_1, dummy_matrix_2):
    m1 = dummy_matrix_1
    m2 = dummy_matrix_2
    out = m1 + m2
    expected = Matrix([[2,3,4], [5,6,7]])
    assert out == expected

def test_subtract(dummy_matrix_1, dummy_matrix_2):
    m1 = dummy_matrix_1
    m2 = dummy_matrix_2
    out = m1 - m2
    expected = Matrix([[0,1,2], [3,4,5]])
    assert out == expected

def test_multiply(dummy_matrix_1, dummy_matrix_3):
    m1 = dummy_matrix_1
    m3 = dummy_matrix_3
    # matrix multiplication    
    out_1 = m1 * m3
    expected_1 = Matrix([[22, 28], [49, 64]])
    # scalar multiplication
    out_2 = m1 * 3
    expected_2 = Matrix([[3,6,9], [12, 15, 18]])
    assert out_1 == expected_1
    assert out_2 == expected_2
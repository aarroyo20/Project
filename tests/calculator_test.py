"""Testing the Calculator"""
import pytest
from calculator import Calculator

def test_calculator_add_method():
    """Testing the Calculator Addition"""
    tuple_list = (1.0, 2.0)
    result = Calculator.add(tuple_list)
    assert result == 3.0


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    tuple_list = (1.0, 2.0)
    assert Calculator.subtract(tuple_list) == -1.0


def test_calculator_multiply_method():
    """Testing the Calculator Multiply"""
    tuple_list = (1.0, 2.0)
    assert Calculator.multiply(tuple_list) == 2.0


def test_calculator_divide_method():
    """A calculator divide test"""
    tuple_list = (1.0, 2.0)
    result = Calculator.divide(tuple_list)
    assert result == 0.5


def test_calculator_division_exception():
    """A calculator division exception test"""
    tuple_list = (1.0, 0.0)
    with pytest.raises(ZeroDivisionError):
        result = Calculator.divide(tuple_list)
        assert result is True

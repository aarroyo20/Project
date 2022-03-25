"""Testing the Calculator with AAA"""
import pytest
from calculator.calculation import Addition, Subtraction, Multiplication, Division

def test_calculation_addition_instance():
    """Testing the Calculator Addition"""
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert isinstance(calculation, Addition)


def test_calculation_subtraction_instance():
    """Testing the Calculator Subtract"""
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    assert isinstance(calculation, Subtraction)


def test_calculation_multiplication_instance():
    """Testing the Calculator Multiply"""
    tuple_list = (1, 2)
    calculation = Multiplication.create(tuple_list)
    assert isinstance(calculation, Multiplication)


def test_calculation_division_instance():
    """Testing the Calculator Multiply"""
    tuple_list = (1, 2)
    calculation = Division.create(tuple_list)
    assert isinstance(calculation, Division)


def test_calculation_add_get_result_method():
    """Testing the Calculator"""
    tuple_list = (1, 2)
    calculation = Addition.create(tuple_list)
    assert calculation.get_result() == 3


def test_calculation_subtract_get_result_method():
    """Testing the Calculator Subtract"""
    tuple_list = (1, 2)
    calculation = Subtraction.create(tuple_list)
    assert calculation.get_result() == -1


def test_calculation_multiply_get_result_method():
    """Testing the Calculator Multiplication"""
    tuple_list = (1, 2)
    calculation = Multiplication.create(tuple_list)
    assert calculation.get_result() == 2


def test_calculation_division_get_results_method():
    """Test calulation division"""
    tuple_list = (1, 2)
    calculation = Division.create(tuple_list)
    assert calculation.get_result() == 0.5


def test_calculator_division_exception():
    """Test calculator division exception"""
    tuple_list = (1.0, 0.0)
    calculation = Division.create(tuple_list)
    with pytest.raises(ZeroDivisionError):
        result = calculation.get_result()
        assert result is True

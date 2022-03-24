"""Testing the calculator operations """
from calculator.operations import Addition, Subtraction, Multiplication, Division

def test_calculator_operations_add():
    """testing addition"""
    assert Addition.add(1, 1) == 2
    assert Addition.add(10, 10) == 20

def test_calculator_operations_subtract():
    """testing subtraction"""
    assert Subtraction.subtract(8.0, 4.0) == 4.0

def test_calculator_operations_multiply():
    """testing multiplication"""
    assert Multiplication.multiply(2, 4) == 8

def test_calculator_operations_divide():
    """testing division"""
    assert Division.divide(8, 4) == 2
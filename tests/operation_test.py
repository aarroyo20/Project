"""Testing the calculator Operations """
from calculator.operations import Addition, Subtraction, Multiplication, Division
def test_calculator_operations_add():
    """testing addition"""
    assert Addition.add(1, 5) == 6
    assert Addition.add(20, 20) == 40

def test_calculator_operations_subtract():
    """testing subtraction"""
    assert Subtraction.subtract(2.0, 1.0) == 1.0

def test_calculator_operations_multiply():
    """multiplication testing"""
    assert Multiplication.multiply(2,3) == 6

def test_calculator_operations_divide():
    """division testing"""
    assert Division.divide(4, 2) == 2

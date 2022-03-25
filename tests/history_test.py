"""Testing the Calculator"""
import pytest
from calculator.history import Calculations as History
from calculator.calculation import Addition, Subtraction, Multiplication, Division

@pytest.fixture
def clear_history_fixture():
    """fixture"""

# pylint: disable=redefined-outer-name
History.clear_history()

@pytest.fixture
def setup_addition_calculation_fixture():
    """Addition"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    addition = Addition(values)
    History.add_calculation(addition)

@pytest.fixture
def setup_subtraction_calculation_fixture():
    """subtraction"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    subtraction = Subtraction(values)
    History.add_calculation(subtraction)


@pytest.fixture
def setup_multiplication_calculation_fixture():
    """multiplication"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    multiplication = Multiplication(values)
    History.add_calculation(multiplication)


@pytest.fixture
def setup_division_calculation_fixture():
    """division"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    division = Division(values)
    History.add_calculation(division)


def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    """addition history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 1


def test_subtraction_calculation_to_history(clear_history_fixture,
                                            setup_subtraction_calculation_fixture):
    """subtraction history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 2


def test_multiplication_calculation_to_history(clear_history_fixture,
                                               setup_multiplication_calculation_fixture):
    """multiplication history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 3


def test_division_calculation_to_history(clear_history_fixture, setup_division_calculation_fixture):
    """division history testing"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 4

def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """get a calculation from history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_calculation(0).get_result() == 3

def test_clear_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    """clearing history test"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 6
    History.clear_history()
    assert History.count_history() == 0
    assert History.clear_history() == True

def test_get_calc_last_result_value(clear_history_fixture, setup_addition_calculation_fixture):
    """get last calculation result value test"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_last_calculation_result_value() == 3


def test_get_calculation_first(clear_history_fixture, setup_addition_calculation_fixture):
    """get first calculation test"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_first_calculation().get_result() == 3



def test_get_calc_last_result_object(clear_history_fixture, setup_addition_calculation_fixture):
    """get last calculation from the history test"""
    # pylint: disable=unused-argument,redefined-outer-name
    # This test if it returns the last calculation as an object
    assert isinstance(History.get_last_calculation_object(), Addition)

def test_history_count(clear_history_fixture, setup_addition_calculation_fixture):
    """get history calculations count test"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.count_history() == 4

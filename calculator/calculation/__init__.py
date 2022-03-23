"""Calculation and Addition, Multiplication, and Subtraction Classes """
from calculator.operations import Addition as Add, Subtraction as Sub, Multiplication as Mult, Division as Div


class Calculation:
    """ calculation abstract base class"""

    # pylint: disable=too-few-public-methods
    def __init__(self, tuple_list: tuple):
        """ constructor method"""
        self.values = Calculation.convert_args_to_tuple_of_float(tuple_list)

    @classmethod
    def create(cls, tuple_list: tuple):
        """ factory method"""
        return cls(tuple_list)

    @staticmethod
    def convert_args_to_tuple_of_float(tuple_list):
        """ standardize values to list of floats"""
    list_values_float = []
    for i in tuple_list:
        list_values_float.append(float(i))
    return tuple(list_values_float)


class Addition(Calculation):
    """ calculation addition class"""
    def get_result(self):
        """get the addition results"""
        values_sum = 0.0
        for value in self.values:
            values_sum = Add.add(value, values_sum)
        return values_sum


class Multiplication(Calculation):
    """multiplication calculation object"""
    def get_result(self):
        """get the multiplication results"""
        result = 1.0
        for value in self.values:
            result = Mult.multiply(result, value)
        return result


class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        difference_of_values = 1.0
        for value in self.values:
            difference_of_values = Sub.subtract(difference_of_values, value)
        return difference_of_values


class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        result = 1.0
        for value in self.values:
            quotient_result = Div.divide(result, value)
        return quotient_result
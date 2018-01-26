#!/usr/bin/env python
# coding: utf-8

"""Module of strategies for random mathematical operation generation."""

import random
from pynairus.validators import operator_validator as py_ov
from pynairus.errors import app_error as err

# Constants for the keys of the dictionnary strategies.
ADD_OPERATOR_KEY = "+"
SUB_OPERATOR_KEY = "-"
MULT_TABLE_OPERATOR_KEY = "*"
SIMPLE_MULT_OPERATOR_KEY = "1*"
COMPLEX_MULT_OPERATOR_KEY = "n*"


def get_list_operator_key():
    """Return a tuple of key operator allowed with explanation."""
    return (
        (ADD_OPERATOR_KEY, "Key for addition operation"),
        (SUB_OPERATOR_KEY, "Key for substraction operation"),
        (MULT_TABLE_OPERATOR_KEY, "Key for table operation (ex. 4*3)"),
        (SIMPLE_MULT_OPERATOR_KEY, "Key for simple mutliplication (ex. 45*2)"),
        (COMPLEX_MULT_OPERATOR_KEY, "Key for complex multiplication (ex. 12*11)")
    )


class ComputeNumbers():
    """Compute the numbers and validate the result."""

    def __init__(self, first, second, operator, validator):
        """Constructor."""
        self.first = first
        self.second = second
        self.operator = operator
        self.validator = validator

    def __repr__(self):
        """String representation."""
        return f"{self.first} {self.operator} {self.second} = ?"

    def validate(self, result):
        """Validate the result."""
        return self.validator.validate(result, self.first, self.second)

    def get_good_result(self):
        """Return the expected result."""
        return self.validator.get_result(self.first, self.second)


class BaseStrategy():
    """Abstract class of operator strategy."""

    def __init__(self, validator):
        self.validator = validator

    def generate_random(self, start, end):
        """Abstract method to implement in each strategy."""
        message = f"method not implemented for class {self.__class__.__name__}"
        raise err.StrategyError(message)

    def get_validator(self):
        """Return the validator."""
        return self.validator


class AdditionStrategy(BaseStrategy):
    """Strategy for random additions."""

    def generate_random(self, start, end):
        """Implementation of random generation for addition strategy."""
        first = random.randint(start, end)
        second = random.randint(start, end)
        return ComputeNumbers(first, second,
                              ADD_OPERATOR_KEY,
                              self.validator)


class SubstractionStrategy(BaseStrategy):
    """Strategy for random substrations."""

    def generate_random(self, start, end):
        """Implementation of random generation for substraction strategy."""
        first = random.randint(start, end)
        second = random.randint(start, end)

        # switch the numbers if the second number
        # is greater than the first number.
        if second > first:
            first, second = second, first

        return ComputeNumbers(first,
                              second,
                              SUB_OPERATOR_KEY,
                              self.validator)


class MutliplicationTableStrategy(BaseStrategy):
    """Strategy for random mutliplication table operations."""

    def generate_random(self, start, end):
        """Implementation of random generation
        for table multiplication strategy."""
        if start < 1 or start > 10:
            err_message = f"the start param must be between 1 and 10 included: {start} given"
            raise err.BadArgmentsError(err_message)

        if end < 1 or end > 10:
            err_message = f"the end param must be between 1 and 10 included: {end} given"
            raise err.BadArgmentsError(err_message)

        first = random.randint(start, end)
        second = random.randint(1, 10)
        return ComputeNumbers(first,
                              second,
                              MULT_TABLE_OPERATOR_KEY,
                              self.validator)


class SimpleMutliplicationStrategy(BaseStrategy):
    """Strategy for random mutliplication with 1 digit factor."""

    def generate_random(self, start, end):
        """Implementation of random generation
        for simple multiplication strategy."""
        first = random.randint(start, end)
        second = random.randint(1, 10)
        return ComputeNumbers(first,
                              second,
                              MULT_TABLE_OPERATOR_KEY,
                              self.validator)


class ComplexMutliplicationStrategy(BaseStrategy):
    """Strategy for random mutliplication with n digits factor."""

    def generate_random(self, start, end):
        """Implementation of random generation
        for complex multiplication strategy."""
        first = random.randint(start, end)
        second = random.randint(start, end)
        return ComputeNumbers(first,
                              second,
                              MULT_TABLE_OPERATOR_KEY,
                              self.validator)


# Strategies dictionnary.
MULT_VALIDATOR = py_ov.MultiplicationValidator()
STRATEGIES = {
    ADD_OPERATOR_KEY: AdditionStrategy(py_ov.AdditionValidator()),
    SUB_OPERATOR_KEY: SubstractionStrategy(py_ov.SubstractionValidator()),
    MULT_TABLE_OPERATOR_KEY: MutliplicationTableStrategy(MULT_VALIDATOR),
    SIMPLE_MULT_OPERATOR_KEY: SimpleMutliplicationStrategy(MULT_VALIDATOR),
    COMPLEX_MULT_OPERATOR_KEY: ComplexMutliplicationStrategy(MULT_VALIDATOR)
}

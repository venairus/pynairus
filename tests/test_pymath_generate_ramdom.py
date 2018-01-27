"""Unit test module for pymath.generate_random function."""

import unittest
from pynairus.pymath import generate_random
from pynairus.errors.app_error import BadArgmentsError
from pynairus.strategies import operator_strategy as ns_os


class TestPymathGenerateRandom(unittest.TestCase):
    """Unit tests for pymath.generate_random function."""

    def test_substraction_generation(self):
        """Test substraction generation"""
        strategy = generate_random(10, 99, '-')
        self.assertIsInstance(strategy, ns_os.ComputeNumbers)

    def test_addition_generation(self):
        """Test addition generation."""
        strategy = generate_random(10, 99, '+')
        self.assertIsInstance(strategy, ns_os.ComputeNumbers)

    def test_mult_table_generation(self):
        """Test de la génération de multiplication table."""
        strategy = generate_random(1, 3, '*')
        self.assertIsInstance(strategy, ns_os.ComputeNumbers)

    def test_simple_mult_generation(self):
        """Test the simple multiplication generation."""
        strategy = generate_random(10, 99, '1*')
        self.assertIsInstance(strategy, ns_os.ComputeNumbers)

    def test_complex_mult_generation(self):
        """Test the complex multiplication generation."""
        strategy = generate_random(10, 99, 'n*')
        self.assertIsInstance(strategy, ns_os.ComputeNumbers)

    def test_bad_parameters(self):
        """Test raise exception in case of unknown operator."""
        with self.assertRaises(BadArgmentsError,
                               msg="BadArgmentsError expected"):
            generate_random(10, 99, "x")

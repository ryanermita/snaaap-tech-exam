import unittest

from src.utils import validator


class TestIsValidEmail(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_valid_email(self):
        result = validator.is_valid_email('john@doe.com.ph')
        self.assertTrue(result)

    def test_invalid_email(self):
        result = validator.is_valid_email('john@doe.com.ph@')
        self.assertTrue(result is False)
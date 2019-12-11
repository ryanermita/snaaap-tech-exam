import unittest

from src.utils import common_util


class TestToBool(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_truthy_values(self):
        truthy_values = ['t', 'true', 'True', 1, 1.0]

        for value in truthy_values:
            with self.subTest(value=value):
                self.assertTrue(common_util.to_bool(value))

    def test_falsy_values(self):
        falsy_values = ['f', 'false', 'False', 0, 0.0]

        for value in falsy_values:
            with self.subTest(value=value):
                self.assertFalse(common_util.to_bool(value))

    def test_invalid_value(self):
        with self.assertRaises(ValueError) as err_context:
            common_util.to_bool('x')
        self.assertEqual(str(err_context.exception),
                         "Invalid data for boolean convertion: x")

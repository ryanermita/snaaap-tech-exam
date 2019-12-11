import unittest

from src.helpers.flask_helper import ResponseHelper


class TestFormatResponseData(unittest.TestCase):

    def setUp(self):
        self.data = {"message": "Hello World!"}

    def tearDown(self):
        pass

    def test_formatted_response_data_keys(self):
        expected_keys = ["success", "results", "errors"]
        formatted_response_data = ResponseHelper(self.data)._format_response_data()
        formatted_response_keys = list(formatted_response_data.keys())

        self.assertListEqual(sorted(expected_keys), sorted(formatted_response_keys))

    def test_formatted_response_data_with_default_status_code(self):
        result_data = {'success': True, 'errors': [],
                       'results': {'message': 'Hello World!'}}
        formatted_response_data = ResponseHelper(self.data)._format_response_data()

        self.assertDictEqual(result_data, formatted_response_data)

    def test_formatted_response_data_with_2xx_status_code(self):
        result_data = {'success': True, 'errors': [],
                       'results': {'message': 'Hello World!'}}
        formatted_response_data = ResponseHelper(self.data, status_code=201)._format_response_data()

        self.assertDictEqual(result_data, formatted_response_data)

    def test_formatted_response_data_with_4xx_status_code(self):
        result_data = {'success': False, 'results': [],
                       'errors': {'message': 'Hello World!'}}
        formatted_response_data = ResponseHelper(self.data, status_code=400)._format_response_data()

        self.assertDictEqual(result_data, formatted_response_data)

    def test_formatted_response_data_with_5xx_status_code(self):
        result_data = {'success': False, 'results': [],
                       'errors': {'message': 'Hello World!'}}
        formatted_response_data = ResponseHelper(self.data, status_code=500)._format_response_data()

        self.assertDictEqual(result_data, formatted_response_data)
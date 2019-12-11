import unittest

from src.helpers.flask_helper import ResponseHelper


class TestResponseJsonify(unittest.TestCase):

    def setUp(self):
        self.data = {"message": "Hello World!"}

    def tearDown(self):
        pass

    def test_response_jsonify_attributes(self):
        jsonified_response = ResponseHelper(self.data).jsonify()

        self.assertTrue(hasattr(jsonified_response, "status_code"))
        self.assertTrue(hasattr(jsonified_response, "is_json"))
        self.assertTrue(hasattr(jsonified_response, "mimetype"))
        self.assertTrue(hasattr(jsonified_response, "get_json"))
        self.assertTrue(hasattr(jsonified_response, "data"))
        self.assertTrue(hasattr(jsonified_response, "status"))

    def test_response_jsonify_values(self):
        result_data = {'success': True, 'errors': [],
                       'results': {'message': 'Hello World!'}}
        jsonified_response = ResponseHelper(self.data).jsonify()

        self.assertEqual(jsonified_response.status_code, 200)
        self.assertEqual(jsonified_response.mimetype, "application/json")
        self.assertTrue(jsonified_response.is_json)
        self.assertEqual(jsonified_response.get_json(), result_data)

    def test_response_jsonify_with_2xx_status_code(self):
        result_data = {'success': True, 'errors': [],
                       'results': {'message': 'Hello World!'}}
        jsonified_response = ResponseHelper(self.data, status_code=201).jsonify()

        self.assertEqual(jsonified_response.status_code, 201)
        self.assertEqual(jsonified_response.get_json(), result_data)

    def test_response_dict_with_4xx_status_code(self):
        result_data = {'success': False, 'results': [],
                       'errors': {'message': 'Hello World!'}}
        jsonified_response = ResponseHelper(self.data, status_code=400).jsonify()

        self.assertEqual(jsonified_response.status_code, 400)
        self.assertEqual(jsonified_response.get_json(), result_data)

    def test_response_dict_with_5xx_status_code(self):
        result_data = {'success': False, 'results': [],
                       'errors': {'message': 'Hello World!'}}
        jsonified_response = ResponseHelper(self.data, status_code=500).jsonify()

        self.assertEqual(jsonified_response.status_code, 500)
        self.assertEqual(jsonified_response.get_json(), result_data)
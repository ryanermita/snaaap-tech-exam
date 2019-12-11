import unittest

from src.helpers.flask_helper import ResponseHelper
from src.constants import http_status_code


class TestResponseObject(unittest.TestCase):

    def setUp(self):
        self.data = {"message": "Hello World!"}

    def tearDown(self):
        pass

    def test_response_object_attributes(self):
        mocked_response = ResponseHelper(self.data)

        self.assertTrue(hasattr(mocked_response, "success"))
        self.assertTrue(hasattr(mocked_response, "data"))
        self.assertTrue(hasattr(mocked_response, "status_code"))

    def test_response_object_with_non_int_status_code(self):

        with self.assertRaises(TypeError) as err_context:
            ResponseHelper(self.data, "200")

        self.assertEqual(str(err_context.exception), "Status code must be an integer.")

    def test_response_object_with_default_status_code(self):
        mocked_response = ResponseHelper(self.data)

        self.assertEqual(mocked_response.success, True)
        self.assertEqual(mocked_response.data, self.data)
        self.assertEqual(mocked_response.status_code, http_status_code.OK)

    def test_response_object_with_2xx_status_code(self):
        mocked_response = ResponseHelper(self.data, status_code=http_status_code.CREATED)

        self.assertEqual(mocked_response.success, True)
        self.assertEqual(mocked_response.data, self.data)
        self.assertEqual(mocked_response.status_code, http_status_code.CREATED)

    def test_response_object_with_4xx_status_code(self):
        mocked_response = ResponseHelper(self.data, 
                                         status_code=http_status_code.UNPROCESSABLE_ENTITY)

        self.assertEqual(mocked_response.success, False)
        self.assertEqual(mocked_response.data, self.data)
        self.assertEqual(mocked_response.status_code, http_status_code.UNPROCESSABLE_ENTITY)

    def test_response_object_with_5xx_status_code(self):
        mocked_response = ResponseHelper(self.data, status_code=http_status_code.INTERNAL_SERVER_ERROR)

        self.assertEqual(mocked_response.success, False)
        self.assertEqual(mocked_response.data, self.data)
        self.assertEqual(mocked_response.status_code, http_status_code.INTERNAL_SERVER_ERROR)
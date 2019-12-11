import unittest
from unittest.mock import MagicMock

from src.utils import flask_util

from flask import Request


class TestGetRequestData(unittest.TestCase):
    def setUp(self):
        self.mock_request = MagicMock(spec=Request)

    def tearDown(self):
        pass

    def test_get_request_data_with_json_data(self):
        request_data = {'name': 'John'}
        self.mock_request.get_json = MagicMock(return_value=request_data)

        result = flask_util.get_request_data(self.mock_request)
        self.assertDictEqual(result, request_data)

    def test_get_request_data_with_args_data(self):
        request_data = {'name': 'John'}
        self.mock_request.get_json = MagicMock(return_value={})
        self.mock_request.values.to_dict = MagicMock(return_value=request_data)

        result = flask_util.get_request_data(self.mock_request)
        self.assertDictEqual(result, request_data)

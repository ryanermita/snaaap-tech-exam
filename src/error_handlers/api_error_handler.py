from src.error_handlers.api_exception import (MissingRequiredFields,
                                              RequestParamException,
                                              ResourceNotFound)
from src.constants import http_status_code

from flask import Blueprint, jsonify


api_error_handler = Blueprint('api_error_handler', __name__)


@api_error_handler.app_errorhandler(MissingRequiredFields)
def missing_required_fields(error):
    response = {
        "success": False,
        "errors": error.args[0],
        "results": []
    }
    return jsonify(response), http_status_code.UNPROCESSABLE_ENTITY


@api_error_handler.app_errorhandler(RequestParamException)
def request_param_exception(error):
    response = {
        "success": False,
        "errors": error.args[0],
        "results": []
    }
    return jsonify(response), http_status_code.UNPROCESSABLE_ENTITY

@api_error_handler.app_errorhandler(ResourceNotFound)
def resource_not_found(error):
    response = {
        "success": False,
        "errors": error.args[0],
        "results": []
    }
    return jsonify(response), http_status_code.NOT_FOUND


@api_error_handler.app_errorhandler(Exception)
def internal_server_error(error):
    response = {
        "success": False,
        "errors": "Something went wrong.",
        "results": []
    }
    return jsonify(response), http_status_code.INTERNAL_SERVER_ERROR

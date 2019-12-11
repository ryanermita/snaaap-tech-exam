from src.exceptions.generic import MissingRequiredFields
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

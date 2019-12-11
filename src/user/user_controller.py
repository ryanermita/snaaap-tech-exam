import logging

from user import user_service
from utils import flask_util

from flask import Blueprint, request

user = Blueprint('user', __name__, url_prefix='/users')


@user.route('/', methods=['POST'])
def create():
    try:
        data = flask_util.get_request_data(request)
        response = user_service.create(data)
        return response.jsonify()
    except Exception as e:
        logging.exception(e)
        raise e


@user.route('/', methods=['GET'])
def retrieve_many():
    try:
        data = flask_util.get_request_data(request)
        response = user_service.retrieve_many(data)
        return response.jsonify()
    except Exception as e:
        logging.exception(e)
        raise e


@user.route('/<db_id>/', methods=['PUT'])
def update(db_id):
    try:
        data = flask_util.get_request_data(request)
        data['id'] = db_id
        response = user_service.update(data)
        return response.jsonify()
    except Exception as e:
        logging.exception(e)
        raise e


@user.route('/<db_id>/', methods=['DELETE'])
def delete(db_id):
    try:
        data = flask_util.get_request_data(request)
        data['id'] = db_id
        response = user_service.delete(data)
        return response.jsonify()
    except Exception as e:
        logging.exception(e)
        raise e

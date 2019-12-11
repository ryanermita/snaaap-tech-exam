import os
import logging

from src.utils import common_util

import pymodm
from flasgger import Swagger


def _initialize_db():
    try:
        host = os.environ['MONGODB_HOST']
        port = os.environ['MONGODB_PORT']
        user = os.environ['MONGODB_USER']
        password = os.environ['MONGODB_PASSWORD']
        database = os.environ['MONGODB_DATABASE']
        db_uri = f"mongodb://{user}:{password}@{host}:{port}/{database}"
        pymodm.connection.connect(db_uri)
    except KeyError as e:
        logging.error(f"Missing config: {e}")
        raise e
    except Exception as e:
        logging.error(f"Unexpected error while initializing database: {e}")
        raise e


def _initialize_swagger(app):
    try:
        swagger_enabled = common_util.to_bool(os.environ.get("SWAGGER_ENABLED",
                                                             False))
        if not swagger_enabled:
            return

        return Swagger(app)
    except KeyError as e:
        logging.error(f"Missing config: {e}")
        raise e
    except Exception as e:
        logging.error(f"Unexpected error while initializing swagger: {e}")
        raise e

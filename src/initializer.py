import os
import logging

import pymodm


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

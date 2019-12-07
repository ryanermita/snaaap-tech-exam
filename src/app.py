import os

import logging

from flask import Flask, escape, request
import pymodm

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


def _initialize_db():
    try:
        mongodb_host = os.environ['MONGODB_HOST']
        mongodb_port = os.environ['MONGODB_PORT']
        mongodb_user = os.environ['MONGODB_USER']
        mongodb_password = os.environ['MONGODB_PASSWORD']
        mongodb_database = os.environ['MONGODB_DATABASE']
        db_uri = f"mongodb://{mongodb_user}:{mongodb_password}@{mongodb_host}:{mongodb_port}/{mongodb_database}"

        pymodm.connection.connect(db_uri)
    except KeyError as e:
        logging.error(f"Missing config: {e}")
        raise e
    except Exception as e:
        logging.error(f"Unexpected error while initializing database: {e}")
        raise e


if __name__ == '__main__':
    _initialize_db()
    app.run(host="0.0.0.0", debug=True)

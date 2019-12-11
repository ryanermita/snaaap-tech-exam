import os

from user.user_controller import user
from error_handlers.api_error_handler import api_error_handler
import initializer

from flask import Flask

app = Flask(__name__)

app.register_blueprint(user)
app.register_blueprint(api_error_handler)

if __name__ == '__main__':
    initializer._initialize_db()
    initializer._initialize_swagger(app)

    app.run(host=os.environ.get('API_HOST', '0.0.0.0'),
            debug=True,
            port=os.environ.get('API_PORT', 5000))

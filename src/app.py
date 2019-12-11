from user.user_controller import user
from error_handlers.api_error_handler import api_error_handler
from initializer import _initialize_db

from flask import Flask

app = Flask(__name__)

app.register_blueprint(user)
app.register_blueprint(api_error_handler)

if __name__ == '__main__':
    _initialize_db()
    # TODO: retrieve app host from env var
    app.run(host="0.0.0.0", debug=True)

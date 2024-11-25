from flask import Flask
from flask_smorest import Api

from rest_api.src.users.user_controller import user_blp

server = Flask(__name__)
server.config['secret_key'] = 'secret_key'


class ApiConfig:
    API_TITLE = 'Example Api'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_SWAGGER_UI_PATH = '/swagger-ui'
    OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'


server.config.from_object(ApiConfig)
api = Api(server)
api.register_blueprint(user_blp)


@server.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=8080)

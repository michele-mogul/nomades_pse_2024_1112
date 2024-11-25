from flask import Flask
from flask_smorest import Api

server = Flask(__name__)

class APIConfig:
  API_TITLE = "Example API"
  API_VERSION = 'v1'
  OPENAPI_VERSION = '3.0.2'
  OPENAPI_URL_PREFIX = '/'
  OPENAPI_SWAGGER_UI_PATH = '/docs'
  OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

server.config.from_object(APIConfig)
api = Api(server)

@server.route("/")
def index():
  return "Hello World!"

if __name__ == '__main__':
  server.run(debug=True, host='0.0.0.0', port=5050)
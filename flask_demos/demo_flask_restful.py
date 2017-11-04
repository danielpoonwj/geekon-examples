from flask import Flask
from flask_restful import Api, Resource

flask_app = Flask(__name__)
flask_api = Api(flask_app)


class HelloWorld(Resource):
    def get(self):
        return 'Hello World'


class Heartbeat(Resource):
    def get(self):
        return {'status': 'ok'}


flask_api.add_resource(HelloWorld, '/')
flask_api.add_resource(Heartbeat, '/heartbeat')

if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=9090,
        debug=True
    )

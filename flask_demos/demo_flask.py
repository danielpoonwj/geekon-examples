from flask import Flask, make_response, jsonify

flask_app = Flask(__name__)


@flask_app.route('/')
def hello_world():
    return 'Hello World'


@flask_app.route('/heartbeat')
def heartbeat():
    return make_response(
        jsonify({
            'status': 'ok'
        })
    )


if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=8080,
        debug=True
    )

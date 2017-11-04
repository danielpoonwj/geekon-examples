from demo_app import flask_app

if __name__ == '__main__':
    flask_app.run(
        '127.0.0.1',
        8081,
        debug=True
    )

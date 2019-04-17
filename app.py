import os

import flask
import redis

app = flask.Flask(__name__)

redis = redis.Redis(host=os.environ.get('REDIS_HOST', 'localhost'), port=6379)


@app.route('/')
def index():
    time = redis.incr('times')
    return f'<h1>hello world, this is {time}</h1>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

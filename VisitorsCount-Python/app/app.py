from flask import Flask
import redis 
import os

app = Flask(__name__)

# Connect to Redis

cache = redis.Redis(
    host=os.getenv('Redis_HOST', 'redis'),
    port=6379)

@app.route('/')
def hello():
    count = cache.incr('visits')
    return f'Hello World! You are visitor number {count}'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
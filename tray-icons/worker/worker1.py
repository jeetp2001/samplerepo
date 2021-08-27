import os
import redis
from rq import Queue, Connection, Worker

listen = ['default']

redis_url = os.getenv('REDISTOGO_URL','redis://192.168.58.2:6379')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue,listen)))
        worker.work()



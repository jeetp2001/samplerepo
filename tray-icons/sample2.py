import redis
import os
from modules import fun
from rq import Queue, Worker
from tkinter import *

# def add_l(i):
#     if i not in l:
#         l.append(i)

def display(i):
    # l=[]
    # l.append(i)
    # q = Queue(connection=Redis(host='172.17.0.4',port='6379'))
    # for i in l:
    redis_url = os.getenv('REDISTOGO_URL','redis://192.168.58.2:6379')
    conn = redis.from_url(redis_url)
    q = Queue(connection=conn)
    q.enqueue(fun,i)

    
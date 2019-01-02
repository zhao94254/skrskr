#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 2018/12/28 3:08 PM
# @Author  : zpy
# @Software: PyCharm

# 这里主要写Connection & Transport 的抽象

import pymongo

class Connection(object):
    """
    提供一层接口，支持多个transport
    """

    def __init__(self, uri, appname, exs):

        self.uri = uri
        self.appname = appname
        self.exs = exs

    def parse_uri(self):
        mtype = self.uri.split('://')[0]
        return self.dispatch(mtype)

    def dispatch(self, mtype):
        from skrq.transport.mongo import MongoChannel

        if mtype == 'mongodb':
            return MongoChannel(self.appname,self.exs ,self.uri)

    def __enter__(self):
        return self.parse_uri()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Channel(object):
    """
    这里处理 Exchange - Queue 之间的逻辑
    """

    def __init__(self, appname, exchanges, uri):
        self.appname = appname
        self.exchanges = exchanges
        self.uri = uri
        self.init_ex()

    def get(self, qname):
        pass

    def put(self, qname, msg, **kwargs):
        pass

    def ack(self):
        pass

    def init_ex(self):
        pass

class Exchange(object):
    """
    交换机实现
    Exchange -> Queue(多个)
    """

    def __init__(self, name, etype, queues):
        self.exname = name
        self.etype = etype
        self.queues = queues

    def add_queue(self, queues):
        pass

    def direct_ex(self):
        pass

    def topic_ex(self):
        pass

    def fanout_ex(self):
        pass


class Queue(object):

    def __init__(self, name):
        self.name = name

    def get(self):
        pass

    def put(self):
        pass

    def delmsg(self):
        pass


if __name__ == '__main__':
    q1 = Queue(name='qqq')
    q2 = Queue(name='qq2')
    ex = Exchange('ex', 'direct', [q1, q2])

    with Connection('mongodb://127.0.0.1:27017', 'skrskr', [ex]) as chan:
        chan.put('qqq', {'test':'ttestt'})
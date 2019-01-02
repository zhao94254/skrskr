#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 2018/12/28 3:08 PM
# @Author  : zpy
# @Software: PyCharm

# 这里主要写Connection & Transport 的抽象

class Connection(object):
    """
    提供一层接口，支持多个transport
    """

    def __init__(self, uri):
        self.uri = uri

    def parse_uri(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Channel(object):
    """
    这里处理 Exchange - Queue 之间的逻辑
    """

    def __init__(self, appname, exchanges, conn):
        self.appname = appname
        self.exchanges = exchanges
        self.conn = conn

    def get(self):
        pass

    def put(self):
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



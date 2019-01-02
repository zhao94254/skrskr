#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 2018/12/28 4:50 PM
# @Author  : zpy
# @Software: PyCharm

from skrq.base import Channel
import pymongo

# 应该是在channel 这一层做mongo redis 等。。
#

class MongoChannel(Channel):

    @property
    def conn(self):
        return pymongo.MongoClient(self.uri)

    def get(self, qname):
        return self.table.find_one({'queue': qname})

    def put(self, qname, msg, **kwargs):
        self.table.insert({'queue': qname, 'message': msg})

    def init_ex(self):
        db = 'skrskr'
        table = '{appname}_message'.format(appname=self.appname)
        qtable = '{appname}_queue'.format(appname=self.appname)
        self.basetable = self.conn[db][table]
        self.table = self.conn[db][qtable]
        for exs in self.exchanges:
            data = [{'exchange': exs.exname,'queue':d.name } for d in exs.queues]
            self.basetable.insert(data)
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 2018/12/28 4:50 PM
# @Author  : zpy
# @Software: PyCharm

from skrq.base import Channel

# 应该是在channel 这一层做mongo redis 等。。
#

class MongoChannel(Channel):


    def get(self):
        pass

    def put(self):
        pass

    def init_ex(self):
        db = 'skrskr'
        table = '{appname}_message'.format(appname=self.appname)
        for exs in self.exchanges:
            data = [{'exchange': exs.exname,'queue':d.name } for d in exs.queues]
            self.conn[db][table].insert(data)
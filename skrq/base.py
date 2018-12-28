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

    def parse_uri(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Transport(object):
    """
    transport 抽象
    """
    pass




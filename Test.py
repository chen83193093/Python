#!/bin/env python
# -*- coding:utf-8 -*-
import sys
from time import sleep


def slow(msg, text):
    print(msg),
    for i in text:
        print(i),
        sys.stdout.flush()
        sleep(1)
    return '.'
slow('loginning','与一般的通信总线相比，CAN总线的数据通信具有突出的')
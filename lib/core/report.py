#!/usr/bin/env python
# -*- coding:utf-8 -*-
 import sys
 import time

 def report():
    f = open('log.txt','a')
    print>> f, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    f.close()
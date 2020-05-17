#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Name:sql-scan
Author:timstrong
Copyright (c) 2019
'''
import requests
import sys
import os
import commands
import time
import threading
import subprocess
import tkMessageBox

from lib.core.Spider import SpiderMain

import Tkinter as tk


def stop_check():
    open('log.txt', 'w').close()
    print("stopcheck")
    sys.exit()


def sys_info():
    print("show sys_info")
    tkMessageBox.showinfo('版本信息', '日期：2020年2月 软件版本：1.0', parent=window)


def connect_me():
    tkMessageBox.showinfo('联系方式', 'connect me qq:1533291427\nemail:timstrong@163.com', parent=window)


window = tk.Tk()
window.title("sql-scan")
window.geometry("500x400")

form_1 = tk.Canvas(window, bg="#efefef", width=10, height=4).place(x=0, y=0, width=500, height=400)

a = tk.Entry(window)
a.place(x=80, y=50, width=301, height=50)
b = tk.Entry(window)
b.place(x=80, y=120, width=120, height=20)
c = tk.Text(window, bg='black', fg='white')
c.place(x=80, y=250, width=400, height=130)

def thread_it(func):
    '''将函数打包进线程'''
    # 创建
    print "子进程运行中"
    t = threading.Thread(target=func)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


def start_check():
    global root, threadNum
    root = a.get()
    threadNum = int(b.get())
    print("start..........")
    c.insert('insert', "开始检查:" + root + "\n\n")
    test1 = SpiderMain(root, threadNum)
    test1.craw()
    #command = "python scan.py \"" + root + "\""
    #os.system(command)
    file_name = 'log.txt'
    with open(file_name) as file_obj:
        for content in file_obj:
            c.insert('insert',content+"\n")

def action(root,threadNum):
    wgd = SpiderMain(root, threadNum)
    wgd.craw()


Label_1 = tk.Label(window, text="输入待检测网址，只支持单个网址检测.\n多线程可以加快检测速度，可设置范围为1-10.").place(x=80, y=156, width=250,
                                                                                     height=86)

label_1 = tk.Label(window, text="输入网址:", width=10, height=4).place(x=-24, y=64, width=100, height=20)
Label_2 = tk.Label(window, text="web系统SQL注入漏洞检测系统", width=10, height=4).place(x=144, y=19, width=186, height=20)
Label_3 = tk.Label(window, text="状态:", width=10, height=4).place(x=-20, y=310, width=100, height=20)
Label_4 = tk.Label(window, text="输入线程数:", width=10, height=4).place(x=-18, y=121, width=100, height=20)

Button_3 = tk.Button(window, text="开始检测", width=10, height=4, command=lambda :thread_it(start_check))
Button_3.place(x=400, y=50, width=100, height=28)
Button_4 = tk.Button(window, text="结束检测", width=10, height=4, command=stop_check)
Button_4.place(x=400, y=100, width=100, height=28)
Button_5 = tk.Button(window, text="版本信息", width=10, height=4, command=sys_info)
Button_5.place(x=400, y=150, width=100, height=28)
Button_6 = tk.Button(window, text="联系作者", width=10, height=4, command=connect_me)
Button_6.place(x=400, y=197, width=100, height=28)

window.mainloop()

# sql-scan
# SQL注入漏洞检测系统框架

scanui.py 利用tkinter编写的主程序框架，图形界面。

bool.py 布尔方式的爆库脚本

scan.py 命令行形式的主程序

运行环境： python 2.7  
          re，random，threading，time，bs4，urlprase，requests

运行方式： 命令行  python scan.py + “http://www.test.com” + num（1-10）

注：lib和script文件夹中的init空文件请勿删除，在pycharm中运行时，没有init文件会报错。

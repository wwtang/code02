#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys


con = mdb.connect('localhost', 'testuser', 
    'testdB', 'testdb');

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    numrows = int(cur.rowcount)

    for i in range(numrows):
        row = cur.fetchone()
        print row[0],"--", row[1]

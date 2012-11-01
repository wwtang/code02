#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys


con = mdb.connect('localhost', 'testuser', 
        'testdB', 'testdb');

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()

    print "rows:", rows

    for row in rows:
        print row

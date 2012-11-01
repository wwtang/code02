#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

con = mdb.connect('localhost', 'testuser', 
    'testdB', 'testdb')

with con:

    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()

    print"rows_Dict: ", rows

    for row in rows:
        print "%s %s" % (row["Id"], row["Name"])

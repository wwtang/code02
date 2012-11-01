#!/usr/bin/python
# _*_coding: utf-8 _*_

import MySQLdb as mdb
import sys

con = mdb.connect("localhost","testuser","testdB","testdb")

with con:
    cur = con.cursor()

    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()

    desc = cur.description

    print "%s %3s" %(desc[0][0], desc[1][0])

    for row in rows:
        print "%2s %3s" % row

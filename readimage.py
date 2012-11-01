#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb 
import sys

try:
    conn = mdb.connect(host='localhost',user='testuser', 
        passwd='testdB', db='testdb')

    cursor = conn.cursor()

    cursor.execute("SELECT Data FROM Images LIMIT 1")

    fout = open('/Users/qitang/Desktop/image.png','wb')
    fout.write(cursor.fetchone()[0])
    print "We are here"
    fout.close()

    cursor.close()
    conn.close()

except IOError, e:

    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)


#!/usr/bin/python
#_*_ coding: utf-8 _*_

import MySQLdb as mdb
import sys

con = mdb.connect("localhost","testuser","testdB","testdb")

with con:
    cur = con.cursor()

    cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s ",
            ("Guy de manupassant", "4"))
    print "Number of rows updated: %d "% cur.rowcount

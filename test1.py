#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:40:35 2019

@author: lucky
"""
import sqlite3 as lite
import sys
 
con = lite.connect('user.db')
 
with con:
    
    cur = con.cursor() 
    cur.execute("SELECT * FROM Users")
 
    rows = cur.fetchall()
 
    for row in rows:
        print (row)
 
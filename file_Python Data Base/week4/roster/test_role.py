# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:25:53 2016

@author: THIENLOI
"""

import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.execute('''
SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
''')

for row in cur:
    print row
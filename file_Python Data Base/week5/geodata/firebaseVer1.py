# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:12:19 2016

@author: THIENLOI
"""
from firebase import firebase

firebase = firebase.FirebaseApplication('https://flickering-heat-4335.firebaseio.com/', None)
result = firebase.get('/', None)
for item in result:
    print result[item]
    
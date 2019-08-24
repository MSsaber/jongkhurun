#!/usr/bin/python
# -*- coding: utf-8 -*-
try :
    import pymysql
except ImportError as e:
    import os
    print("download mysql support")
    os.system('pip3 install pymysql')

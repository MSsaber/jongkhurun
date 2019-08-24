#!/usr/bin/python
# -*- coding: utf-8 -*-

import Log

def config_log():
    Log.JLogging(File=True, Function=True, LogLevel=True, Line=True, LogFile='JongRun.log')
    Log.test()

config_log()
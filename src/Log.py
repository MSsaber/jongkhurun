#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

test_open = False

def test():
    logging.debug("This is a debug log.哈哈")
    logging.info("This is a info log.")
    logging.warning("This is a warning log.")
    logging.error("This is a error log.")
    logging.critical("This is a critical log.")

class JLogging:
    log_fmt_config = { "Logger" : "%(name)s", "LogLevel" : "%(levelname)s",
                      "File" : "%(filename)s", "Module" : "%(module)s",
                      "Function" : "%(funcName)s", "Line" : "%(lineno)d",
                      "Thread" : "%(thread)d", "ThreadName" : "%(threadName)s",
                      "Process" : "%(process)d", "LogFile" : "a.txt",
                      "Charset" : "utf-8" , "Level" : logging.DEBUG }
    def __init__(self, **log_args):
        self.config(**log_args)
        self.reset()

    def __get_log_format(self):
        fmt = "%(asctime)s"
        for key in self.log_args:
            if key != "LogFile" and key != "Charset" and key != "Level":
                fmt += " - " + self.log_fmt_config[key]
        fmt += " - %(message)s"
        return fmt

    def reset(self):
        h = []
        if "LogFile" in self.log_args:
            h.append(logging.FileHandler(self.log_args["LogFile"], encoding='utf-8'))
        DATE_FORMAT = "%Y-%m-%d %H:%M:%S %p"
        h.append(logging.StreamHandler())
        if "Level" in self.log_args:
            lv = self.log_args["Level"]
        else:
            lv = self.log_fmt_config["Level"]
        logging.basicConfig(level=lv, format=self.__get_log_format(), datefmt=DATE_FORMAT, handlers=h)

    def config(self, **log_args):
        all_param_valid = True
        error_param = []
        self.log_args = log_args
        self_keys = self.log_fmt_config.keys()
        for key in self.log_args.keys():
            if key not in self_keys:
                all_param_valid = False
                error_param.append(key)
        if not all_param_valid:
            print("Invlid param : ", error_param)
            raise Exception("Invlid param : ", error_param)

if test_open:
    jl = JLogging()
    eval('test')()

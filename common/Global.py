#coding=utf8
import os
import sys
import configparser

def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)
#打印结果
mainpath = cur_file_dir()
ConfigFile = os.path.join(mainpath,"config.ini")

def readcfg():
    kargs={}
    cf = configparser.ConfigParser()
    cf.read(ConfigFile.replace("\\","/"))
    for opt in cf.sections():
        if opt:
            kargs[opt]={}
    for opt in kargs.keys():
        for k,v in cf.items(opt):
            kargs[opt][k]=v
    return kargs

def writecfg(**kargs):
    pass

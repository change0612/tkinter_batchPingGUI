# -*- coding: utf-8 -*-
import os
import json
from app import config


# cmd ping 执行事件
def ping_cmd(title,ip):
    cmd = 'start cmd /k "title {title} &&ping {ip} -t"'.format(title=title,ip=ip)
    try:
        os.system(cmd)
    except Ellipsis as e:
        print(e)

# 获取 节点信息
def hosts_Info(region):
    app_path = os.path.dirname(os.path.abspath(__file__))
    HK = os.path.join(app_path, "HK.txt")
    BGP = os.path.join(app_path, "BGP.txt")
    US = os.path.join(app_path, "US.txt")
    data = ""
    if region == "HK":
        txt = HK
    elif region == "BGP":
        txt = BGP
    elif region == "US":
        txt = US
    for lines in open(txt).readlines():
        data += lines.strip('\n')
    data_dict = eval(data)
    return data_dict

def close_ping():
    cmd = 'start cmd /k "taskkill /f /im ping.exe|taskkill /f /im cmd.exe"'
    os.system(cmd)


from tkinter import *
from app import tools
import os

app_path = os.path.dirname(os.path.abspath(__file__))

# 创建主窗体
window = Tk()
window.title("沙田ping")
window.geometry("420x580")
window.resizable(width = False,height = False)
window.iconbitmap("icons.ico")

# 标题窗体
title_fm = Frame(window).place(x= 30,y=40)
# 内容窗体
body_fm = Frame(window).place(x=200,y=300)

# 按钮创建
#  创建节点按钮方法
class Button_bt:
    def __init__(self,bt_name,fm_name,title,ip,x,y):
        Button(fm_name, text=title, width=13, command=lambda: tools.ping_cmd(title, ip)).place(x=x,y=y)

#  创建机房按钮方法
class Button_title:
    def __init__(self, title_name, host, x, y):
        Button(title_fm, text=title_name,width=10,command=lambda: create_bt(host)).place(x=x, y=y)

# 创建按钮函数
def create_bt(region):
    body_fm = Frame(window,width=400,height=550).place(x=13, y=70)
    if region == "bgp":
        host_name = tools.hosts_Info('BGP')
    elif region == "hk":
        host_name = tools.hosts_Info('HK')
    elif region == "us":
        host_name = tools.hosts_Info('US')

    i, f, y,num = 0, 0, 0, 0
    bt_x, bt_y = 15, 80

    for title, ip in host_name.items():
        i+=1
        if f != 4:
            Button_bt("i",body_fm, title, ip, bt_x + i, bt_y + y)
            i += 95
            f += 1
        else:
            f = 1
            i = 0
            y += 30
            Button_bt("i", body_fm, title, ip, bt_x + i, bt_y + y)
            i += 95

#  节点信息
host_list = ("hk","bgp","us")

# 关闭所有ping
Button(window,text="关闭所有ping ",width=62,command=tools.close_ping).place(x=10,y=10)
i = 0
# 创建节点选自信息
for v in range(len(host_list)):
    if  host_list[v] == "bgp":
        title_name = "BGP"
    elif  host_list[v] == "hk":
        title_name = "香港"
    elif  host_list[v] == "us":
        title_name = "美国"
    Button_title(title_name,host_list[v],10+i,y=45)
    i+=77

window.mainloop()
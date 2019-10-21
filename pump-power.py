#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import *
from tkinter.dialog import *
import tkinter.messagebox


win = Tk()

win.title("水泵功率计算")
win.iconbitmap("pump.ico")
win.resizable(0, 0)# 禁止调整窗口大小


def about():
    tkinter.messagebox.showinfo("关于","反馈建议：zhanghaowk@foxmail.com \n               @2018")



#创建菜单栏
menubar = Menu(win)
menubar.add_command(label = "关于", command=about)


frame = Frame(win)

frame.pack(padx=10, pady=10)

Label(frame, text="泵的流量:").grid(row=0, column=0, sticky=E)# 设置其在界面中出现的位置  column代表列   row 代表行
Label(frame, text="泵的扬程:").grid(row=1, column=0, sticky=E)
Label(frame, text="泵的效率:").grid(row=2, column=0, sticky=E)
Label(frame, text="传动方式:").grid(row=3, column=0, sticky=E)

Label(frame, text="泵的轴功率:").grid(row=5, column=0, sticky=E)
Label(frame, text="配用电机功率:").grid(row=6, column=0, sticky=E)

Label(frame, text="m3/h").grid(row=0, column=2)
Label(frame, text="m").grid(row=1, column=2)
Label(frame, text="%").grid(row=2, column=2)
Label(frame, text="kW").grid(row=5, column=2)
Label(frame, text="kW").grid(row=7, column=2)
Label(frame, text="至").grid(row=7, column=0, sticky=E)


# 创建一个下拉列表
transmission = StringVar()
transmissionChosen = Combobox(frame, width=7, textvariable=transmission)#textvariable
transmissionChosen["values"] = ("联轴器", "直连", "三角带")# 设置下拉列表的值
transmissionChosen["state"] = "readonly"
transmissionChosen.grid(row=3, column=1)
transmissionChosen.current(0)# 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值

def chuandong():
    if transmissionChosen.get() == "联轴器":
        ch = 0.98
    elif transmissionChosen.get() == "直连":
        ch = 1
    elif transmissionChosen.get() == "三角带":
        ch = 0.95

    return ch


#清空输入
def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)


v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()

#输入框
e1 = Entry(frame, width=10, textvariable=v1, validate="key")
e1.grid(row=0, column=1)

e2 = Entry(frame, width=10, textvariable=v2, validate="key")
e2.grid(row=1, column=1)

e3 = Entry(frame, width=10, textvariable=v3, validate="key")
e3.grid(row=2, column=1)

e4 = Entry(frame, width=10, textvariable=v4, state="readonly")
e4.grid(row=5, column=1)

e5 = Entry(frame, width=10, textvariable=v5, state="readonly")
e5.grid(row=6, column=1)

e6 = Entry(frame, width=10, textvariable=v6, state="readonly")
e6.grid(row=7, column=1)



#计算
def calc():
    N1 = 1000 * float(v1.get()) * float(v2.get()) / (3600 * 102 * float(v3.get())/100)
    m = chuandong()
    N2 = N1 / m
            
#电机容量安全系数的选取
    if N2 < 1:
        K2 = 1.7 * N2
        K1 = K2
    elif 1 <= N2 < 2:
        K1 = 1.5 * N2
        K2 = 1.7 * N2

    elif 2 <= N2 < 5:
        K1 = 1.3 * N2
        K2 = 1.5 * N2

    elif 5 <= N2 < 10:
        K1 = 1.25 * N2
        K2 = 1.3 * N2

    elif 10 <= N2 < 25:
        K1 = 1.15 * N2
        K2 = 1.25 * N2

    elif 25 <= N2 < 60:
        K1 = 1.1 * N2
        K2 = 1.15 * N2

    elif 60 <= N2 <= 100:
        K1 = 1.08 * N2
        K2 = 1.1 * N2

    elif N2 >100:
        K2 = 1.08 * N2
        K1 = K2
         
    A1 = round(N1, 5) #结果保留小数后5位
    A2 = round(K1, 5) 
    A3 = round(K2, 5)
    v4.set(str(A1))
    v5.set(str(A2))
    v6.set(str(A3))

           




action = Button(frame, width=9, text="计算结果", command=calc)
action.grid(row=4, column=1)
Button(frame, width=9, text="清空", command=clear).grid(row=4, column=0)

    


win["menu"] = menubar

win.mainloop()

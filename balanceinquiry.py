#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Dec 12, 2020 12:40:56 PM CAT  platform: Windows NT

import sys
import client

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import balanceinquiry_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    balanceinquiry_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    balanceinquiry_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+555+264")
        top.minsize(120, 1)
        top.maxsize(3076, 845)
        top.resizable(1,  1)
        top.title("Balance Inquiry")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.267, rely=0.022, height=41, width=294)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Balance Inquiry''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.167, rely=0.556, height=54, width=177)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Print''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.2, rely=0.222, height=31, width=94)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Name :''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.217, rely=0.333, height=31, width=84)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Balance :''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.417, rely=0.236, height=21, width=264)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text=client.client1.getname())

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.547, rely=0.342, height=21, width=114)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text=client.client1.getbalance())

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.567, rely=0.556, height=54, width=177)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''OK''')

if __name__ == '__main__':
    vp_start_gui()






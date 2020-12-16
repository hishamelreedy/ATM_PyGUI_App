#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Dec 12, 2020 12:27:45 PM CAT  platform: Windows NT

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

import withdraw_support
from tkinter import END
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    withdraw_support.init(root, top)
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
    withdraw_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
def runwithdraw(amount):
    print('client Balance is:',client.client1.getbalance())
    if int(amount[0:len(amount)-1])<client.client1.getbalance() and int(amount[0:len(amount)-1])<=5000:
        print(int(int(amount[0:len(amount)-1])/100))
        client.client1.reduceme(amount=int(int(amount[0:len(amount)-1])/100)*100)
        print('Client Balance now is:',client.client1.getbalance())
        #atm_actuator_out()

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+474+201")
        top.minsize(120, 1)
        top.maxsize(3076, 845)
        top.resizable(0,  0)
        top.title("Withdraw")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.267, rely=0.022, height=51, width=284)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Cash Withdrawal''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.067, rely=0.311, height=41, width=254)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Enter the desired amount:''')

        self.Text2 = tk.Text(top)
        self.Text2.place(relx=0.517, rely=0.333, relheight=0.053, relwidth=0.323)

        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="blue")
        self.Text2.configure(selectforeground="white")
        self.Text2.configure(wrap="word")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.35, rely=0.467, height=54, width=187)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''withdraw''')
        self.Button1.configure(command=lambda: runwithdraw(amount=self.Text2.get('1.0',END)))

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.283, rely=0.644, height=31, width=274)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 14 -weight bold -slant italic")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Thank You''')

if __name__ == '__main__':
    vp_start_gui()






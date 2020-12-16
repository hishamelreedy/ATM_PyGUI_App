import sys
import client
import atmmain_support
import atmmain
global exist
exist=False
global trials
trials=0
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

import main_support
from tkinter import END

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    main_support.init(root, top)
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
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    #global w
    global root
    #w.destroy()
    #w.quit()
    root.quit()
    root.destroy()
    root=None
def impcsv():
    import csv
    with open('clientsdb.csv',newline='')as csvfile:
        reader=csv.DictReader(csvfile)
        ids=[]
        for column in reader:
            ids.append(column['ID'])
    return ids

def checkpass(enteredpass):
    global trials
    if client.client1.getpass()==enteredpass[0:len(enteredpass)-1]:
        print('right')
        atmmain.vp_start_gui()
        destroy_Toplevel1()
    else:
        if(trials==3):
            print('The account is locked, Please go to the branch')
        else:
            print('wrong')
            trials=trials+1

def enterid(id):
    ids = impcsv()
    #ids=[int(item) for item in ids]
    #for i in range(len(ids)):
        #print(ids[i])
    for idno in ids:
        #print(id,idno)
        #print(id[0:len(id)-1],len(id[0:len(id)-1]),idno,len(idno))
        if id[0:len(id)-1]==idno:
            exist=True
            break
        else: 
            exist=False
    if not exist:
        print('this id doesn\'t exist')
    else:
        print('this id exists')
        client.importclientsdb(id[0:len(id)-1])
    

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+491+239")
        top.minsize(120, 1)
        top.maxsize(3076, 845)
        top.resizable(0,  0)
        top.title("Main")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.367, rely=0.044, height=31, width=174)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''ATM''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.117, rely=0.378, height=41, width=104)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Enter ID:''')

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.35, rely=0.4, relheight=0.053, relwidth=0.423)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")
        #self.Text1.configure(text="Text")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.105, rely=0.511, height=21, width=134)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Enter Pass:''')

        self.Text2 = tk.Text(top)
        self.Text2.place(relx=0.35, rely=0.511, relheight=0.053, relwidth=0.423)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="blue")
        self.Text2.configure(selectforeground="white")
        if exist:
            self.Text2.configure(state='disabled')
        self.Text2.configure(wrap="word")

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.333, rely=0.267, height=21, width=204)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 12 -weight bold -slant italic")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Welcome''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.833, rely=0.4, height=24, width=47)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Enter''')
        self.Button1.configure(command=lambda: enterid(id=self.Text1.get('1.0',END)))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.833, rely=0.511, height=24, width=47)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Enter''')
        self.Button2.configure(command= lambda: checkpass(enteredpass=self.Text2.get('1.0',END)))

if __name__ == '__main__':
    vp_start_gui()

#End of File




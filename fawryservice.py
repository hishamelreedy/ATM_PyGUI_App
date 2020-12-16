#Fawry Service PAGE

import sys
import tkinter as tk
import tkinter.ttk as ttk
py3 = True
    
import fawryservice_support
    
def vp_start_gui():
        '''Starting point when module is the main routine.'''
        global val, w, root
        root = tk.Tk()
        top = Toplevel1 (root)
        fawryservice_support.init(root, top)
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
        fawryservice_support.init(w, top, *args, **kwargs)
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
    
            top.geometry("600x450+659+15")
            top.minsize(120, 1)
            top.maxsize(3076, 845)
            top.resizable(0,  0)
            top.title("Fawry Service")
            top.configure(background="#d9d9d9")
    
            self.Label1 = tk.Label(top)
            self.Label1.place(relx=0.217, rely=0.022, height=70, width=354)
            self.Label1.configure(background="#d9d9d9")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(font="-family {Segoe UI} -size 24 -weight bold")
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(text='''Fawry Service''')
    
            self.Button1 = tk.Button(top)
            self.Button1.place(relx=0.083, rely=0.244, height=74, width=207)
            self.Button1.configure(activebackground="#ececec")
            self.Button1.configure(activeforeground="#000000")
            self.Button1.configure(background="#d9d9d9")
            self.Button1.configure(disabledforeground="#a3a3a3")
            self.Button1.configure(font="-family {Segoe UI} -size 14 -weight bold")
            self.Button1.configure(foreground="#000000")
            self.Button1.configure(highlightbackground="#d9d9d9")
            self.Button1.configure(highlightcolor="black")
            self.Button1.configure(pady="0")
            self.Button1.configure(text='''Orange Recharge''')
    
            self.Button2 = tk.Button(top)
            self.Button2.place(relx=0.583, rely=0.244, height=74, width=207)
            self.Button2.configure(activebackground="#ececec")
            self.Button2.configure(activeforeground="#000000")
            self.Button2.configure(background="#d9d9d9")
            self.Button2.configure(disabledforeground="#a3a3a3")
            self.Button2.configure(font="-family {Segoe UI} -size 14 -weight bold")
            self.Button2.configure(foreground="#000000")
            self.Button2.configure(highlightbackground="#d9d9d9")
            self.Button2.configure(highlightcolor="black")
            self.Button2.configure(pady="0")
            self.Button2.configure(text='''Etisalat Recharge''')
    
            self.Vodafone_Recharge = tk.Button(top)
            self.Vodafone_Recharge.place(relx=0.083, rely=0.489, height=74
                   , width=207)
            self.Vodafone_Recharge.configure(activebackground="#ececec")
            self.Vodafone_Recharge.configure(activeforeground="#000000")
            self.Vodafone_Recharge.configure(background="#d9d9d9")
            self.Vodafone_Recharge.configure(disabledforeground="#a3a3a3")
            self.Vodafone_Recharge.configure(font="-family {Segoe UI} -size 14 -weight bold")
            self.Vodafone_Recharge.configure(foreground="#000000")
            self.Vodafone_Recharge.configure(highlightbackground="#d9d9d9")
            self.Vodafone_Recharge.configure(highlightcolor="black")
            self.Vodafone_Recharge.configure(pady="0")
            self.Vodafone_Recharge.configure(text='''Vodafone Recharge''')
   
            self.Button3_1 = tk.Button(top)
            self.Button3_1.place(relx=0.583, rely=0.489, height=74, width=207)
            self.Button3_1.configure(activebackground="#ececec")
            self.Button3_1.configure(activeforeground="#000000")
            self.Button3_1.configure(background="#d9d9d9")
            self.Button3_1.configure(disabledforeground="#a3a3a3")
            self.Button3_1.configure(font="-family {Segoe UI} -size 14 -weight bold")
            self.Button3_1.configure(foreground="#000000")
            self.Button3_1.configure(highlightbackground="#d9d9d9")
            self.Button3_1.configure(highlightcolor="black")
            self.Button3_1.configure(pady="0")
            self.Button3_1.configure(text='''We Recharge''')
   
            self.Text1 = tk.Text(top)
            self.Text1.place(relx=0.517, rely=0.778, relheight=0.053, relwidth=0.257)
   
            self.Text1.configure(background="white")
            self.Text1.configure(font="TkTextFont")
            self.Text1.configure(foreground="black")
            self.Text1.configure(highlightbackground="#d9d9d9")
            self.Text1.configure(highlightcolor="black")
            self.Text1.configure(insertbackground="black")
            self.Text1.configure(selectbackground="blue")
            self.Text1.configure(selectforeground="white")
            self.Text1.configure(wrap="word")
   
            self.Text2 = tk.Text(top)
            self.Text2.place(relx=0.517, rely=0.844, relheight=0.053, relwidth=0.257)
   
            self.Text2.configure(background="white")
            self.Text2.configure(font="TkTextFont")
            self.Text2.configure(foreground="black")
            self.Text2.configure(highlightbackground="#d9d9d9")
            self.Text2.configure(highlightcolor="black")
            self.Text2.configure(insertbackground="black")
            self.Text2.configure(selectbackground="blue")
            self.Text2.configure(selectforeground="white")
            self.Text2.configure(wrap="word")
   
            self.Label2 = tk.Label(top)
            self.Label2.place(relx=0.117, rely=0.778, height=21, width=194)
            self.Label2.configure(background="#d9d9d9")
            self.Label2.configure(disabledforeground="#a3a3a3")
            self.Label2.configure(font="-family {Segoe UI} -size 14 -weight bold")
            self.Label2.configure(foreground="#000000")
            self.Label2.configure(text='''Enter Phone Number''')
   
            self.Label3 = tk.Label(top)
            self.Label3.place(relx=0.1, rely=0.844, height=21, width=234)
            self.Label3.configure(background="#d9d9d9")
            self.Label3.configure(disabledforeground="#a3a3a3")
            self.Label3.configure(font="-family {Segoe UI} -size 14 -weight bold")
            self.Label3.configure(foreground="#000000")
            self.Label3.configure(text='''Enter Recharge Amount''')
   
            self.Button3 = tk.Button(top)
            self.Button3.place(relx=0.533, rely=0.911, height=24, width=137)
            self.Button3.configure(activebackground="#ececec")
            self.Button3.configure(activeforeground="#000000")
            self.Button3.configure(background="#d9d9d9")
            self.Button3.configure(disabledforeground="#a3a3a3")
            self.Button3.configure(foreground="#000000")
            self.Button3.configure(highlightbackground="#d9d9d9")
            self.Button3.configure(highlightcolor="black")
            self.Button3.configure(pady="0")
            self.Button3.configure(text='''Send''')
   
if __name__ == '__main__':
       vp_start_gui()
   
   


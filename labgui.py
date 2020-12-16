from tkinter import *
#Initialize Window
window = Tk()
window.title("Welcome to LikeGeeks app")


#Create Label Widget
lbl = Label(window, text="Hello",padx=5,pady=5)
lbl.grid(column=0, row=7)
lbl = Label(window, text="Hello", font=("Arial Bold", 20))
lbl.grid(column=0, row=8)

#setting Window Size
window.geometry('640x480')

#Adding a button widget
#btn = Button(window, text="Click Me")
#btn.grid(column=1, row=0)

#changing button foreground and background colors
btn = Button(window, text="Click Me", bg="orange", fg="red")
btn.grid(column=1, row=1)

#handle button click event
def clicked():
    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", bg="orange", fg="red",command=clicked)
btn.grid(column=1, row=1)

#Get input using TextBox
txt = Entry(window,width=10)
txt.grid(column=0,row=1)
def clickedwithTB():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)
btn = Button(window,text="CopyTBtoLabel",bg="yellow",fg="green",command=clickedwithTB)
btn.grid(column=2,row=1)
txt.focus()

#Add ComboBox Widget
from tkinter.ttk import *
combo = Combobox(window)
combo['values']=(1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=0)

#Add checkbutton widget 
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text='choose',var=chk_state)
chk.grid(column=0, row=2)

#set check state of a checkbutton
chk_state = IntVar()
chk_state.set(0) #uncheck
chk_state.set(1) #check

#Add radiobutton widgets
rad1 = Radiobutton(window, text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
rad1.grid(column=0, row=3)
rad2.grid(column=1, row=3)
rad3.grid(column=2, row=3)

#Add ScrolledText Widget(Tkinter TextArea)
#scrolledtxt = scrolledtext.ScrolledText(window,width=40,height=10)
#scrolledtxt.insert(INSERT,'Your Text Goes Here')
#txt.delete(1.0,END)

#Create a MessageBox
from tkinter import messagebox
messagebox.showinfo('Message title','Message Content')
messagebox.showwarning('Message title', 'Message content')  #shows warning message
messagebox.showerror('Message title', 'Message content')    #shows error message
res = messagebox.askquestion('Message title','Message content')
res = messagebox.askyesno('Message title','Message content')
res = messagebox.askyesnocancel('Message title','Message content')
res = messagebox.askokcancel('Message title','Message content')
res = messagebox.askretrycancel('Message title','Message content')

#Add a SpinBox
var = IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100)
spin = Spinbox(window, values=(3,8,11), width=5, textvariable=var)

#Add a Progressbar
from tkinter.ttk import Progressbar
from tkinter import ttk
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')
bar = Progressbar(window, length=200,style='black.Horizontal.TProgressbar')
bar['value']=70
bar.grid(column=0,row=5)

#add a filedialog (file&directory chooser)
from tkinter import filedialog
file = filedialog.askopenfilename()
files = filedialog.askopenfilenames()
dir = filedialog.askdirectory()
from os import path
file=filedialog.askopenfilename(initialdir= path.dirname(__file__))

#add a menu bar
from tkinter import Menu
menu = Menu(window)
new_item = Menu(menu)
menu.add_command(label='New')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

#Add a Notebook widget (tab control)
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
#tab_control.pack(expand=1, fill='both')

window.mainloop()


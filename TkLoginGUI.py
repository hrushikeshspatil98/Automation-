#Python Tkinter
#Python provides the standard library Tkinter for creating the graphical user interface for desktop based applications.
""" Steps:
    1) import the Tkinter module.
    2) Create the main application window.
    3) Add the widgets like labels, buttons, frames, etc. to the window.
    4) Call the main event loop so that the actions can take place on the user's computer screen.
"""

#from tkinter import *
from tkinter import Tk
from tkinter import Frame
from tkinter import messagebox
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button

#creating the application main window. 
top=Tk()
top.geometry("500x300")
frame=Frame(top,width=500,height=300,background="orange")

def Login():
    if (uname.get()!="" and len(uname.get())>4 and upass.get()!="" and len(upass.get())>4):
        if (uname.get()=="hrushi" and upass.get()=="12345"):
            messagebox.showinfo("Login","Login Successful...") 
            top.destroy()
        else:
            messagebox.showerror("Login","Invalid Credentials") 
    else:
            messagebox.showerror("Login","Enter valid values") 
        
def Cancel():
    answer = messagebox.askokcancel("Question","Do you want to close window?")
    if answer is True:
        top.destroy()
        
#LABEL WIDGET
lblLogin=Label(top,text="Login",fg="red",font="Centaur 19 bold",background="orange").place(x=225,y=30)

#VARIABLES
uname=StringVar()  #It is placed in widget textvariable attribute
upass=StringVar()

#LABEL WIDGETS
lblUName=Label(top,text="User Name :",fg="dark blue",font="TimesNewRoman 11 bold",bg="orange").place(x=70,y=90)
lblUPass=Label(top,text="Password  :",fg="dark blue",font="TimesNewRoman 11 bold",background="orange").place(x=70,y=140)

#ENTRY WIDGETS
entryUName=Entry(top,width=30,textvariable=uname,font="TimesNewRoman 9 bold").place(x=190,y=90)
entryUPass=Entry(top,width=30,textvariable=upass,show="*",font="TimesNewRoman 9 bold").place(x=190,y=140)

#BUTTON WIDGETS
btnLogin=Button(top,text="Login",font="Century 8 bold",width=10,fg="white",bg="black",command=Login).place(x=190,y=200)
btnCamcel=Button(top,text="Cancel",font="Century 8 bold",width=10,fg="white",bg="black",command=Cancel).place(x=310,y=200)

frame.pack()
top.mainloop()  #Entering the event main loop  

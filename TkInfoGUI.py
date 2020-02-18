from tkinter import *
from tkinter import ttk
#creating the application main window. 
top=Tk()
top.geometry("550x500")
frame=Frame(top,width=550,height=500,background="orange")


#LABEL WIDGET
lblLogin=Label(top,text="Information",fg="red",font="Centaur 19 bold",background="orange").place(x=220,y=30)

#VARIABLES
name=StringVar()  #It is placed in widget textvariable attribute
address=StringVar()
gen=IntVar()
c1=IntVar()
c2=IntVar()
c3=IntVar()
age=IntVar()
country=StringVar()

def submit():
    dname=name.get()
    daddr=address.get()
    
    if(gen.get()==1):
        dgen="Male"
    elif(gen.get()==2):
        dgen="Female"
    else:
        dgen="Other"
    dpl=""
    if(c1.get()==1):
        dpl=dpl+"C "
    if(c2.get()==1):
        dpl=dpl+"C++ "
    if(c3.get()==1):
        dpl=dpl+"Java "
    
    dage=str(age.get())
   
    messagebox.showinfo("Information","Name: "+dname+"\nAdress: "+daddr+"\nGender: "+dgen+"\nCountry: "+country.get()+"\nProg.Lang known: \n"+dpl+"\nAge: "+dage)
    top.destroy()
    
def cancel():
    top.destroy()
#LABEL WIDGETS
lblName=Label(top,text="Name          :",fg="dark blue",font="TimesNewRoman 11 bold",bg="orange").place(x=80,y=90)
lblUAdd=Label(top,text="Address      :",fg="dark blue",font="TimesNewRoman 11 bold",background="orange").place(x=80,y=140)
lblGender=Label(top,text="Gender       :",fg="dark blue",font="TimesNewRoman 11 bold",bg="orange").place(x=80,y=190)
lblCountry=Label(top,text="Country       :",fg="dark blue",font="TimesNewRoman 11 bold",bg="orange").place(x=80,y=240)
lblPL=Label(top,text="Prog.Lang   : ",fg="dark blue",font="TimesNewRoman 11 bold",bg="orange").place(x=80,y=290)
lblAge=Label(top,text="Age              :",fg="dark blue",font="TimesNewRoman 11 bold",bg="orange").place(x=80,y=340)

#ENTRY WIDGETS
entryName=Entry(top,width=30,textvariable=name,font="TimesNewRoman 9 bold").place(x=210,y=90)
entryAdd=Entry(top,width=30,textvariable=address,font="TimesNewRoman 9 bold").place(x=210,y=140)
#Radiobutton Widget
R1 = Radiobutton(top, text="Male", variable=gen, value=1,  
                  bg="orange").place(x=210,y=190) 
 
R2 = Radiobutton(top, text="Female", variable=gen, value=2,  
                  bg="orange").place(x=290,y=190) 

R3 = Radiobutton(top, text="Other", variable=gen, value=3,  
                  bg="orange").place(x=370,y=190)   

countries=["India","USA","Austrelia","Afganistan","Japan"]
#Combobox widget
cbCountry=ttk.Combobox(top,values=countries,textvariable=country).place(x=210,y=240)
#Checkbutton widget
cb1=Checkbutton(top,text="C",variable=c1,onvalue=1,offvalue=0,height = 2, width = 10,bg="orange").place(x=180,y=280)
cb2=Checkbutton(top,text=" C++",variable=c2,onvalue=1,offvalue=0,height = 2, width = 10,bg="orange").place(x=260,y=280)
cb3=Checkbutton(top,text=" Java",variable=c3,onvalue=1,offvalue=0,height = 2, width = 10,bg="orange").place(x=340,y=280)
 
scale = Scale( top, variable = age, from_ = 1, to = 100, orient = HORIZONTAL,bg="orange").place(x=210,y=330)
#BUTTON WIDGETS
btnSubmit=Button(top,text="Submit",font="Century 8 bold",width=10,fg="white",bg="black",command=submit).place(x=210,y=400)
btnCamcel=Button(top,text="Cancel",font="Century 8 bold",width=10,fg="white",bg="black",command=cancel).place(x=330,y=400)

frame.pack()
top.mainloop()  #Entering the event main loop  

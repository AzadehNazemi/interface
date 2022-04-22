from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter as Tkinter
from tkinter.messagebox import showinfo
from tkcalendar import Calendar
import tkinter.simpledialog  as tkSimpleDialog
from PIL import ImageTk, Image
import numpy as np


def create_widgets(ti):
    def ok_clicked():
   
        print(value_inside1.get(),amount.get(),descri.get(),sd.get()    )
        
        
        Label(tab,text=sd.get()).place(x=350,y=30*  (rowno))
        
        Label(tab,text=value_inside1.get()).place(x=450,y=30*  (rowno))
        
        Label(tab,text=descri.get()).place(x=700,y=30*  (rowno))
        
        Label(tab,text=amount.get()).place(x=570,y=30*  (rowno))
        
        return sd.get()
        
    options_list1 =  ('Weekly','Forthnightly','Monthly','Quaterly','Annually')
    
        

    tab =Toplevel()
    tab.geometry("1000x"+str(len(ti)*150))
          
    tab.title('Bill Detail')
    Label(tab,text='Bill').place(x=10,y=0)
    Label(tab,text='Amount').place(x=570,y=0)
    Label(tab,text='Start Date').place(x=350,y=0)
    Label(tab,text='Frequency').place(x=450,y=0)
    Label(tab,text='Desciption').place(x=700,y=0)
    cdd=tkSimpleDialog.Dialog  
    sd=StringVar()
   

    
    Calendar(tab,textvariable=sd).place(x=150,y=30)
   
    for i in range (len ( ti)):
        Label(tab,text= ti[i]).place(x=10,y=(1+i)*30)
        # startDate     =cd.selection_get''()   
     #       cd = CalendarDialog(tab)                      
      # #  startDate=cd.result
        # timestampStr =startDate.strftime("%d-%b-%Y")


        amount = IntVar()
        # sd=StringVar()
        value_inside1 = StringVar()
        descri=StringVar()
        value_inside1.set("Bill Frequency")
        OptionMenu(tab, value_inside1, *options_list1).place(x=450,y=30*(i+1))
    
     
        Entry(tab, textvariable=amount).place(x=570,y=(i+1)*30) 
        Entry(tab, textvariable=descri).place(x=700,y=(i+1)*30)
        rowno=i
        Button(tab, text="Ok", command=ok_clicked).place(x=820,y=30*(i+1)) 
               
        
        
        
    tab.mainloop()    
   
class CalendarDialog(tkSimpleDialog.Dialog):
    
    def body(self, master):
        self.calendar =Calendar(master)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection_get()


class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)
     
    def state(self):
      return map((lambda var: var.get()), self.vars)

def all():
         
    ti=[]     
    chk1=list(home.state())
    chk2=list(car.state())
    chk3=list(util.state())
    chk4=list(health.state())
    chk5=list(credit.state())
    chk6=list(entertainment.state())
    
    for i in range(len(chk1)):
        if chk1[i]==1:
      
            titleb=(options1[i])
            ti.append(titleb)
            
    for i in range(len(chk2)):
        if chk2[i]==1:
      
            titleb=(options2[i])
            ti.append(titleb)
    for i in range(len(chk3)):
        if chk3[i]==1:
      
            titleb=(options3[i])        
            ti.append(titleb)
    for i in range(len(chk4)):
        if chk4[i]==1:
      
            titleb=(options4)            
            ti.append(titleb)
    for i in range(len(chk5)):
        if chk5[i]==1:
      
            titleb=(options5)
            ti.append(titleb)
    for i in range(len(chk6)):
        if chk6[i]==1:
      
            titleb=(options6)    
            ti.append(titleb)
    
    
    create_widgets(ti)  
    
root = Tk()

root.geometry("800x600")
root.title("Managing Bills")

home = Checkbar(root,  ["Mortgate Fixed","Mortgate Variable","Home Insurance","Home Rate","Sterata","Pest Control"])
health=Checkbar(root,["Health Insurance"]) 
car = Checkbar(root, ["Car Insurance","Car Registeration"]) 
util=Checkbar(root ,["Electricity","Water","Gas","Phone","Internet"])
credit=Checkbar(root,["Credit Card"])
entertainment=Checkbar(root,["Entertianment"])

home.place(x=70,y=10)
car.place(x=70,y=100)
util.place(x=70,y=200)
health.place(x=70,y=300 )
credit.place(x=70,y=400 )
entertainment.place(x=70,y=500 )

img = ImageTk.PhotoImage(Image.open("PyAus_logo_small.png"))
imgh = ImageTk.PhotoImage(Image.open("home_re.png"))
imgc = ImageTk.PhotoImage(Image.open("car_re.png"))
imgu = ImageTk.PhotoImage(Image.open("util_re.png"))
imgi = ImageTk.PhotoImage(Image.open("health_insurance_re.png"))
imgcc = ImageTk.PhotoImage(Image.open("cc_re.png"))
imge = ImageTk.PhotoImage(Image.open("entertain_re.png"))

frame = Frame(root)
frame.pack()
frame.place(anchor='ne', relx=1, rely=0)
label = Label(frame, image = img)
label.pack()

label1= Label(root, image = imgh).place(x=0,y=10)
label2= Label(root, image = imgc).place(x=0,y=100)
label3= Label(root, image = imgu).place(x=0,y=200)
label4= Label(root, image = imgi).place(x=0,y=300)
label5= Label(root, image = imgcc).place(x=0,y=400)
label6 = Label(root, image = imge   ).place(x=0,y=500)

            
options1 =  ("Mortgate Fixed","Mortgate Variable","Home Insurance","Home Rate","Sterata","Pest Control" )
options2=("Car Insurance","Car Registeration")
options3=("Electricity","Water","Gas","Phone","Internet")
options4=("Health Insurance")
options5=("Credit Card")
options6=("Entertianment")
Button(root, text='Quit  ', command=root.quit).place(x=740,y=580)
Button(root, text='Select', command=all).place(x=740,y=560)

root.mainloop()  
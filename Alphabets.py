from tkinter import *
from PIL import ImageTk, Image

import winsound
winsound.PlaySound("kryptic_minds.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP )

def raise_frame(frame):
    frame.tkraise()

    
f=open("intro1.txt","r")
intr=f.read()
f.close()

f=open("x.txt","r")
x=f.read()
f.close() 

f=open("a1.txt","r")
a1=f.read()
f.close()    

f=open("a2.txt","r")
a2=f.read()
f.close()    

f=open("b1.txt","r")
b1=f.read()
f.close()    

f=open("b2.txt","r")
b2=f.read()
f.close()    

f=open("c1.txt","r")
c1=f.read()
f.close()

f=open("c2.txt","r")
c2=f.read()
f.close()

f=open("d1.txt","r")
d1=f.read()
f.close()

f=open("d2.txt","r")
d2=f.read()
f.close() 

f=open("e.txt","r")
e=f.read()
f.close()

f=open("k1.txt","r")
k1=f.read()
f.close()

f=open("k2.txt","r")
k2=f.read()
f.close()

f=open("z.txt","r")
z=f.read()
f.close()

f=open("x1.txt","r")
x1=f.read()
f.close() 

f=open("x2.txt","r")
x2=f.read()
f.close() 

f=open("x3.txt","r")
x3=f.read()
f.close() 

f=open("x4.txt","r")
x4=f.read()
f.close() 

root2 = Toplevel()
root2.geometry('2000x2000')
root2.state("zoomed")

f0=Frame(root2)
intro=Frame(root2)
f1 = Frame(root2)
f2 = Frame(root2)
f3 = Frame(root2)
f4 = Frame(root2)
f5 = Frame(root2)
f6=Frame(root2)
f7=Frame(root2)
f8=Frame(root2)
f9=Frame(root2)
f10=Frame(root2)
f11=Frame(root2)
f12=Frame(root2)
f13=Frame(root2)
f14=Frame(root2)
f15=Frame(root2)
f16=Frame(root2)
f17=Frame(root2)



for frame in (f0,intro,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17):
    frame.grid(row=8000, column=8000, sticky='news')

load1 = Image.open("hack.png")
render1 = ImageTk.PhotoImage(load1)
for i in (f0,intro,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17):
    img = Label(i, image=render1)
    img.image = render1
    img.place(x=0, y=0)


def FAQ():
    
    def pin():
        
        if e2.get() in ["hacking","honeytrap","server"]:
           raise_frame(f14)
           Label(f14,text=x1,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=50)
           Button(f14,text="END",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=root2.destroy).pack(padx=550)

        elif e2.get() in["backstory","past"]:
            raise_frame(f15)
            Label(f15,text=x2,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
            Button(f15,text="END",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=root2.destroy).pack(padx=550,pady=100)

        elif e2.get() in ["depression","mental health"]:
            raise_frame(f16)
            l7=Label(f16,text=x3,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
            Button(f16,text="END",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=root2.destroy).pack(padx=550,pady=100)

        else:
            raise_frame(f17)
            Label(f17,text=x4,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
            Button(f17,text="END",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=root2.destroy).pack(padx=550,pady=100)


        return

    raise_frame(f13)
    
    l3=Label(f13,text="Want to know more about THE ALPHABETS?",font=("Monotype Corsiva",35,"bold"),fg="white",bg="black").pack(padx=400,pady=100)

    l4=Label(f13,text="Enter what you are curious to know!",font=("Monotype Corsiva",25,"bold"),fg="white",bg="black").pack(padx=400)

    e2=Entry(f13,width=40,font=("Arial",20,"bold"))
    e2.pack(padx=400,pady=100)

    Button(f13,text="NEXT",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=pin).pack(padx=400,pady=100)



def end():
    raise_frame(f12)
    label=Label(f12, text=z,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
    Button(f12,text="NEXT",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=FAQ).pack(padx=550,pady=100)
#--------------------------------------------
def gbel():
    raise_frame(f10)
    label=Label(f10, text=k1,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
    Button(f10,text="NEXT",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=end).pack(padx=550,pady=100)
def gdbel():
    raise_frame(f11)
    label=Label(f11, text=k2,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
    Button(f11,text="NEXT",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=end).pack(padx=550,pady=100)
#-----------------------------------------------------------
def iin():
    raise_frame(f8)
    label=Label(f8, text=d1,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
    Button(f8,text="Gaya believes",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=gbel).pack(padx=550)
    Button(f8,text="Gaya do not believe",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=gdbel).pack(padx=550)
#--------------------------------------------------------------------
def iout():
    raise_frame(f9)
    label=Label(f9, text=d2,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
    Button(f9,text="Gaya believes",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=gbel).pack(padx=550)
    Button(f9,text="Gaya do not believe",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=gdbel).pack(padx=550)
#----------------------------------------------------------------
def hack():
    raise_frame(f7)
    label=Label(f7, text=c2,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
    Button(f7,text="Gaya believes",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=gbel).pack(padx=550)
    Button(f7,text="Gaya do not believe",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=gdbel).pack(padx=550)
#--------------------------------------------------------------
def nohack():
    raise_frame(f6)
    label=Label(f6, text=c1,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
    Button(f6,text="Gaya believes",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=gbel).pack(padx=550)
    Button(f6,text="Gaya do not believe",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=gdbel).pack(padx=550)

#-------------------------------------------------------------
def op1():
    #take pill
    raise_frame(f4)
    label=Label(f4, text=b1,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
    Button(f4,text="No Hack",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=nohack).pack(padx=550)
    Button(f4,text="Hack",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=hack).pack(padx=550)
   
    
#------------------------------------------------------------------------------------------------------------------------------
def op2():
    #do not take pill
    raise_frame(f5)
    Label(f5, text=b2,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
    Button(f5,text="I am in",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=iin).pack(padx=550)
    Button(f5,text="I am out",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=iout).pack(padx=550)
#----------------------------------------------------------------------
def takep():
    raise_frame(f2)
    label=Label(f2, text=a1,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
    Button(f2,text="Take pill",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=op1).pack(padx=550)
    Button(f2,text="Do not take pill",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=op2).pack(padx=550)
    
#-----------------------------------------------------------------------------------------------------------------------------------
def dtakep():
    raise_frame(f3)
    label=Label(f3, text=a2,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=400,pady=100)
    Button(f3,text="Take pill",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=op1).pack(padx=400)
    Button(f3,text="Do not take pill",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=op2).pack(padx=400)
#----------------------------------------------------------------
raise_frame(f0)
label=Label(f0,text="THE ALPHABETS",font=("Examples of erosion",80,"bold"),fg="white",bg="black").pack(padx=500,pady=100)
Button(f0,text='NEXT',font=("Monotype Corsiva",20,"bold"),fg="white",bg="black",command=lambda:raise_frame(intro)).pack(padx=500)

label=Label(intro, text=a1,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
Button(intro,text='NEXT',font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=lambda:raise_frame(f1)).pack(padx=800)
label=Label(intro,bg="black").pack(padx=800,pady=800)
label=Label(f1, text=x,font=("Monotype Corsiva",18,"bold"),fg="white",bg="black").pack(padx=550,pady=100)
Button(f1,text="Take project",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=takep).pack(padx=550)
Button(f1,text="Do not take Project",font=("Monotype Corsiva",18,"bold"),fg="white",bg="black",command=dtakep).pack(padx=550)
   

#-----------------------------------------------------------------------------------------------------------------------------------


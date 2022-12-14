from tkinter import *
from PIL import ImageTk, Image

import winsound
winsound.PlaySound("The_Secret_History.wav", winsound.SND_ASYNC | winsound.SND_ALIAS | winsound.SND_LOOP )

f=open("Intro.txt","r",encoding='utf8')
abc=f.read()
f.close()

f=open("story1.1.txt","r",encoding='utf-8')
a=f.read()
f.close()

f=open("story1.2.txt","r",encoding='utf-8')
b=f.read()
f.close()

f=open("story1.3.txt","r",encoding='utf-8')
c=f.read()
f.close()

f=open("story1.4.txt","r",encoding='utf-8')
d=f.read()
f.close()

f=open("story1.5(a).txt","r",encoding='utf-8')
e=f.read()
f.close()

f=open("story1.6(a).txt","r",encoding='utf-8')
g=f.read()
f.close()

f=open("story1.7(a)i.txt","r",encoding='utf-8')
h=f.read()
f.close()

f=open("story1.8(a)i.txt","r",encoding='utf-8')
aak=f.read()
f.close()

f=open("story1.9(a)i.txt","r",encoding='utf-8')
aal=f.read()
f.close()

f=open("story1.7(a)ii.txt","r",encoding='utf-8')
q=f.read()
f.close()

f=open("story1.8(a)ii.txt","r",encoding='utf-8')
aam=f.read()
f.close()

f=open("story1.9(a)ii.txt","r",encoding='utf-8')
aan=f.read()
f.close()

f=open("story1.5(e).txt","r",encoding='utf-8')
r=f.read()
f.close()

f=open("story1.6(e).txt","r",encoding='utf-8')
s=f.read()
f.close()

f=open("story1.7(e).txt","r",encoding='utf-8')
t=f.read()
f.close()

f=open("story1.8(e).txt","r",encoding='utf-8')
u=f.read()
f.close()

f=open("story1.9(e)i.txt","r",encoding='utf-8')
v=f.read()
f.close()

f=open("story1.10(e)i.txt","r",encoding='utf-8')
w=f.read()
f.close()

f=open("story1.9(e)ii.txt","r",encoding='utf-8')
x=f.read()
f.close()

f=open("story1.10(e)ii.txt","r",encoding='utf-8')
y=f.read()
f.close()

f=open("story1.5(n).txt","r",encoding='utf-8')
z=f.read()
f.close()

f=open("story1.6(n).txt","r",encoding='utf-8')
aa=f.read()
f.close()

f=open("story1.7(n)i.txt","r",encoding='utf-8')
ab=f.read()
f.close()

f=open("story1.8(n)i.txt","r",encoding='utf-8')
ac=f.read()
f.close()

f=open("story1.9(n)i.txt","r",encoding='utf-8')
ad=f.read()
f.close()

f=open("story1.10(n)i.txt","r",encoding='utf-8')
ae=f.read()
f.close()

f=open("story1.7(n)ii.txt","r",encoding='utf-8')
af=f.read()
f.close()

f=open("story1.8(n)ii.txt","r",encoding='utf-8')
ag=f.read()
f.close()

f=open("story1.9(n)ii.txt","r",encoding='utf-8')
ah=f.read()
f.close()

f=open("story1.10(n)ii.txt","r",encoding='utf-8')
ai=f.read()
f.close()

f=open("story1.11.txt","r",encoding='utf-8')
aj=f.read()
f.close()

f=open("story1.12.txt","r",encoding='utf-8')
ak=f.read()
f.close()

f=open("story1.13.txt","r",encoding='utf-8')
al=f.read()
f.close()

f=open("story1.14.txt","r",encoding='utf-8')
am=f.read()
f.close()

f=open("story1.15.txt","r",encoding='utf-8')
an=f.read()
f.close()

f=open("story1.16i.txt","r",encoding='utf-8')
ao=f.read()
f.close()

f=open("story1.17i.txt","r",encoding='utf-8')
ap=f.read()
f.close()

f=open("story1.18i.1.txt","r",encoding='utf-8')
aq=f.read()
f.close()

f=open("story1.19i.1.1.txt","r",encoding='utf-8')
ar=f.read()
f.close()

f=open("story1.19i.1.2.txt","r",encoding='utf-8')
at=f.read()
f.close()

f=open("story1.18i.2.txt","r",encoding='utf-8')
au=f.read()
f.close()

f=open("story1.16ii.txt","r",encoding='utf-8')
av=f.read()
f.close()

f=open("story1.17ii.txt","r",encoding='utf-8')
aw=f.read()
f.close()

f=open("story1.20.txt","r",encoding='utf-8')
ax=f.read()
f.close()

f=open("story1.21.txt","r",encoding='utf-8')
ay=f.read()
f.close()

f=open("story1.22.txt","r",encoding='utf-8')
az=f.read()
f.close()

f=open("story1.24(a).txt","r",encoding='utf-8')
aab=f.read()
f.close()

f=open("story1.25(a).txt","r",encoding='utf-8')
aac=f.read()
f.close()

f=open("story1.26(a).txt","r",encoding='utf-8')
aad=f.read()
f.close()

f=open("story1.24(e).txt","r",encoding='utf-8')
aae=f.read()
f.close()

f=open("story1.25(e).txt","r",encoding='utf-8')
aaf=f.read()
f.close()

f=open("story1.24(n).txt","r",encoding='utf-8')
aag=f.read()
f.close()

f=open("story1.25(n).txt","r",encoding='utf-8')
aah=f.read()
f.close()

f=open("story1.letter.txt","r",encoding='utf-8')
aai=f.read()
f.close()

f=open("story1.gameover.txt","r",encoding='utf-8')
aaj=f.read()
f.close()

sa=5
se=5
sn=5

def raise_frame(frame):
    frame.tkraise()

root = Toplevel()
root.configure(bg="black")
root.geometry('2000x2000')
root.state('zoomed')

f = Frame(root)
f0 = Frame(root)
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

f5a = Frame(root)
f6a = Frame(root)
f7ai = Frame(root)
f7aii = Frame(root)

f8ai = Frame(root)
f8aii = Frame(root)  
f9ai = Frame(root)
f9aii = Frame(root)

f5e = Frame(root)
f6e = Frame(root)
f7e = Frame(root)
f8e = Frame(root)
f9ei = Frame(root)
f10ei = Frame(root)
f9eii = Frame(root)
f10eii = Frame(root)

f5n = Frame(root)
f6n = Frame(root)
f7ni = Frame(root)
f7nii = Frame(root)
f8ni = Frame(root)
f9ni = Frame(root)
f10ni = Frame(root)
f8nii = Frame(root)
f9nii = Frame(root)
f10nii = Frame(root)

fne = Frame(root)
fae = Frame(root)
fan = Frame(root)
fa = Frame(root)
fe = Frame(root)
fn = Frame(root)

f11 = Frame(root)
f12 = Frame(root)
f13 = Frame(root)
f14 = Frame(root)
f15 = Frame(root)

f16i = Frame(root)
f17i = Frame(root)
f18i1 = Frame(root)
f18i2 = Frame(root)
f19i11 = Frame(root)
f19i12 = Frame(root)
f16ii = Frame(root)
f17ii = Frame(root)

f20 = Frame(root)
f21 = Frame(root)
f22 = Frame(root)
f23 = Frame(root)
fss = Frame(root)

f24a = Frame(root)
f25a = Frame(root)
f26a = Frame(root)
f24e = Frame(root)  
f25e = Frame(root)
f24n = Frame(root)
f25n = Frame(root)

fletter = Frame(root)
fover = Frame(root)


for frame in (f, f0, f1, f2, f3, f4, f5a, f6a, f7ai, f7aii, f8ai, f8aii, f9ai, f9aii, f5e, f6e ,f7e, f8e, f9ei, f10ei, f9eii, f10eii, f5n, f6n, f7ni, f7nii, f8ni, f9ni, f10ni, f8nii,
              f9nii, f10nii, fne, fae, fan, fa, fe, fn, f11 , f12, f13, f14, f15, f16i, f17i, f16ii, f17ii, f18i1, f18i2, f19i11, f19i12, f20, f21, f22, f23 ,f24a, f25a, f26a, f24e,
              f25e, f24n, f25n, fletter, fover, fss ):

    frame.grid(row=800, column=800, sticky='news')


load1 = Image.open("glass90.png")
render1 = ImageTk.PhotoImage(load1)
for i in (root, f, f0, f1, f2, f3, f4, f5a, f6a, f7ai, f7aii, f8ai, f8aii, f9ai, f9aii, f5e, f6e ,f7e, f8e, f9ei, f10ei, f9eii, f10eii, f5n, f6n, f7ni, f7nii, f8ni, f9ni, f10ni, f8nii,
              f9nii, f10nii, fne, fae, fan, fa, fe, fn, f11 , f12, f13, f14, f15, f16i, f17i, f16ii, f17ii, f18i1, f18i2, f19i11, f19i12, f20, f21, f22, f23 ,f24a, f25a, f26a, f24e,
              f25e, f24n, f25n, fletter, fover, fss ):
    img = Label(i, image=render1)
    img.image = render1
    img.place(x=0, y=0)


aaa=IntVar()
eee=IntVar()
nnn=IntVar()


def some():
    if aaa.get()==1 and eee.get()!=2 and nnn.get()!=3:
        raise_frame(fne)
        label=Label(fne, text="  ",background="black").pack(pady=120)
        label=Label(fne, text="  ",background="black").pack()
        label=Label(fne, text="Whom do you want to interrogate next",font=(15),fg="white",background="black").pack()
        label=Label(fne, text="  ",background="black").pack()
        Radiobutton(fne, text='Emil Ray',font=(15),fg="white",background="black", command=lambda:raise_frame(f5e),value=2,variable=eee).pack()
        Radiobutton(fne, text='Nachiket Mukund',font=(15),fg="white",background="black", command=lambda:raise_frame(f5n),value=3,variable=nnn).pack()

    elif aaa.get()!=1 and eee.get()==2 and nnn.get()!=3:
        raise_frame(fan)
        label=Label(fan, text="  ",background="black").pack(pady=120)
        label=Label(fan, text="  ",background="black").pack()
        label=Label(fan, text="Whom do you want to interrogate next",font=(15),fg="white",background="black").pack()
        label=Label(fan, text="  ",background="black").pack()
        Radiobutton(fan, text='Arushi Chauhan',font=(15),fg="white",background="black", command=lambda:raise_frame(f5a),value=1,variable=aaa).pack()
        Radiobutton(fan, text='Nachiket Mukund',font=(15),fg="white",background="black", command=lambda:raise_frame(f5n),value=3,variable=nnn).pack()

    elif aaa.get()!=1 and eee.get()!=2 and nnn.get()==3:
        raise_frame(fae)
        label=Label(fae, text="  ",background="black").pack(pady=120)
        label=Label(fae, text="  ",background="black").pack()
        label=Label(fae, text="Whom do you want to interrogate next",font=(15),fg="white",background="black").pack()
        label=Label(fae, text="  ",background="black").pack()
        Radiobutton(fae, text='Arushi Chauhan',font=(15),fg="white",background="black", command=lambda:raise_frame(f5a),value=1,variable=aaa).pack()
        Radiobutton(fae, text='Emil Ray',font=(15),fg="white",background="black", command=lambda:raise_frame(f5e),value=2,variable=eee).pack()

    elif aaa.get()!=1 and eee.get()==2 and nnn.get()==3:
        raise_frame(fa)
        label=Label(fa, text="  ",background="black").pack(pady=120)
        label=Label(fa, text="  ",background="black").pack()
        label=Label(fa, text="Whom do you want to interrogate next",font=(15),fg="white",background="black").pack()
        label=Label(fa, text="  ",background="black").pack()
        Radiobutton(fa, text='Arushi Chauhan',font=(15),fg="white",background="black", command=lambda:raise_frame(f5a),value=1,variable=aaa).pack()

    elif aaa.get()==1 and eee.get()!=2 and nnn.get()==3:
        raise_frame(fe)
        label=Label(fe, text="  ",background="black").pack(pady=120)
        label=Label(fe, text="  ",background="black").pack()
        label=Label(fe, text="Whom do you want to interrogate next",font=(15),fg="white",background="black").pack()
        label=Label(fe, text="  ",background="black").pack()
        Radiobutton(fe, text='Emil Ray',font=(15),fg="white",background="black", command=lambda:raise_frame(f5e),value=2,variable=eee).pack()

    elif aaa.get()==1 and eee.get()==2 and nnn.get()!=3:
        raise_frame(fn)
        label=Label(fn, text="  ",background="black").pack(pady=120)
        label=Label(fn, text="  ",background="black").pack()
        label=Label(fn, text="Whom do you want to interrogate next",font=(15),fg="white",background="black").pack()
        label=Label(fn, text="  ",background="black").pack()
        Radiobutton(fn, text='Nachiket Mukund',font=(15),fg="white",background="black", command=lambda:raise_frame(f5n),value=3,variable=nnn).pack()
    
    else:
        raise_frame(f11)
        Label(f11, text=aj,font=(15),fg="white",background="black").pack(pady=45)
        Button(f11, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f12)).pack()

        
#-------------------------------------------------------Name----------------------------------------------------------------
        
Label(f, text='The Murder of Alok',font=('Butcher The Baker',70),fg="white",background="black").pack(pady=150)
Button(f, text='Next',font=(15),fg="white",background="black", command=lambda:raise_frame(f0)).pack()

#-------------------------------------------------------INTRODUCTION--------------------------------------------------------------

Label(f0, text=abc,font=(20),fg="white",background="black").pack(pady=90)
name=Entry(f0,font=("Arial",15))
name.pack()

def decname():
    dec=name.get()
    x='''Detective '''+dec
    f=open("Previous_Invetigators.txt","a")
    f.write("\n")
    f.write("*****************************************")
    f.write("\n")
    f.write(x)
    f.write("\n")
    f.write("*****************************************")
    f.write("\n")
    f.close()
    
Button(f0, text='Next',font=(15),fg="white",background="black", command=lambda:raise_frame(f1)).pack(pady=60)

Label(f1, text=a,font=(15),fg="white",background="black").pack(pady=90)
Button(f1, text='Next',font=(15),fg="white",background="black", command=lambda:raise_frame(f2)).pack()

Label(f2, text=b,font=(15),fg="white",background="black").pack(pady=90)
Button(f2, text='Next',font=(15),fg="white",background="black", command=lambda:raise_frame(f3)).pack()

Label(f3, text=c,font=(15),fg="white",background="black").pack(pady=80)
Button(f3, text='Next',font=(15),fg="white",background="black", command=lambda:raise_frame(f4)).pack(padx=700,pady=25)

Label(f4, text=d,font=(15),fg="white",background="black").pack(pady=90)
Radiobutton(f4, text='Aarushi Chauhan',font=(15),fg="white",background="black", command=lambda:raise_frame(f5a),value=1,variable=aaa).pack()
Radiobutton(f4, text='Emil Ray',font=(15),fg="white",background="black", command=lambda:raise_frame(f5e),value=2,variable=eee).pack()
Radiobutton(f4, text='Nachiket Mukund',font=(15),fg="white",background="black", command=lambda:raise_frame(f5n),value=3,variable=nnn).pack()

#------------------------------------------------------Aarushi---------------------------------------------------------------

Label(f5a, text=e,font=(15),fg="white",background="black").pack(pady=90)
Button(f5a, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f6a)).pack()

opt1='''We’d like to know whom you suspect.
That is, if you were close to Mr. Alok.'''

opt2='''Your answers seem a bit… rehearsed.
You also seem oddly calm for someone
whose roommate died not many hours ago.'''

j=IntVar()

Label(f6a, text=g,font=(15),fg="white",background="black").pack(pady=45)
Radiobutton(f6a, text=opt1,font=(15),fg="white",background="black", command=lambda:raise_frame(f7ai),value=1,variable=j).pack()
Radiobutton(f6a, text=opt2,font=(15),fg="white",background="black", command=lambda:raise_frame(f7aii),value=2,variable=j).pack()

Label(f7ai, text=h,font=(15),fg="white",background="black").pack(pady=90)
Button(f7ai, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f8ai)).pack()

Label(f7aii, text=q,font=(15),fg="white",background="black").pack(pady=90)
Button(f7aii, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f8aii)).pack()

Label(f8ai, text=aak,font=(15),fg="white",background="black").pack(pady=90)
Button(f8ai, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f9ai)).pack()

Label(f8aii, text=aam,font=(15),fg="white",background="black").pack(pady=45)
Button(f8aii, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f9aii)).pack()

Label(f9ai, text=aal,font=(15),fg="white",background="black").pack(pady=45)
Button(f9ai, text='Next', font=(15),fg="white",background="black", command=some).pack()

Label(f9aii, text=aan,font=(15),fg="white",background="black").pack(pady=45)
Button(f9aii, text='Next', font=(15),fg="white",background="black", command=some).pack()

#------------------------------------------------------Emil------------------------------------------------------------------

Label(f5e, text=r,font=(15),fg="white",background="black").pack(pady=45)
Button(f5e, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f6e)).pack()

Label(f6e, text=s,font=(15),fg="white",background="black").pack(pady=45)
Button(f6e, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f7e)).pack()

Label(f7e, text=t,font=(15),fg="white",background="black").pack(pady=45)
Button(f7e, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f8e)).pack()

opt3='Why did you come back?'
opt4='Why did you lie about not coming back?'

k=IntVar()

Label(f8e, text=u,font=(15),fg="white",background="black").pack(pady=45)
Radiobutton(f8e, text=opt3,font=(15),fg="white",background="black", command=lambda:raise_frame(f9ei),value=1,variable=k).pack()
Radiobutton(f8e, text=opt4,font=(15),fg="white",background="black", command=lambda:raise_frame(f9eii),value=2,variable=k).pack()
   
Label(f9ei, text=v,font=(15),fg="white",background="black").pack(pady=45)
Button(f9ei, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f10ei)).pack(pady=45)

Label(f9eii, text=x,font=(15),fg="white",background="black").pack(pady=45)
Button(f9eii, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f10eii)).pack()

Label(f10ei, text=w,font=(15),fg="white",background="black").pack(pady=45)
Button(f10ei, text='Next', font=(15),fg="white",background="black", command=some).pack()

Label(f10eii, text=y,font=(15),fg="white",background="black").pack(pady=45)
Button(f10eii, text='Next', font=(15),fg="white",background="black", command=some).pack()

#-------------------------------------------------------Nachiket------------------------------------------------------------

Label(f5n, text=z,font=(15),fg="white",background="black").pack(pady=45)
Button(f5n, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f6n)).pack()

opt5='Pressurize'
opt6='Comfort'

m=IntVar()

Label(f6n, text=aa,font=(15),fg="white",background="black").pack(pady=45)
Radiobutton(f6n, text=opt5,font=(15),fg="white",background="black", command=lambda:raise_frame(f7ni),value=1,variable=m).pack()
Radiobutton(f6n, text=opt6,font=(15),fg="white",background="black", command=lambda:raise_frame(f7nii),value=2,variable=m).pack()

Label(f7ni, text=ab,font=(15),fg="white",background="black").pack(pady=45)
Button(f7ni, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f8ni)).pack()

Label(f8ni, text=ac,font=(15),fg="white",background="black").pack(pady=45)
Button(f8ni, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f9ni)).pack()

Label(f9ni, text=ad,font=(15),fg="white",background="black").pack(pady=45)
Button(f9ni, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f10ni)).pack()

Label(f10ni, text=ae,font=(15),fg="white",background="black").pack(pady=45)
Button(f10ni, text='Next', font=(15),fg="white",background="black", command=some).pack()

Label(f7nii, text=af,font=(15),fg="white",background="black").pack(pady=45)
Button(f7nii, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f8nii)).pack()

Label(f8nii, text=ag,font=(15),fg="white",background="black").pack(pady=45)
Button(f8nii, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f9nii)).pack()

Label(f9nii, text=ah,font=(15),fg="white",background="black").pack(pady=45)
Button(f9nii, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f10nii)).pack()

Label(f10nii, text=ai,font=(15),fg="white",background="black").pack(pady=45)
Button(f10nii, text='Next', font=(15),fg="white",background="black", command=some).pack()

#----------------------------------------------------Common------------------------------------------------------------

Label(f12, text=ak,font=(15),fg="white",background="black").pack(pady=45)
Button(f12, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f13)).pack()

Label(f13, text=al,font=(15),fg="white",background="black").pack(pady=45)
Button(f13, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f14)).pack()

Label(f14, text=am,font=(15),fg="white",background="black").pack(pady=45)
Button(f14, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f15)).pack()

opt7='''Yes, he put a lot of pressure on the throat.
So it wouldn’t be a surprise if he used his
knees and weight as an advantage.'''

opt8='''No; that would mean he had to jump on Alok’s
hands and strangulate him at the same time to
prevent him from defending himself or screaming.'''

o=IntVar()

Label(f15, text=an,font=(15),fg="white",background="black").pack(pady=45)
Radiobutton(f15, text=opt7,font=(15),fg="white",background="black", command=lambda:raise_frame(f16i),value=1,variable=o).pack()
Radiobutton(f15, text=opt8,font=(15),fg="white",background="black", command=lambda:raise_frame(f16ii),value=2,variable=o).pack()

Label(f16i, text=ao,font=(15),fg="white",background="black").pack(pady=45)
Button(f16i, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f17i)).pack()

opt9='''Yes, it's a possibility'''
opt10='''No; killer probably just panicked
and rubbed off all the prints'''

oo=IntVar()

Label(f17i, text=ap,font=(15),fg="white",background="black").pack(pady=45)
Radiobutton(f17i, text=opt9,font=(15),fg="white",background="black", command=lambda:raise_frame(f18i1),value=1,variable=oo).pack()
Radiobutton(f17i, text=opt10,font=(15),fg="white",background="black", command=lambda:raise_frame(f18i2),value=2,variable=oo).pack()

opt11='''Yes, she knows more than she is letting on.'''
opt12='''No; she lives in this house. It wouldn’t be a
surprise if the smell travels to this room.'''

ooo=IntVar()

Label(f18i1, text=aq,font=(15),fg="white",background="black").pack(pady=45)
Radiobutton(f18i1, text=opt11,font=(15),fg="white",background="black", command=lambda:raise_frame(f19i11),value=1,variable=ooo).pack()
Radiobutton(f18i1, text=opt12,font=(15),fg="white",background="black", command=lambda:raise_frame(f19i12),value=2,variable=ooo).pack()

Label(f19i11, text=ar,font=(15),fg="white",background="black").pack(pady=45)
Button(f19i11, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f20)).pack()

Label(f19i12, text=at,font=(15),fg="white",background="black").pack(pady=45)
Button(f19i12, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f20)).pack()

Label(f18i2, text=au,font=(15),fg="white",background="black").pack(pady=45)
Radiobutton(f18i2, text=opt11,font=(15),fg="white",background="black", command=lambda:raise_frame(f19i11),value=1,variable=ooo).pack()
Radiobutton(f18i2, text=opt12,font=(15),fg="white",background="black", command=lambda:raise_frame(f19i12),value=2,variable=ooo).pack()

Label(f16ii, text=av,font=(15),fg="white",background="black").pack(pady=45)
Button(f16ii, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f17ii)).pack()

Label(f17ii, text=aw,font=(15),fg="white",background="black").pack(pady=45)
Radiobutton(f17ii, text=opt9,font=(15),fg="white",background="black", command=lambda:raise_frame(f18i1),value=1,variable=oo).pack()
Radiobutton(f17ii, text=opt10,font=(15),fg="white",background="black", command=lambda:raise_frame(f18i2),value=2,variable=oo).pack()

Label(f20, text=ax,font=(15),fg="white",background="black").pack(pady=45)
Button(f20, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f21)).pack()

Label(f21, text=ay,font=(15),fg="white",background="black").pack(pady=45)
Button(f21, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f22)).pack()

oooo=IntVar()

def total():
    global sn
    global sa
    global se
    if j.get()==2:
        sa+=1
    elif j.get()==1:
        sn++1
    if o.get()==1:
        sn+=1
    if oo.get==1:
        sn+=1
    if oooo.get()==1:
        sa+=1
    elif oooo.get()==2:
        se+=1
    elif oooo.get()==3:
        sn+=1
    if ooo.get()==1:
        se+=1
    if m.get()==1:
        se+=1
    elif m.get()==2:
        sn+=2
        se+=1
        sa+=1
    if k.get()==1:
        sa+=1
    elif k.get()==2:
        se+=1

    raise_frame(fss)

    sus='''Suspicion Levels :
    Aarushi : ''' +str(sa) +'''
    Emil : ''' +str(se) +'''
    Nachiket : ''' +str(sn)

    f=open("Previous_Invetigators.txt","a")
    f.seek(539)
    f.truncate()
    f.write("\n")
    f.close()

    decname()

    f=open("Previous_Invetigators.txt","a")
    f.write(sus)
    f.write("\n")
    f.close()

    f=open("Previous_Invetigators.txt","r")
    det=f.read()
    f.close()

    Label(fss, text=det,font=(10),fg="white",background="black",).pack(pady=5)
    Label(fss, text='Who is most Suspicious?',font=(15),fg="white",background="black").pack()
    Radiobutton(fss, text='Aarushi Chauhan',font=(15),fg="white",background="black", command=lambda:raise_frame(f23),value=1,variable=oooo).pack()
    Radiobutton(fss, text='Emil Ray',font=(15),fg="white",background="black", command=lambda:raise_frame(f23),value=2,variable=oooo).pack()
    Radiobutton(fss, text='Nachiket Mukund',font=(15),fg="white",background="black", command=lambda:raise_frame(f23),value=3,variable=oooo).pack()
    

Label(f22, text=az,font=(15),fg="white",background="black").pack(pady=45)
Button(f22, text='Show Suspicion Level',font=(15),fg="white",background="black", command=total).pack()

o5=IntVar()

Label(f23, text='Whom do you arrest?',font=(15),fg="white",background="black").pack(pady=100,padx=670)
Radiobutton(f23, text='Aarushi Chauhan',font=(15),fg="white",background="black", command=lambda:raise_frame(f24a),value=1,variable=o5).pack()
Radiobutton(f23, text='Emil Ray',font=(15),fg="white",background="black", command=lambda:raise_frame(f24e),value=2,variable=o5).pack()
Radiobutton(f23, text='Nachiket Mukund',font=(15),fg="white",background="black", command=lambda:raise_frame(f24n),value=3,variable=o5).pack()

#----------------------------------------Final Result------------------------------------------
#------------------------------------------Aarushi---------------------------------------------

Label(f24a, text=aab,font=(15),fg="white",background="black").pack(pady=45)
Button(f24a, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f25a)).pack()

Label(f25a, text=aac,font=(15),fg="white",background="black").pack(pady=45)
Button(f25a, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f26a)).pack()

Label(f26a, text=aad,font=(15),fg="white",background="black").pack(pady=45)
Button(f26a, text='End',font=(15),fg="white",background="black", command=root.destroy).pack()

#-------------------------------------------Emil------------------------------------------------

Label(f24e, text=aae,font=(15),fg="white",background="black").pack(pady=45)
Button(f24e, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(f25e)).pack()

Label(f25e, text=aaf,font=(15),fg="white",background="black").pack(pady=45)
Button(f25e, text='Next', font=(15),fg="white",background="black", command=lambda:raise_frame(fletter)).pack()

#-------------------------------------------Common-------------------------------------------------

Label(fletter, text=aai,fg="white",background="black").pack(pady=10)
Button(fletter, text='Next', font=(10),fg="white",background="black", command=lambda:raise_frame(fover)).pack()

Label(fover, text=aaj,font=("Sunday Beach",20),fg="white",background="black").pack(pady=120)
Button(fover, text='End',font=(15),fg="white",background="black", command=root.destroy).pack()

#-----------------------------------------Nachiket----------------------------------------------

Label(f24n, text=aag,font=(15),fg="white",background="black").pack(pady=45)
Button(f24n, text='Next',font=(15),fg="white",background="black", command=lambda:raise_frame(f25n)).pack()

Label(f25n, text=aah,font=(15),fg="white",background="black").pack(pady=45)
Button(f25n, text='Next',font=(15),fg="white",background="black", command=lambda:raise_frame(fletter)).pack()

raise_frame(f)






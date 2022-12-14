from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.configure(bg="black")
root.geometry('2000x2000')
root.state('zoomed')



load = Image.open("typewriter_27.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.place(x=35, y=0)

def story1():
    import Murder

def story2():
    import Alphabets

i=IntVar()

Label(root, text='Odyssey',font=('Tox Typewriter',100),fg="white",background="black").place(x=300,y=150)
Button(root, text='Murder of Alok',font=('Tox Typewriter',35),fg="white",background="black", command=story1).place(x=150,y=500)
Button(root, text='The Alphabets',font=('Tox Typewriter',35),fg="white",background="black", command=story2).place(x=550,y=500)


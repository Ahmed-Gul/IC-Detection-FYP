# Tkinter Session In Python - GUI Development/Desktop Based Applications

# =============================================================================
# from tkinter import *
# =============================================================================
import tkinter as Tk
from PIL import ImageTk,Image
from tkinter import *

root = Tk()
root.configure(background='white')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width,height))
root.title('Tkinter GUI Development')

# Variables
#and gate
global andA
andA = 1
global andB
andB = 1
#or gate
global orA
orA = 1
global orB
orB = 1
#nand gate
global nandA
nandA = 1
global nandB
nandB = 1
#and gate
global norA
norA = 1
global norB
norB = 1


img = ImageTk.PhotoImage(Image.open("and-gate.png"))
lbb = Label(root,image=img,width="180",height="130",bg="powderblue")
lbb.place(x=100,y=20)

# lb1 = Label(root,text="Result")
# lb1.place(x=450,y=40)
lb2 = Label(root,text="0",font=("Arial Bold",10),padx="10",pady="10",bg="powderblue")
lb2.place(x=260,y=58)

def andAtoggle():
    global andA
    if btn1['text'] == "0":
        btn1.config(text="1")
        andA = 0
    else:
        btn1.config(text="0")
        andA = 1
    if andA == 0 and andB == 0:
        lb2.config(text="1")
    else:
        lb2.config(text="0")

def andBtoggle():
    global andB
    if btn2['text'] == "0":
        btn2.config(text="1")
        andB = 0
    else:
        btn2.config(text="0")
        andB = 1
    if andA == 0 and andB == 0:
        lb2.config(text="1")
    else:
        lb2.config(text="0")

btn1 = Button(root, text="0",command=andAtoggle,font=("Arial Bold",10),padx="10",pady="10",bg="powderblue")
btn1.place(x=63,y=25)

btn2 = Button(root, text="0",command=andBtoggle,font=("Arial Bold",10),padx="10",pady="10",bg="powderblue")
btn2.place(x=63,y=90)

root.mainloop()

from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Coolstuffs")
root.geometry("244x346")

def PopUp():
    tkinter.messagebox.showinfo("Aura","You just obtained 100+ aura")


btn=Button(root,text='click Me',bd='5',background='teal',command=PopUp)
btn.pack()

root.mainloop()
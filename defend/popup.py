from tkinter import *
from tkinter import ttk
#root = Tk()
#root.title("asdf")
#frm = ttk.Frame(root, padding=100)#frame padding str with vals for left, top, right, bottom
#frm.grid()
#ttk.Label(frm, text="you're mom").grid(column=0, row=0)
#ttk.Button(frm, text=":(", command=root.destroy).grid(column=0, row=1)
#root.mainloop()

#Create an instance of Tkinter frame
win= Tk()
#Define the geometry of the function
win.geometry("750x250")
def close_win():
   win.destroy()
def disable_event():
   pass
#Create a button to close the window
#btn = ttk.Button(win, text ="Click here to Close",command=close_win)
#btn.pack()
#Disable the Close Window Control Icon
win.protocol("WM_DELETE_WINDOW", disable_event)
win.mainloop()
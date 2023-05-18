#not done yet + doesn't work :(((
from tkinter import *
from tkinter import ttk

win= Tk() #Create instance of Tkinter frame
win.attributes('-fullscreen',True)
frame = ttk.Frame(win, padding=0)
frame.grid()
text0 = ttk.Label(frame, text="New device detected!").grid(row=0, column=0, padx=100, pady=100)
text1 = ttk.Label(frame, text="Do you trust this device?").grid(row=1, column=0, padx=100, pady=100)


def disable_event():
   pass

trust = False

def cursedCode(bool):
  if bool == False:
    bool = True

btn1 = ttk.Button(win, text ="Do Not Trust", command=win.destroy()).grid(row=2, column=0, padx=100, pady=100)#button for untrusted devices (closes the window as well)
btn1.pack()

btn2 = ttk.Button(win, text = "Trust", command = lambda:[cursedCode(trust), win.destroy()]).grid(row=3, column=0, padx=100, pady=100)
btn2.pack()

#Disable the Close Window Control Icon
win.protocol("WM_DELETE_WINDOW", disable_event)
win.mainloop()
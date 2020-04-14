from Tkinter import *
top=Tk()
canvas=Canvas(top,width=200,height=200)
canvas.pack()
oval=canvas.create_oval(10,15,200,150)
top.mainloop()

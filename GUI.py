from tkinter import *
root=Tk()
root.geometry("300x300+100+100")
root.title("void hacks")

frame1=Frame(root)
frame1.pack(fill=X)
Label(frame1,text="year").grid(row=0,column=0,pady=10)
Entry(frame1,width=40).grid(row=0,column=1)
frame2=Frame(root)
frame2.pack(fill=X)

Label(frame2,text="Location").grid(row=0,column=0,pady=10)
Entry(frame2,width=40).grid(row=0,column=1)
frame3=Frame(root)
frame3.pack(fill=X)
Label(frame3,text="Date").grid(row=0,column=0,pady=10)
Entry(frame3,width=40).grid(row=0,column=1)

Button(root,text="Submit").pack()


root.mainloop()
from tkinter import *
from tkinter import messagebox
win=Tk()
win.configure(bg="black")
frame1=Frame(win,bg="cyan")
#decleration of variables
mark1=IntVar()
mark2=IntVar()
mark3=IntVar()
mark4=IntVar()
mark5=IntVar()
total=IntVar()
avg=DoubleVar()
result="Fail"
#sum calculated when submit is clicked
def submit():
    total.set(mark1.get()+mark2.get()+mark3.get()+mark4.get()+mark5.get())
    avg.set(total.get()/5)
    if avg.get()>=35:
        result="Pass"
    else:
        result="Fail"
    messagebox.showinfo("Studenmts Performance","%s\nTotal=%d/500\nAverage=%f"%(result,total.get(),avg.get()))
#print result in message box
label=Label(frame1,text="MARKS DETAILS",font=70,bg="cyan",fg="blue",justify="center").grid(row=4)
label0=Label(frame1,text="Enter name                  :",bg="cyan",font=50,fg="red").grid(row=5)
#inserting values
entry0=Entry(frame1)
#creating labels
label1=Label(frame1,text="Enter subject 1 marks :",bg="cyan",font=60,fg="black").grid(row=6)
entry1=Entry(frame1,textvariable=mark1)
label2=Label(frame1,text="Enter subject 2 marks :",bg="cyan",font=60,fg="black").grid(row=7)
entry2=Entry(frame1,textvariable=mark2)
label3=Label(frame1,text="Enter subject 3 marks :",bg="cyan",font=60,fg="black").grid(row=8)
entry3=Entry(frame1,textvariable=mark3)
label4=Label(frame1,text="Enter subject 4 marks :",bg="cyan",font=60,fg="black").grid(row=9)
entry4=Entry(frame1,textvariable=mark4)
label5=Label(frame1,text="Enter subject 5 marks :",bg="cyan",font=60,fg="black").grid(row=10)
entry5=Entry(frame1,textvariable=mark5)
P=Button(frame1,text="SUBMIT",fg="white",bg="blue",command=submit)
entry0.grid(row=5, column=5)
entry1.grid(row=6, column=5)
entry2.grid(row=7, column=5)
entry3.grid(row=8, column=5)
entry4.grid(row=9, column=5)
entry5.grid(row=10, column=5)
P.grid(row=11, column=5)
#starts the program
frame1.place(relx=0.5, rely=0.5, anchor=CENTER)
win.mainloop()

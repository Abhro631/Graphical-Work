from tkinter import *
from tkinter import messagebox
root = Tk()

def genderButton():
    pass
    # if(male.get()==1):
    #     female.set(0)
    # if(female.get()==1):
    #     male.set(0)

label1=Label(root,text='Regno')
label2=Label(root,text='Name')
label3=Label(root,text='Dept')
label4=Label(root,text='Gender')
label5=Label(root,text='Age')

entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)
entry4=Spinbox(root,from_=0,to=100)


male=Radiobutton(root,text='Male',value=1)
female=Radiobutton(root,text='Femle',value=0)

button1=Button(root,text='Insert')
button2=Button(root,text='Update')
button3=Button(root,text='Delete')
button4=Button(root,text='Select')

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
label4.grid(row=3,column=0)
label5.grid(row=4,column=0)

male.grid(row=3,column=1)
female.grid(row=3,column=2)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)
entry4.grid(row=4,column=1)

button1.grid(row=5,column=0)
button2.grid(row=5,column=1)
button3.grid(row=6,column=0)
button4.grid(row=6,column=1)

root.mainloop()

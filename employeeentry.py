from tkinter import *

root = Tk()

label1=Label(root,text='Custid')
label2=Label(root,text='Customer name: ')
label3=Label(root,text='Branch')
label4=Label(root,text='account type')
label5=Label(root,text='Amount')

button1=Button(root,text='Insert')
button2=Button(root,text='Update')
button3=Button(root,text='Delete')
button4=Button(root,text='Select')

entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)

saving=Radiobutton(root,value=0,text='Saving')
non_saving=Radiobutton(root,value=1,text='Non Saving')

scale1=Scale(root,from_=0,to=100,orient=HORIZONTAL)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
label4.grid(row=3,column=0)
label5.grid(row=4,column=0)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)

saving.grid(row=3,column=1)
non_saving.grid(row=3,column=2)

scale1.grid(row=4,column=1)

button1.grid(row=5,column=0)
button2.grid(row=5,column=1)
button3.grid(row=6,column=0)
button4.grid(row=6,column=1)

root.mainloop()

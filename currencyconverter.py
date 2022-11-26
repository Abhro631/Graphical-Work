from datetime import datetime
from tkinter import *

root=Tk()


def convert():
    if variable.get()=='USD' and variable1.get()=='INR':
        txtvat2.set(str(float(leftentry.get())*74.93))
    elif variable.get()=='INR' and variable1.get()=='USD':
        txtvat2.set(str(float(leftentry.get())/74.93))
    elif variable.get()=='INR' and variable1.get()=='INR':
        txtvat2.set(str(float(leftentry.get())))
    elif variable.get()=='USD' and variable1.get()=='USD':
        txtvat2.set(str(float(leftentry.get())))

#str(float(leftentry.get()))
#float(leftentry.get())
#   {:.2f}.format(float(leftentry.get()))
label1=Label(text='Welcome to Real time currency converter',bg='blue',fg='White')
label2=Label(text='1 USD = 74.93 Indian Rupee')
label3=Label(text='Date ' +str(datetime.now()))

variable=StringVar(root)
variable.set('USD')

variable1=StringVar(root)
variable1.set('INR')

leftside=OptionMenu(root,variable,'USD','INR')
rigtside=OptionMenu(root,variable1,'INR','USD')

txtvat1=StringVar()
txtvat2=StringVar()

leftentry=Entry(root,textvariable=txtvat1)
rightentry=Entry(root,textvariable=txtvat2)

convertButton=Button(root,command=convert,fg='white',bg='#000080',text='Convert')

label1.grid(row=0,columnspan=3)
label2.grid(row=1,columnspan=3)
label3.grid(row=2,columnspan=3)

leftside.grid(row=3,column=0)
rigtside.grid(row=3,column=2)

leftentry.grid(row=4,column=0)
rightentry.grid(row=4,column=2)

convertButton.grid(row=5,column=1)
# label1.pack()
# label2.pack()
# label3.pack()
root.mainloop()

from tkinter import*
window=Tk()
window.title('My window')
window.geometry('450x500')
m=Label(window,text="Calculator",font=("Arial",25))
m.place(x=135,y=40)
m1=Label(window,text="type value1:",font=("Arial",15))
m1.place(x=90,y=100)
m1=Label(window,text="type value2:",font=("Arial",15))
m1.place(x=90,y=150)
m2=Label(window,text="result:",font=("Arial",15))
m2.place(x=130,y=290)
def Add():
    sum=num1.get()+num2.get()
    entry3.delete(0,END)
    entry3.insert(0,str(sum))
def Sub():
    minus=num1.get()-num2.get()
    entry3.delete(0,END)
    entry3.insert(0,str(minus))  
def Mult():
    pro=num1.get()*num2.get()
    entry3.delete(0,END)
    entry3.insert(0,str(pro))
def Div():
    quo=num1.get()/num2.get()
    entry3.delete(0,END)
    entry3.insert(0,str(quo))
num1=IntVar()
num2=IntVar()
num3=IntVar()
entry1=Entry(window,textvariable=num1)
entry1.place(x=200,y=100,height=30,width=100)
entry2=Entry(window,textvariable=num2)
entry2.place(x=200,y=150,height=30,width=100)
entry3=Entry(window,textvariable=num3)
entry3.place(x=200,y=290,height=30,width=100)
b=Button(window,text='+',font=("Arial",15),bg='green',fg='white',command=Add)
b.place(x=100,y=200,height=30,width=40)
b1=Button(window,text='-',font=("Arial",15),bg='green',fg='white',command=Sub)
b1.place(x=150,y=200,height=30,width=40)
b2=Button(window,text='*',font=("Arial",15),bg='green',fg='white',command=Mult)
b2.place(x=200,y=200,height=30,width=40)
b3=Button(window,text='/',font=("Arial",15),bg='green',fg='white',command=Div)
b3.place(x=250,y=200,height=30,width=40)
window.mainloop()

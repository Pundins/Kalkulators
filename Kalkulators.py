from ast import operator
from argparse import MetavarTypeHelpFormatter
from tkinter import*
from math import*
mansLogs=Tk()
mansLogs.title("Kalkulators")
mansLogs.configure(bg="#A9A9A9") 
#mansLogs.geometry("300x450")

def vienads():
    global num2
    num2=(float(e.get()))
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="x":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    elif mathOp=="%":
        result=num1*0.01*num2
    else:
        result=0
    e.delete(0, END)
    e.insert(0, str(result))
    return 0

def notirit():
    e.delete(0, END)
    num1=0
    mathOp=""
    return 0 

def sakne():
    global operator
    global num1
    global mathOp
    num1=(float(e.get()))
    num1=sqrt(num1)
    e.delete(0, END)
    e.insert(0, num1)
    return 0

def kvadrats():
    global operator 
    global num1
    global mathOp
    num1=(float(e.get()))
    num1=num1*num1
    e.delete(0, END)
    e.insert(0, num1)
    return 0

def logaritms():
    global operator
    global num1
    global mathOp
    num1=(float(e.get()))
    num1=log(num1, 10)
    e.delete(0, END)
    e.insert(0, num1)
    return 0

btn0 = Button(mansLogs, text="0", padx="40", bd=5, bg="#C6DDAF", pady="30", command=lambda:btnClick(0))
btn1 = Button(mansLogs, text="1", padx="40", bd=5, bg="#C6DDAF", pady="30", command=lambda:btnClick(1))
btn2 = Button(mansLogs, text="2", padx="40", bd=5, bg="#C6DDAF", pady="30", command=lambda:btnClick(2))
btn3 = Button(mansLogs, text="3", padx="40", bd=5, bg="#C6DDAF", pady="30", command=lambda:btnClick(3))
btn4 = Button(mansLogs, text="4", padx="40", bd=5, bg="#C6DDAF", pady="30", command=lambda:btnClick(4))
btn5 = Button(mansLogs, text="5", padx="40", bd=5, bg="#C6DDAF", pady="30", command=lambda:btnClick(5))
btn6 = Button(mansLogs, text="6", padx="40", bd=5, bg="#C6DDAF", pady="30", command=lambda:btnClick(6))
btn7 = Button(mansLogs, text="7", padx="40", bd=5, bg="#C6DDAF", pady="30", command=lambda:btnClick(7))
btn8 = Button(mansLogs, text="8", padx="40", bd=5, bg="#C6DDAF", pady="30", command=lambda:btnClick(8))
btn9 = Button(mansLogs, text="9", padx="40", bd=5, bg="#C6DDAF", pady="30", command=lambda:btnClick(9))
btn10 = Button(mansLogs, text="-", padx="40", bd=5, bg="#ACE7FF", pady="30", command=lambda:btnCommand("-"))
btn11 = Button(mansLogs, text="+", padx="40", bd=5, bg="#ACE7FF", pady="30", command=lambda:btnCommand("+"))
btn12 = Button(mansLogs, text="/", padx="40", bd=5, bg="#ACE7FF", pady="30", command=lambda:btnCommand("/"))
btn13 = Button(mansLogs, text="x", padx="40", bd=5, bg="#ACE7FF", pady="30", command=lambda:btnCommand("x"))
btn14 = Button(mansLogs, text="=", padx="40", bd=5, bg="#FFABAB", pady="30", command=vienads)
btn15 = Button(mansLogs, text="C", padx="40", bd=5, bg="#FFABAB", pady="30", command=notirit)
btn16 = Button(mansLogs, text="%", padx="40", bd=5, bg="#ACE7FF", pady="30", command=lambda:btnCommand("%"))
btn17 = Button(mansLogs, text="x??", padx="38", bd=5, bg="#ACE7FF", pady="30", command=kvadrats)
btn18 = Button(mansLogs, text="???", padx="40", bd=5, bg="#ACE7FF", pady="30", command=sakne)
btn19 = Button(mansLogs, text="Log", padx="35", bd=5, bg="#ACE7FF", pady="30", command=logaritms)

btn0.grid(row=4,column=2)
btn1.grid(row=3,column=1)
btn2.grid(row=3,column=2)
btn3.grid(row=3,column=3)
btn4.grid(row=2,column=1)
btn5.grid(row=2,column=2)
btn6.grid(row=2,column=3)
btn7.grid(row=1,column=1)
btn8.grid(row=1,column=2)
btn9.grid(row=1,column=3)
btn10.grid(row=2, column=4)
btn11.grid(row=1, column=4)
btn12.grid(row=3, column=4)
btn13.grid(row=4, column=4)
btn14.grid(row=4, column=3)
btn15.grid(row=4, column=1)
btn16.grid(row=5, column=4)
btn17.grid(row=5, column=2)
btn18.grid(row=5, column=3)
btn19.grid(row=5, column=1)

def btnClick(number):
    current=e.get() # nolasa eso??o skaitli
    e.delete(0, END) # nodz????
    newNumber=str(current)+str(number)
    e.insert(0, newNumber) # ievieto displej??
    return 0

def btnCommand(command):
    global num1 # j??iegaum?? skaitlis un darb??ba
    global mathOp # matem??tisks operators
    mathOp = command # +,-,*,/
    num1 = float(e.get())
    e.delete(0, END)
    return 0


e=Entry(mansLogs, width=15, bd=10, bg="#A9A9A9", font=("Arial Black", 20))
e.grid(row=0, column=0, columnspan=5)

#poga.pack()

mansLogs.mainloop()
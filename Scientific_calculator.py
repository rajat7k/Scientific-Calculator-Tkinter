from tkinter import *
import tkinter.messagebox as tmsg
import os
import time
from math import *


root = Tk()
root.title("Scientific Calculator")
root.wm_iconbitmap("Calculator.ico")

root.configure(background="black")


root.resizable(width=False, height=False)
root.geometry("934x615+350+120")


def getvals(event):
    value = event.widget.cget('text')
    if value == 'Clr':
        sc_variable.set('')
    elif value == '=':
        try:
            sc_variable.set(eval(screen.get()))
            screen.update()
        except Exception as e:
            sc_variable.set('Error - Wait for 3 sec')
            screen.update()
            status_var.set('Preparing...')
            screen.update()
            time.sleep(3)
            sc_variable.set('')
            screen.update()
            status_var.set('Ready..')
            screen.update()

    else:
        sc_variable.set(f'{sc_variable.get()}{value}')


def radian():
    a = screen.get()
    b = float(a)
    rad_val = radians(b)
    sc_variable.set(rad_val)
    screen.update()


def degree():

    a = screen.get()
    b = float(a)
    deg_val = degrees(b)
    sc_variable.set(deg_val)
    screen.update()


def how_to_use():
    tmsg.showinfo(' How to use ', 'NOTE: use base x=e,10,2,etc with log to get answer in your desired log base. *Sin cos etc answers are in radian by default')


def developers():
    tmsg.showinfo('Developers', 'Developed by Rajat kaushik and Saket Thenua.')


my_menu = Menu(root)
m1 = Menu(my_menu, tearoff=0, fg='black')
m1.add_command(label='How to use', command=how_to_use)
m1.add_command(label='Developers', command=developers)
root.config(menu=my_menu)
my_menu.add_cascade(label=' About ', menu=m1)


sc_variable = StringVar()
f = Frame(root)
f.pack()
screen = Entry(f, textvariable=sc_variable,
               relief=RAISED, font=(
                   'Helvetica', 20, 'bold'), bg="black", fg="white", bd=30, width=58, justify=RIGHT)
screen.grid(row=0, column=0, columnspan=4, pady=1)


f = Frame(root)
f.pack()
numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(f, width=6, height=2, font=(
            'arial', 20, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i].bind('<Button-1>', getvals)
        i += 1


btnClear = Button(f, text='Clr', width=6, height=2, font=('arial', 20, 'bold'),
                  bd=4, bg="yellow")
btnClear.bind('<Button-1>', getvals)
btnClear.grid(row=1, column=0, pady=1)


leftparan = Button(f, text='(', width=6, height=2, font=('arial', 20, 'bold'),
                   bd=4, bg="Aqua")
leftparan.bind('<Button-1 >', getvals)
leftparan.grid(row=1, column=1, pady=1)


rightparan = Button(f, text=")", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                    bg="Aqua")
rightparan.bind('<Button-1>', getvals)
rightparan.grid(row=1, column=2, pady=1)

btnAdd = Button(f, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="Aqua")
btnAdd.bind('<Button-1>', getvals)
btnAdd.grid(row=1, column=3, pady=1)


btnSub = Button(f, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="Aqua")
btnSub.bind('<Button-1>', getvals)
btnSub.grid(row=2, column=3, pady=1)

btnMult = Button(f, text="*", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="Aqua")
btnMult.bind('<Button-1>', getvals)
btnMult.grid(row=3, column=3, pady=1)


btnDiv = Button(f, text='/', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="Aqua")
btnDiv.bind('<Button-1>', getvals)
btnDiv.grid(row=4, column=3, pady=1)

btnZero = Button(f, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="white")
btnZero.bind('<Button-1>', getvals)
btnZero.grid(row=5, column=0, pady=1)


btnDot = Button(f, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="Aqua")
btnDot.bind('<Button-1>', getvals)
btnDot.grid(row=5, column=1, pady=1)

btncomma = Button(f, text=',', width=6, height=2, font=('arial', 20, 'bold'),
                  bd=4, bg="Aqua")
btncomma.bind('<Button-1>', getvals)
btncomma.grid(row=5, column=2, pady=1)

btnEquals = Button(f, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                   bg="blue")
btnEquals.bind('<Button-1>', getvals)
btnEquals.grid(row=5, column=3, pady=1)

btnpower = Button(f, text='**', width=6, height=2, font=('arial', 20, 'bold'),
                  bd=4, bg="gray")
btnpower.bind('<Button-1>', getvals)
btnpower.grid(row=1, column=4, pady=1)

btnwholediv = Button(f, text="//", width=6, height=2, font=('arial', 20, 'bold'),
                     bd=4, bg="gray")
btnwholediv.bind('<Button-1>', getvals)
btnwholediv.grid(row=1, column=5, pady=1)


btnsqrt = Button(f, text="sqrt", width=6, height=2, font=('arial', 20, 'bold'),
                 bd=4, bg="gray")
btnsqrt.bind('<Button-1>', getvals)
btnsqrt.grid(row=1, column=6, pady=1)

btnlog = Button(f, text='log', width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="gray")
btnlog.bind('<Button-1>', getvals)
btnlog.grid(row=1, column=7, pady=1)

btnsin = Button(f, text='sin', width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="gray")
btnsin.bind('<Button-1>', getvals)
btnsin.grid(row=2, column=4, pady=1)

btnCos = Button(f, text="cos", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="gray")
btnCos.bind('<Button-1>', getvals)
btnCos.grid(row=2, column=5, pady=1)

btnTanh = Button(f, text="tan", width=6, height=2, font=('arial', 20, 'bold'),
                 bd=4, bg="gray")
btnTanh.bind('<Button-1>', getvals)
btnTanh.grid(row=2, column=6, pady=1)

btnSinh = Button(f, text="pow", width=6, height=2, font=('arial', 20, 'bold'),
                 bd=4, bg="gray")
btnSinh.bind('<Button-1>', getvals)
btnSinh.grid(row=2, column=7, pady=1)

btnLog = Button(f, text='asinh', width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="gray")
btnLog.bind('<Button-1>', getvals)
btnLog.grid(row=3, column=4, pady=1)

btninv = Button(f, text="acosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="gray")
btninv.bind('<Button-1>', getvals)
btninv.grid(row=3, column=5, pady=1)

btnMod = Button(f, text="atanh", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="gray")
btnMod.bind('<Button-1>', getvals)
btnMod.grid(row=3, column=6, pady=1)

btnE = Button(f, text="exp", width=6, height=2, font=('arial', 20, 'bold'),
              bd=4, bg="gray")
btnE.bind('<Button-1>', getvals)
btnE.grid(row=3, column=7, pady=1)

btnexp = Button(f, text='abs', width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="gray")
btnexp.bind('<Button-1>', getvals)
btnexp.grid(row=4, column=4, pady=1)

btnDeg = Button(f, text="ceil", width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="gray")
btnDeg.bind('<Button-1>', getvals)
btnDeg.grid(row=4, column=5, pady=1)

btnAcosh = Button(f, text="floor", width=6, height=2, font=('arial', 20, 'bold'),
                  bd=4, bg="gray")
btnAcosh.bind('<Button-1>', getvals)
btnAcosh.grid(row=4, column=6, pady=1)

btnAsinh = Button(f, text="Inv", width=6, height=2, font=('arial', 20, 'bold'),
                  bd=4, bg="gray")
btnAsinh.bind('<Button-1>', getvals)
btnAsinh.grid(row=4, column=7, pady=1)

btnpow = Button(f, text='%', width=6, height=2, font=('arial', 20, 'bold'),
                bd=4, bg="gray")
btnpow.bind('<Button-1>', getvals)
btnpow.grid(row=5, column=4, pady=1)

btnLog1p = Button(f, text="Deg", width=6, height=2, font=('arial', 20, 'bold'),
                  bd=4, bg="gray", command=degree)

btnLog1p.grid(row=5, column=5, pady=1)

btnExpm1 = Button(f, text="Rad", width=6, height=2, font=('arial', 20, 'bold'),
                  bd=4, bg="gray", command=radian)

btnExpm1.grid(row=5, column=6, pady=1)


def Exitcal():
    iExit = tmsg.askyesno(
        "Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return


exitbutton = Button(f, text="Exit", width=6, height=2, font=(
    'arial', 20, 'bold'), bd=4, bg="red", command=Exitcal).grid(row=5, column=7, pady=1)


status_var = StringVar()
status_var.set('Ready..')
Label(root, textvariable=status_var, relief=SUNKEN, anchor='w',
      borderwidth=3, bg='yellow', fg='red').pack(side=BOTTOM, fill=X)


root.mainloop()

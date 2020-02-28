from tkinter import *
import math

def clickCalculate(event):
    result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(result)
    if (result >= 30):
        labelResult.configure(text="อ้วนมาก",font=("serithai",10),fg="red",bg="white")
    elif (result >= 25 and result <= 29.9):
        labelResult.configure(text="อ้วน",font=("serithai",10),fg="red",bg="white")
    elif (result >= 23 and result <= 24.9 ):
        labelResult.configure(text="น้ำหนักเกิน",font=("serithai",10),fg="red",bg="white")
    elif (result >= 18.6 and result <= 22.9 ):
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม",font=("serithai",10),fg="green",bg="white")
    elif (result <= 18.5):
        labelResult.configure(text="ผอมเกินไป",font=("serithai",10),fg="red",bg="white")

MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง(cm)",font=("serithai",10))
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(MainWindow,text="น้ำหนัก(kg)",font=("serithai",10))
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text="คำนวณ",font=("serithai",10))
calculateButton.grid(row=2,column=0)
calculateButton.bind('<Button-1>',clickCalculate)
labelResult = Label(MainWindow,text="Result")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()
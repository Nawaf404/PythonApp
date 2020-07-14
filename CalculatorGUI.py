from tkinter import *
app = Tk()
app.title("Calculator")
app.minsize(300,300) # لو تصغر التطبيق راح يصغر لين هذا الحجم
app.maxsize(500,500)# الحد الاقصى من النافذه
Fonts = "Helvetica 14 bold "
# def
def addNumber():
    number1 = float(number1Box.get())
    number2 = float(number2Box.get())
    result = number1 + number2
    resultlabel = Label(text="result is: " + str(result),font=Fonts,pady=15)
    date = Label(text=f"Date Today : {datetime.datetime.today().date()}",fg="red",pady=5,font=Fonts)
    time = Label(text=f"Time now : {datetime.datetime.today().hour}:{datetime.datetime.today().minute}",fg="blue",font=Fonts,pady=5)
    resultlabel.pack()
    date.pack()
    time.pack()

number1Label = Label(app,text="First Number",font=Fonts,pady=15)
number1Label.pack() # حجز مكان Book Place

number1Box = Entry(font=Fonts) # Input
number1Box.pack()

number2Label = Label(text="Second Number",font=Fonts,pady=15).pack()
number2Box = Entry(font=Fonts)
number2Box.pack()

Button = Button(text="Add",padx=15,font=Fonts,pady=5,command=addNumber)
Button.pack()
app.mainloop()

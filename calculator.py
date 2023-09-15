from tkinter import *

window = Tk()
window.title("My Window")
# window.geometry("720x720")
expression = ""

def handleClick(button):
   
    global expression
    if len(expression) == 0:     
        if button.isdigit():
            if button!="0":
                expression = expression + button
                data.set(expression)
        
    else:
        expression = expression + button
        data.set(expression)



        

def handleEqual ():
    global expression
    a=expression[-1]
    if a.isdigit():

        res = eval(expression)
        data.set(res)
        expression=""
    


# string[start: end: stepsize]

def handleBackspace():
    global expression
    expression = expression[:-1]
    data.set(expression)
###################
data = StringVar()

input_box = Entry(window,font=28, textvariable=data)
input_box.grid(row=0, column=0, columnspan=4, pady=10)

button_one = Button(window,text="0", font=24, padx=10, pady=10, command=lambda: handleClick("0"))
button_one.grid(row=4, column=1, padx=10, pady=10)
button_one = Button(window,text="=", font=24, padx=10, pady=10, command=handleEqual)
button_one.grid(row=4, column=2, padx=10, pady=10)
button_one = Button(window,text="/", font=24, padx=10, pady=10, command=lambda: handleClick("/"))
button_one.grid(row=4, column=3, padx=10, pady=10)
button_one = Button(window,text="<=", font=24, padx=10, pady=10, command=handleBackspace)
button_one.grid(row=4, column=0, padx=10, pady=10)

button_one = Button(window,text="1", font=24, padx=10, pady=10, command=lambda: handleClick("1"))
button_one.grid(row=3, column=0,padx=10, pady=10)
button_one = Button(window,text="2", font=24, padx=10, pady=10, command=lambda: handleClick("2"))
button_one.grid(row=3, column=1, padx=10, pady=10)
button_one = Button(window,text="3", font=24, padx=10, pady=10, command=lambda: handleClick("3"))
button_one.grid(row=3, column=2, padx=10, pady=10)
button_one= Button(window, text="+", font=24, padx=10, pady=10, command=lambda: handleClick("+"))
button_one.grid(row=3, column=3,padx=10, pady=10)

button_one = Button(window,text="4", font=24, padx=10, pady=10, command=lambda: handleClick("4"))
button_one.grid(row=2, column=0, padx=10, pady=10)
button_one = Button(window,text="5", font=24, padx=10, pady=10, command=lambda: handleClick("5"))
button_one.grid(row=2, column=1, padx=10, pady=10)
button_one = Button(window,text="6", font=24, padx=10, pady=10, command=lambda: handleClick("6"))
button_one.grid(row=2, column=2 , padx=10, pady=10)
button_one= Button(window, text="-", font=24, padx=10, pady=10, command=lambda: handleClick("-"))
button_one.grid(row=2, column=3,padx=10, pady=10)

button_one = Button(window,text="7", font=24, padx=10, pady=10, command=lambda: handleClick("7"))
button_one.grid(row=1, column=0, padx=10, pady=10)
button_one = Button(window,text="8", font=24, padx=10, pady=10, command=lambda: handleClick("8"))
button_one.grid(row=1, column=1, padx=10, pady=10)
button_one = Button(window,text="9", font=24, padx=10, pady=10, command=lambda: handleClick("9"))
button_one.grid(row=1, column=2, padx=10, pady=10)
button_one= Button(window, text="*", font=24, padx=10, pady=10, command=lambda: handleClick("*"))
button_one.grid(row=1, column=3,padx=10, pady=10)
###################


window.mainloop()
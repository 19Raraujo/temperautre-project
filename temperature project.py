# sticky means which sides of the window it should stick on 
from tkinter import *
window = Tk()
window.title("new project")
window.geometry("600x800")

#temperature - continuous data
#seperates the window into 3 different sections
window.columnconfigure(0,weight = 1)
window.columnconfigure(1,weight = 1)
window.columnconfigure(2,weight = 1)

window.rowconfigure(0,weight = 1)
window.rowconfigure(1,weight = 1)
window.rowconfigure(2,weight = 1)


current_unit = NONE

def submit_celcius():
    global current_unit
    try:
        temp = float(input1.get())
        label_1.configure(text="The weather is: " + str(round(temp, 2)) + "°C")
        current_unit = "C"
    except:
        label_1.configure(text="Invalid, try again")


def submit_fahrenheit():
    global current_unit
    try:
        temp = float(input1.get())
        label_1.configure(text= "the weather is : " + str(temp) + "°F")
        current_unit = "F"
    except:
        label_1.configure(text = "invalid, try again")
        

def fahrenheit_convert():
    global current_unit
    try:
        temp = float(input1.get())
        if current_unit == "F":
            label_1.configure(text="It's already in Fahrenheit: " + str(temp) + "°F")
        else:
            fahrenheit = (temp * 1.8) + 32
            fahrenheit = round(fahrenheit, 2)
            label_1.configure(text=f"The weather is {fahrenheit}°F")
            input1.delete(0, END) # deletes all of the characters in label 1
            input1.insert(0, str(fahrenheit))  # changes the label 1 temperature back to the original conversion 
            current_unit = "F"
    except ValueError:
        label_1.configure(text="Invalid number, try again")


def celcius_convert():
    global current_unit
    try:
        temp = float(input1.get())
        if current_unit == "C":
            label_1.configure(text="It's already in Celsius: " + str(temp) + "°C")
        else:
            celcius = (temp - 32) / 1.8
            celcius = round(celcius, 2)
            label_1.configure(text=f"The weather is {celcius}°C")
            input1.delete(0, END) 
            input1.insert(0, str(celcius))  #
            current_unit = "C"
    except ValueError:
        label_1.configure(text="Invalid number, try again")

#entry area

label_2 = Label(font = ("Arial",20),
                text = "input temperature and click either fahrenheit or celcius: ",
                fg= "yellow",
                bg = "black")
label_2.grid(row = 0, column = 0 , sticky = "ne")

input1 = Entry(window,
              font = ("Arial",30),
              fg = "white",
              bg = "grey")
input1.grid(row = 0, column = 1, sticky= "nw")

#initial temperature choice 1 
initial_celcius = Button(window, text = "celcius", 
                    command = submit_celcius,
                    font=("Comic Sans",30))

initial_celcius.grid(row = 0, column = 1, sticky= "e")


#initial temperature choice 2
temperature = Button(window, text = "fahrenheit", 
                    command = submit_fahrenheit,
                    font=("Comic Sans",30))

temperature.grid(row = 0, column = 1, sticky= "w")


#first label
label_1 = Label(font = ("Arial",20),
                text = "no weather temperature inputted",
                fg= "yellow",
                bg = "black")
label_1.grid(row = 1,column =1, sticky="nsew")

#farenheit converter
fahrenheit = Button(window,text= "change to fahrenheit", command = fahrenheit_convert,
                    font = ("Comic Sans",20),
                    bg = "grey")

fahrenheit.grid(row = 1, column = 2, sticky = "nsew")

celcius = Button(window,text= "change to celcius", command = celcius_convert,
                    font = ("Comic Sans",20),
                    bg = "grey")

celcius.grid(row = 1, column = 0, sticky = "nsew")



window.mainloop()


#things to do in future
    # -273 degrees is 0 fahrenheit, not -400

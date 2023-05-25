from ast import Expression, Lambda
from tkinter import *

from numpy import equal, multiply
window = Tk()

window.geometry("312x324") #size of the width:- 500, height:- 375

#change the tittle
window.title("Calculator")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
    
    
def btn_clear():
    global expression
    expression = ""
    input_text.set("")
    
    
def btn_equal():
    global expression
    result = str(eval(expression))# eval function evalute the string expression directly, or we can write our own evalute function.
    input_text.set(result)
    expression = ""
    
expression = ""
input_text = StringVar()
    
    
#creating frame for the inout field
input_frame = Frame(window, width= 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black")    
input_frame.pack(side = TOP)

#creating input field inside the frame
input_field = Entry(input_frame, font =('arial',16, 'bold'), textvariable= input_text, width = 50, bg="#eee", bd=0, justify='center')

input_field.grid(row=0, column = 0)
input_field.pack(ipady=10) # ipady is internal padding to increase the height of input field

#creating another Frame for the button below input frame
btn_frame = Frame(window, width= 312, height = 275.5, bg = 'grey')
btn_frame.pack()

#first row
clear = Button(btn_frame, text ="C", fg = "black", width = 32,height =3, bd=0, bg="#eee", cursor = "hand2", command = lambda:btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

divide = Button(btn_frame,text ="/", fg = "black", width = 10,height =3, bd=0, bg="#eee", cursor = "hand2", command =lambda:btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

#second row
seven =  Button(btn_frame,text ="7", fg = "black", width = 10,height =3, bd=0, bg="#fff", cursor = "hand2", command =lambda:btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)

eight =  Button(btn_frame,text ="8", fg = "black", width = 10,height =3, bd=0, bg="#fff", cursor = "hand2", command =lambda:btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1) 

nine =  Button(btn_frame,text ="9", fg = "black", width = 10,height =3, bd=0, bg="#fff", cursor = "hand2", command =lambda:btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

multiply =  Button(btn_frame,text ="*", fg = "black", width = 10,height =3, bd=0, bg="#eee", cursor = "hand2", command = lambda:btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)


#third row
four =  Button(btn_frame,text ="4", fg = "black", width = 10,height =3, bd=0, bg="#fff", cursor = "hand2", command =lambda:btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)

five =  Button(btn_frame,text ="5", fg = "black", width = 10,height =3, bd=0, bg="#fff", cursor = "hand2", command =lambda:btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)

six =  Button(btn_frame,text ="6", fg = "black", width = 10,height =3, bd=0, bg="#fff", cursor = "hand2", command = lambda:btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

minus =  Button(btn_frame,text ="-", fg = "black", width = 10,height =3, bd=0, bg="#eee", cursor = "hand2", command =lambda:btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

#fourth row
one =  Button(btn_frame,text ="1", fg = "black", width = 10,height =3, bd=0, bg="#fff", cursor = "hand2", command =lambda:btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)

two =  Button(btn_frame,text ="2", fg = "black", width = 10,height =3, bd=0, bg="#fff", cursor = "hand2", command =lambda:btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)

three =  Button(btn_frame,text ="3", fg = "black", width = 10,height =3, bd=0, bg="#fff", cursor = "hand2", command =lambda:btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

plus =  Button(btn_frame,text ="+", fg = "black", width = 10,height =3, bd=0, bg="#eee", cursor = "hand2", command =lambda:btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)


#fifth row
zero =  Button(btn_frame,text ="0", fg = "black", width = 21,height =3, bd=0, bg="#fff", cursor = "hand2", command =lambda:btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

point =  Button(btn_frame,text =".", fg = "black", width = 10,height =3, bd=0, bg="#fff", cursor = "hand2", command =lambda:btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)

equal =  Button(btn_frame,text ="=", fg = "black", width = 10,height =3, bd=0, bg="#fff", cursor = "hand2", command =lambda:btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)


window.mainloop()
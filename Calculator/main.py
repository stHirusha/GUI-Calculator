from customtkinter import *

root = CTk()
root.title("Calculator")
root.geometry("570x630+50+50")
root.resizable(False,False)

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

info = ""

def clear():
    global info
    info = ""
    display.configure(text = info)

def show(value):
    global info
    info += value
    display.configure(text = info)

def calculate():
    global info
    if eval != "":
        try:
            results = eval(info)
            display.configure(text = results)
        except:
           display.configure(text = "Unexpected Input", text_color = "red")
           info = ""

frame1 = CTkFrame(root, border_color="white", border_width=2)
frame1.columnconfigure(0,weight = 1)
frame1.columnconfigure(1,weight = 1)

frame1.place(x= 20,y= 10,width = 530,height = 130)

display = CTkLabel(frame1, text="", font=("Arial", 40), bg_color="grey")
display.pack()
display.width = 25
display.height = 10

display.pack(fill="both", expand = True)

frame = CTkFrame(root, border_color = "white", border_width=2)
frame.columnconfigure(0,weight = 1)
frame.columnconfigure(1,weight = 1)
frame.columnconfigure(2,weight = 1)
frame.columnconfigure(3,weight = 1)
frame.columnconfigure(4,weight = 1)

frame.place(x = 20, y = 150, width = 530, height = 460)

CTkButton(frame, text= "C", font=("arial", 60, "bold"),command = lambda : clear(), border_width = 2, width = 120,height = 30, fg_color = "white",text_color = "black",hover_color = "grey").place(x = 10, y = 10)
CTkButton(frame, text= "/", font=("arial", 60, "bold"),command = lambda : show("/"),  border_width = 2, width = 120,height = 30, fg_color = "white",text_color = "black",hover_color = "grey").place(x = 140, y = 10)
CTkButton(frame, text= "%", font=("arial", 60, "bold"),command = lambda : show("%"), border_width = 2, width = 120,height = 30, fg_color = "white",text_color = "black",hover_color = "grey").place(x = 270, y = 10)
CTkButton(frame, text= "*", font=("arial", 60, "bold"),command = lambda : show("*"), border_width = 2, width = 120,height = 30, fg_color = "white",text_color = "black",hover_color = "grey").place(x = 400, y = 10)
CTkButton(frame, text= "7", font=("arial", 60, "bold"),command = lambda : show("7"), border_width = 2, width = 120,height = 30).place(x = 10, y = 100)
CTkButton(frame, text= "8", font=("arial", 60, "bold"),command = lambda : show("8"),border_width = 2, width = 120,height = 30).place(x = 140, y = 100)
CTkButton(frame, text= "9", font=("arial", 60, "bold"),command = lambda : show("9"), border_width = 2, width = 120,height = 30).place(x = 270, y = 100)
CTkButton(frame, text= "-", font=("arial", 60, "bold"),command = lambda : show("-"), border_width = 2, width = 120,height = 30, fg_color = "white",text_color = "black",hover_color = "grey").place(x = 400, y = 100)
CTkButton(frame, text= "4", font=("arial", 60, "bold"),command = lambda : show("4"), border_width = 2, width = 120,height = 30).place(x = 10, y = 190)
CTkButton(frame, text= "5", font=("arial", 60, "bold"),command = lambda : show("5"), border_width = 2, width = 120,height = 30).place(x = 140, y = 190)
CTkButton(frame, text= "6", font=("arial", 60, "bold"),command = lambda : show("6"), border_width = 2, width = 120,height = 30).place(x = 270, y = 190)
CTkButton(frame, text= "+", font=("arial", 60, "bold"),command = lambda : show("+"), border_width = 2, width = 120,height = 30, fg_color = "white",text_color = "black",hover_color = "grey").place(x = 400, y = 190)
CTkButton(frame, text= "1", font=("arial", 60, "bold"),command = lambda : show("1"), border_width = 2, width = 120,height = 30).place(x = 10, y = 280)
CTkButton(frame, text= "2", font=("arial", 60, "bold"),command = lambda : show("2"),border_width = 2, width = 120,height = 30).place(x = 140, y = 280)
CTkButton(frame, text= "3", font=("arial", 60, "bold"),command = lambda : show("3"), border_width = 2, width = 120,height = 30).place(x = 270, y = 280)
CTkButton(frame, text= "=", font=("arial", 60, "bold"),command = lambda : calculate(), border_width = 2, width = 120,height = 170, fg_color = "white",text_color = "black",hover_color = "grey").place(x = 400, y = 280)
CTkButton(frame, text= "0", font=("arial", 60, "bold"),command = lambda : show("0"), border_width = 2, width = 250,height = 30).place(x = 10, y = 370)
CTkButton(frame, text= ".", font=("arial", 60, "bold"),command = lambda : show("."), border_width = 2, width = 120,height = 30).place(x = 270, y = 370)



root.mainloop()

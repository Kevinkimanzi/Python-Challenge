# Tkinter - Python library that can be used to create 
#           basic graphical user interface (GUI) applications
#widgets - GUI elements: buttons, textboxes, labels, images
#windows - container to hold widgets

from tkinter import *
import os

window = Tk() #instantiate an instance od a window
window.geometry("420x420")
window.title("Kevin Kimanzi")

#icon = PhotoImage(file = "kevinkimanzi.png")
#window.iconphoto(True,icon)

window.config(background="white")

#photo = PhotoImage(file= 'kevinkimanzi.png')



label = Label(window,
            text = "Hello World",
            font=('arial',40, 'bold'),
            fg= 'green',   # fg ni text color
            bg='white')   #background photo

label.pack()

# BUTTONS  - You click it, then it does stuff
count = 0
def click():
    global count
    count +=1
    print("You clicked the button")

button = Button(window,
                text = "click me!",
                command = click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="white",
                state=ACTIVE,
                ) #to disable the click but change to DISABLE

button.pack()


# entry widget = textbox that accept a single line of user

def submit():
    username = entry.get()
    print("Hello "+username )

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)

entry = Entry(window,
            font=('arial', 30),
            fg= "black",
            bg="white")

entry.pack(side=LEFT)

submit_button=Button(window,
                    text ="Submit",
                    command=submit)

submit_button.pack(side=RIGHT)

delete_button=Button(window,
                    text ="Delete-All",
                    command=delete)

delete_button.pack(side=RIGHT)

backspace_button=Button(window,
                    text ="X",
                    command=backspace)

backspace_button.pack(side=RIGHT)


# CHECKBOX
def display():
    if(x.get()==1):
        print("You agree")
    else:
        print("You don't agree!")

x = IntVar()
check_button = Checkbutton(window,
                        text ="I agree to terms and condition",
                        variable = x,
                        onvalue=1,
                        offvalue=0,
                        command=display,
                        font=('arial',20),
                        fg= 'black',
                        bg='#00FF00',
                        activebackground='#00FF00',
                        activeforeground='black',
                        padx =25,
                        pady = 10,
                        compound = 'left')

check_button.pack()


# radio buttons = similar to checkbox, but you can only select one from a group

food = ["pizza", "humburger","hotdog"]

def order():
    if (x.get==0):
        print("You ordered Pizza")
    elif(x.get==1):
        print("You ordered Hamburger")
    elif(x.get==2):
        print("You ordered hotdog")
x = IntVar()

for index in range(len(food)):
    radio_button =Radiobutton(window,
                            text = food[index], #add text to radiobuttons
                            variable=x, 
                            value=index, #assign radiobutton different value
                            indicatoron=0, # eliminate 0
                            width=300,
                            command = order
                            )
    radio_button.pack(anchor=W)

# LISTBOX = A listing of selected text items within it's own container

def submit1():

    food = []

    for index in list_box.curselection():
        food.insert(index, list_box.get(index))
    print("You have ordered: ")

    for index in food:
        print(index)

# print(list_box.get(list_box.curselection()))  will allow you to order only one

def add():
    list_box.insert(list_box.size(), entryBox.get())
    list_box.config(height=list_box.size())

def delete():
    for index in reversed(list_box.curselection()):
        list_box.delete(index)
#   list_box.delete(list_box.curselection())
    list_box.config(height=list_box.size())

list_box = Listbox(window,
                bg = "#f7ffde",
                font= ("constantia", 35),
                width=12,
                selectmode=MULTIPLE
                )

list_box.pack()
list_box.insert(1,"pizza")
list_box.insert(2,"pasta")
list_box.insert(3,"pilau")
list_box.insert(4,"Ugali")
list_box.insert(5,"matoke")

list_box.config(height=list_box.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text = "submit", command=submit1)
submitButton.pack

addButton = Button(window,text = "add", command=add)  #allow user to add more like add soda, Juice to the list
addButton.pack()

deleteButton = Button(window,text = "Delete", command=delete)  #allow user to add more like add soda, Juice to the list
deleteButton.pack()



# MESSAGE BOX

def click1():
    messagebox.showinfo(title="This is an info message box", message = 'you are a person')
    
    messagebox.showwarning(title="This is an info message box", message = 'you are a person')

from tkinter import messagebox
button1 = Button(window,
                command = click1,
                text= 'click me'
                )
button1.pack()


window.mainloop() #place window on comp screen and listen for events































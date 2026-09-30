import tkinter as tk
from tkinter.ttk import *

list = []

def button_clicked():
    print("Button clicked!")

def exit():
    print("You are leaving! Goodbye!")
    
def add_to_list_window():
    new_window = tk.Toplevel(root)
    new_window.title("Add to the list")
    new_window.geometry("320x275")

    label = tk.Label(new_window, text="Please add to your list")
    label.pack(pady=20)

    for i in range(5):
        entry = tk.Entry(new_window)
        entry.pack(pady=5)
        list.append(entry)

    btn = tk.Button(new_window, text="Submit", command=read_inputs)
    btn.pack()

def show_my_list():
    my_list_window = tk.Toplevel(root)
    my_list_window.title("This is your list")
    my_list_window.geometry("320x275")

    label = tk.Label(my_list_window, print(list))
    label.pack(pady=20)

    
root = tk.Tk()


def read_inputs():
    data = [e.get() for e in list]
    print("User inputs:", data)



#Title
root.title("Nik's To Do List")

# Creating a button with specified options
button = tk.Button(root, 
                   text="Add to your list", 
                   command=add_to_list_window,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=30,
                   pady=5,
                   width=15,
                   wraplength=100)
button1 = tk.Button(root, 
                   text="Remove from your list", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=30,
                   pady=5,
                   width=15,
                   wraplength=100)
button2 = tk.Button(root, 
                   text="Show your list", 
                   command=show_my_list,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=30,
                   pady=5,
                   width=15,
                   wraplength=100)
button3 = tk.Button(root, 
                   text="Edit your list", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=30,
                   pady=5,
                   width=15,
                   wraplength=100)
button4 = tk.Button(root, 
                   text="Exit", 
                   command=root.destroy, 
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=30,
                   pady=5,
                   width=15,
                   wraplength=100)


button.pack(padx=20, pady=20)
button1.pack(padx=20, pady=20)
button2.pack(padx=20, pady=20)
button3.pack(padx=20, pady=20)
button4.pack(padx=20, pady=20)  

root.mainloop()
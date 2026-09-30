import tkinter as tk
from tkinter.ttk import *


def button_clicked():
    print("Button clicked!")

def exit():
    print("You are leaving! Goodbye!")
    
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Add to the list")
    new_window.geometry("320x200")

    label = tk.Label(new_window, text="This is a new window!")
    label.pack(pady=20)
    
root = tk.Tk()

#Title
root.title("Nik's To Do List")

# Creating a button with specified options
button = tk.Button(root, 
                   text="Add to your list", 
                   command=open_new_window,
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
import tkinter as tk
import hello
from tkinter.constants import END

def handle_click(event):
    name=entry.get()
    age=entry2.get()
    hello.printname(name,age)
    entry.delete(0,END)
    entry2.delete(0,END)

def reset_entry(event):
    entry.delete(0,END)
    entry2.delete(0,END)

window =tk.Tk()
window.geometry("400x300")

frame_a= tk.Frame()
frame_b=tk.Frame()

greeting = tk.Label(master=frame_a,
    text="Sláðu inn nafn",
    fg="black",
    bg="white",
    width=43,
    height=5
)

entry = tk.Entry(master=frame_a,
    fg="black", 
    bg="white",
    width=50,
)
label2 = tk.Label(master=frame_b,
    width=43,
    height=5,
    bg="white",
    text="Sláðu inn aldur"
)
entry2 = tk.Entry(master=frame_b,
    bg="white",
    width=50
)

#entry.bind("<Return>",handle_click)
window.bind("<Return>",handle_click)

button = tk.Button(master=window,text="Staðfesta")
button2 = tk.Button(master=window,text="Hreynsa allt")

button.bind("<Button-1>", handle_click)
button2.bind("<Button-1>", reset_entry)

greeting.pack()
label2.pack()
entry.pack()
entry2.pack()
frame_a.pack()
frame_b.pack()
button.pack()
button2.pack()
window.mainloop()


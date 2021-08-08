import tkinter as tk
import hello
from tkinter.constants import END

def handle_click(event):
    name=entry.get()
    hello.printname(name)
    entry.delete(0,END)

window =tk.Tk()
window.geometry("400x400")

frame_a= tk.Frame()
frame_b=tk.Frame()

greeting = tk.Label(master=frame_a,
    text="Sláðu inn nafn",
    fg="black",
    bg="white",
    width=43,
    height=5
)

entry = tk.Entry(master=frame_b,
    fg="black", 
    bg="white",
    width=50,
)

entry.bind("<Return>",handle_click)

button = tk.Button(master=window,text="Staðfesta")

button.bind("<Button-1>", handle_click)

greeting.pack()
entry.pack()

frame_a.pack()
frame_b.pack()
button.pack()
window.mainloop()


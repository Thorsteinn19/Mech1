import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
}

window =tk.Tk()


def handle_click(event):
    print(entry.get())

frame_a= tk.Frame()
frame_b=tk.Frame()

greeting = tk.Label(master=frame_a,
    text="Prufutexti",
    fg="white",
    bg="#34A2FE",
    width=43,
    height=1
)

greeting.pack()

entry = tk.Entry(master=frame_b,
    fg="black", 
    bg="white",
    width=50
)
entry.pack()

frame_a.pack()
frame_b.pack()

button = tk.Button(master=window,text="Click me!")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()


import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.master.title("Appið mitt")
            self.pack()
            self.master.geometry("400x200")
            self.create_button(xpos=15,ypos=120,buttontext="Click here",bcommand=self.say_hi)
            self.create_button(xpos=15,ypos=140,buttontext="press",bcommand=self.say_bi)
            self.quit_button(xpos=320,ypos=133)
            
    def create_button(self,xpos=0,ypos=0,buttontext="None",bcommand=None):
        self.frame=tk.Frame()
        self.frame.place(x=xpos,y=ypos)
        self.hi_there = tk.Button(self.frame)
        self.hi_there["text"] = buttontext
        self.hi_there["command"] = bcommand
        self.hi_there.pack()

    def quit_button(self,xpos,ypos):
        self.frame=tk.Frame()
        self.frame.place(x=xpos,y=ypos)
        self.quit = tk.Button(self.frame, text="QUIT", fg="red",
                                command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
    
    def say_bi(self):
        print("Hastala vista")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

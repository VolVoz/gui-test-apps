import Tkinter
import tkMessageBox

top = Tkinter.Tk()  # init a tkinter window


def hello_world():  # init info message window
    tkMessageBox.showinfo("Say Hello", "Hello World")


B1 = Tkinter.Button(top, text="Say Hello", command=hello_world)
B1.pack()  # pack widgets widgets on window

top.mainloop()

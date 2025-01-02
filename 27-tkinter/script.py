import tkinter

window = tkinter.Tk()
window.title("DanGUI")
window.minsize(width=500, height=300)
my_label = tkinter.Label(window, text="Hello World!")
my_label.pack()


window.mainloop()
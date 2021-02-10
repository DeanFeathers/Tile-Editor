from tkinter import *
from tkinter import colorchooser
global img

root = Tk()
root.title("Tile Editor")
root.configure(bd=10)

canvas = Canvas(root, width=240, height=240, bg="Gainsboro")
canvas.grid(column=0, row=0, columnspan=2)


def color1(event):
    current = event.widget.find_withtag('current')
    item = current[0]
    canvas.itemconfigure(item, fill=color, outline=color)


def color2(event):
    current = event.widget.find_withtag('current')
    item = current[0]
    canvas.itemconfigure(item, fill="Ghost White", outline="Gainsboro")


def new():
    grid()


color = "Blue Violet"


def change_color():
    global color
    c = colorchooser.askcolor()
    color = c[1]
    button1.configure(bg=color)


def save():
    canvas.postscript(file="image.eps")
    from PIL import Image
    img = Image.open("image.eps")
    img.save("image.png", "png")


def open_image(self):

    """from PIL import ImageTk, Image
    img = ImageTk.PhotoImage(Image.open("image.png"))  # PIL solution
    canvas.create_image(20, 20, anchor=NW, image=img)"""


button1 = Button(root, text="Select a Colour", height=2, bg=color, bd=0, cursor="hand2", command=change_color)
button1.grid(column=0, row=1, pady=2, sticky=E+W)

button2 = Button(root, text="Click to Save Image", height=2, cursor="hand2", command=save)
button2.grid(column=0, row=2, sticky=E+W)

button3 = Button(root, text="New", height=2, cursor="hand2", command=new)
button3.grid(column=1, row=1, sticky=E+W)

button3 = Button(root, text="Open Image", height=2, cursor="hand2", command=open_image)
button3.grid(column=1, row=2, sticky=E+W)


def grid():
    for y in range(2, 500, 15):
        for x in range(2, 600, 15):
            draw = canvas.create_rectangle(x, y, x+15, y+15, fill="Ghost white", width=1, outline="Gainsboro")
            canvas.tag_bind(draw, '<Button-1>', color1)
            canvas.tag_bind(draw, '<Button-3>', color2)


grid()

root.mainloop()

from tkinter import *
import random

# Constants
RADIUS = 10

def random_color():
    colors = ["red", "blue", "pink", "cyan", "black", "aqua", "green", "yellow", "purple", "orange", "brown", "grey"]
    color = random.randrange(0,len(colors))
    return colors[color]

def exit_screen():
    root.destroy()

def display_coordinates(event):
    create_circle(event.x, event.y, RADIUS)
    counter.set(counter.get()+1)

def create_circle(xr, yr, radius):
    x0 = xr - radius
    y0 = yr - radius
    x1 = xr + radius
    y1 = yr + radius
    color = random_color()
    canvas.create_oval(x0, y0, x1, y1, fill=color)
    XData.set(xr)
    YData.set(yr)
    colorData.set(color)
    labelColor.config(fg=color)

def clean_screen():
    canvas.delete("all")
    counter.set(0)
    XData.set(0)
    YData.set(0)
    labelColor.config(fg='black')
    colorData.set("-")

root = Tk()
root.attributes("-fullscreen", True)
root.title("Touch Debugger")

# Variables
counter = IntVar()
counter.set(0)
XData = IntVar()
XData.set(0)
YData = IntVar()
YData.set(0)
colorData = StringVar()
colorData.set("-")

root.update()
# Drawable canvas
canvas = Canvas(root, width=root.winfo_width()-100, height=root.winfo_height()-50, background='white')
canvas.grid(row=0, column=0, rowspan=2, columnspan=2)
canvas.bind('<Button-1>', display_coordinates) # Click event

# Counter groupbox
groupboxCounter = LabelFrame(root, text="Counter:", bd=0)
groupboxCounter.grid(row=0, column=2)
labelCounter = Label(groupboxCounter, font="Times 20 bold", padx=5, pady=5, textvariable=counter)
labelCounter.grid(row=0, column=0)

# Circle information groupbox
groupboxData = LabelFrame(root, text="Circle data")
groupboxData.grid(row=1,column=2)
labelXStatic = Label(groupboxData, text='X:')
labelXStatic.grid(row=0, column=0)
labelX = Label(groupboxData, padx=5, pady=5, textvariable=XData)
labelX.grid(row=0, column=1)
labelYStatic = Label(groupboxData, text='Y:')
labelYStatic.grid(row=1, column=0)
labelY = Label(groupboxData, padx=5, pady=5, textvariable=YData)
labelY.grid(row=1, column=1)
labelColor = Label(groupboxData, padx=5, pady=5, textvariable=colorData, font=" Time 12 bold")
labelColor.grid(row=2, column=0, columnspan=2)

# Bottom buttons
buttonClean = Button(root, padx=10, pady=5, width=10, text="Clean", command=clean_screen)
buttonClean.grid(row=4, column=0, columnspan=1)

buttonExit = Button(root, padx=10, pady=5, width=10, text="Exit", command=exit_screen)
buttonExit.grid(row=4, column=1, columnspan=1)


root.mainloop()

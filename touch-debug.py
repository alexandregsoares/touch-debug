from tkinter import *
import random

# Constants
RADIUS = 10

#counter = 0

def random_color():
    colors = ["red", "blue", "pink", "cyan", "black", "aqua", "green", "yellow", "purple", "orange", "brown", "grey"]
    color = random.randrange(0,len(colors))
    #print(color)
    #print(colors[color])
    return colors[color] 

def exit_screen():
    #root.attributes("-fullscreen", False)
    root.destroy()

def display_coordinates(event):
    #label['text']=str(event.x)
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

root = Tk()
root.attributes("-fullscreen", True)
root.title("Touch Debug")

#Variables
counter = IntVar()
counter.set(0)

XData = IntVar()
XData.set(0)
YData = IntVar()
YData.set(0)

root.update()
canvas = Canvas(root, width=root.winfo_width()-190, height=root.winfo_height()-50, background='white')
canvas.grid(row=0, column=0, rowspan=3, columnspan=2)
canvas.bind('<Button-1>', display_coordinates)

labelCounter = Label(font="Times 20 bold", padx=5, pady=5, textvariable=counter)
labelCounter.grid(row=0, column=2)

labelX = Label(font="Times 20 bold", padx=5, pady=5, textvariable=XData)
labelX.grid(row=1, column=2)

labelY = Label(font="Times 20 bold", padx=5, pady=5, textvariable=YData)
labelY.grid(row=2, column=2)


w = Button(root, padx=10, pady=5, width=10, text="Exit", command=exit_screen)
w.grid(row=4, column=0)

#label = Label(bd=4, relief="solid", font="Times 12 bold", bg="white", fg="black", text="text")
#label.grid(row=1, column=1)

root.mainloop()

from tkinter import *
import random

# Constants
RADIUS = 10
 
def random_color():
    colors = ["red", "blue", "pink", "cyan", "black", "aqua", "green", "yellow", "purple", "orange", "brown", "grey"]
    color = random.randrange(0,len(colors))
    print(color)
    print(colors[color])
    return colors[color] 

def exit_screen():
    #root.attributes("-fullscreen", False)
    root.destroy()

def display_coordinates(event):
    #label['text']=str(event.x)
    create_circle(event.x, event.y, RADIUS)

def create_circle(xr, yr, radius):
    x0 = xr - radius
    y0 = yr - radius
    x1 = xr + radius
    y1 = yr + radius
    color = random_color()
    canvas.create_oval(x0, y0, x1, y1, fill=color)

root = Tk()
root.attributes("-fullscreen", True)
root.title("Touch Debug")

root.update()
canvas = Canvas(root, width=root.winfo_width(), height=root.winfo_height()-50, background='white')
canvas.grid(row=0, column=0, columnspan=1)

canvas.bind('<Button-1>', display_coordinates)

w = Button(root, padx=10, pady=5, width=10, text="Exit", command=exit_screen)
w.grid(row=1, column=0)

#label = Label(bd=4, relief="solid", font="Times 12 bold", bg="white", fg="black", text="text")
#label.grid(row=1, column=1)

root.mainloop()

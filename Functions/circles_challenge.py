import tkinter
import math

#parabola function
#changing parabola to do everything

def parabola(page,size):
    for x in range(size):
        y = x**2 / size
        plot(page,x,y)
        plot(page,-x,y)
    return y


def circle(page,radius,g,h):
    for x in range(g,g+radius):
        y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
        plot(page,x,y)
        plot(page,x,2*h-y)
        plot(page,x,2 * h - y)
        plot(page,2 * g - x ,y)
        plot(page,2 * g - x,2 * h - y)



#shifting origin to center, default is top left corner
def draw_axes(canvas):
    canvas.update()   # to access canvas width and height
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin,-y_origin,x_origin,y_origin))
    canvas.create_line(-x_origin,0,x_origin,0,fill="red")
    canvas.create_line(0,-y_origin,0,y_origin,fill="red")

def plot(canvas,x,y):
    canvas.create_line(x,-y,x+1,-y+1,fill="blue")

mainwindow = tkinter.Tk()
mainwindow.geometry('640x480')
mainwindow.title("Parabola")

canvas = tkinter.Canvas(mainwindow,width=640,height=480)
canvas.grid(row=0,column=0)

draw_axes(canvas)


#cant indivdually plot points on a canvas but a line of length 1 can be drawn
#canvas has y axis increasing top down
parabola(canvas,100)
parabola(canvas,200)
circle(canvas,100,100,100)
circle(canvas,100,100,-100)
circle(canvas,100,-100,100)
circle(canvas,100,-100,-100)
circle(canvas,10,30,30)
circle(canvas,10,30,-30)
circle(canvas,10,-30,30)
circle(canvas,10,-30,-30)
circle(canvas,30,0,0)
mainwindow.mainloop()

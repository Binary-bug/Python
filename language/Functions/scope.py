import tkinter

#parabola function

def parabola(x):
    y = x**2 / 100
    return y



#shifting origin to center, default is top left corner
def draw_axes(canvas):
    canvas.update()   # to access canvas width and height
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin,-y_origin,x_origin,y_origin))
    canvas.create_line(-x_origin,0,x_origin,0,fill="red")
    canvas.create_line(0,-y_origin,0,y_origin,fill="red")
# to print all local variables local to a method
    print(locals())


def plot(canvas,x,y):
    canvas.create_line(x,y,x+1,y+1,fill="black")

mainwindow = tkinter.Tk()
mainwindow.geometry('640x480')
mainwindow.title("Parabola")

canvas = tkinter.Canvas(mainwindow,width=320,height=480)
canvas.grid(row=0,column=0)

canvas2 = tkinter.Canvas(mainwindow,width=320,height=480,background="blue")
canvas2.grid(row=0,column=1)

draw_axes(canvas)
draw_axes(canvas2)

#printing details about an object
print(repr(canvas),repr(canvas2))


#cant indivdually plot points on a canvas but a line of length 1 can be drawn
#canvas has y axis increasing top down
for x in range(-100,100):
    y = parabola(x)
    plot(canvas,x,-y)

mainwindow.mainloop()

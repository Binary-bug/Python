#NOTE

#Everything in Tk is a window and objects are placed in a hierarchy

import tkinter



mainwindow = tkinter.Tk()

mainwindow.title("using Canvas widget")
mainwindow.geometry("640x480")

label = tkinter.Label(mainwindow,text='Hello World')
label.pack(side='top')


leftframe = tkinter.Frame(mainwindow)
leftframe.pack(side='left',anchor='n',fill=tkinter.Y,expand=False)
#canvas = tkinter.Canvas(mainwindow,relief='raised',borderwidth=1) #relief = raised gives a raised appearance
canvas = tkinter.Canvas(leftframe,relief='raised',borderwidth=1)

##placement of the canvas
#canvas.pack(side='bottom')


##filling the entire canvas
#canvas.pack(side='left',fill=tkinter.Y) to fill vertically
#canvas.pack(side='left',fill=tkinter.X) is expectedto fill horizontally
##but above line wont work
#canvas.pack(side='left',fill=tkinter.X,expand=True)

#alternatively even this wont help unless u use expand
#canvas.pack(side='left')
canvas.pack(side='left',anchor='n')

#rightframe
rightframe=tkinter.Frame(mainwindow)
rightframe.pack(side='right',anchor='n',expand=True)

#adding buttons

# button1 = tkinter.Button(mainwindow,text="button1")
# button2 = tkinter.Button(mainwindow,text="button2")
# button3 = tkinter.Button(mainwindow,text="button3")


##buttons are placed in frame now
button1 = tkinter.Button(rightframe,text="button1")
button2 = tkinter.Button(rightframe,text="button2")
button3 = tkinter.Button(rightframe,text="button3")

# button1.pack(side='left',anchor='n') # note: when widgets share the same side,
# button2.pack(side='left',anchor='s') # they are placed adjacent to each other
# button3.pack(side='left', anchor='e') # hence use anchor default is center

#now that buttons are added to the rightframe , we no longer need anchor
button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')

#In the above lines anchor is working only on line 36,37. since anchor only
#affects vertical positioning since buttons are packed to the vertical side of the window
# to see the effect try exchanging line 36,38

#pack manager is highly limited in options
mainwindow.mainloop()

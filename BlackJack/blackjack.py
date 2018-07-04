import tkinter
import random


def load_images(cardimages):
    suits=['heart','club','diamond','spade']
    facecards=['jack','queen','']



























mainwindow = tkinter.Tk()

#Setup the screen and frames for the dealer and player

mainwindow.title("Black Jack")
mainwindow.geometry("640x480")

result_text = tkinter.StringVar()
result = tkinter.Label(mainwindow,textvariable=result_text)
result.grid(row=0,column=0,columnspan=3)

cardframe = tkinter.Frame(mainwindow, relief='sunken', borderwidth = 1, background ="green")
cardframe.grid(row=1, column = 0, sticky ='news', columnspan=3, rowspan=2)


dealerscorelabel = tkinter.IntVar()
tkinter.Label(cardframe, text="dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(cardframe, textvariable=dealerscorelabel, background="green", fg="white").grid(row=1, column=0)


#Embedded frame to hold the card images

dealercardframe=tkinter.Frame(cardframe,background="green")
dealercardframe.grid(row=0,column=1,sticky="ew",rowspan=2)


playerscorelabel = tkinter.IntVar()
tkinter.Label(cardframe,text="Player",background="green",fg="white").grid(row=2,column=0)
tkinter.Label(cardframe,textvariable=playerscorelabel,background="green",fg="white").grid(row=3,column=0)


#embedded frame to hold the card images
playercardframe = tkinter.Frame(cardframe,background="green")
playercardframe.grid(row=2,column=1,sticky='ew',rowspan=2)

#adding buttons
button_frame = tkinter.Frame(mainwindow)
button_frame.grid(row =3,column=0,columnspan=3,sticky='w')

dealerbutton = tkinter.Button(button_frame,text="Dealer")
dealerbutton.grid(row=0,column=0)

playerbutton = tkinter.Button(button_frame,text="Player")
playerbutton.grid(row=0,column=1)



mainwindow.columnconfigure(0,weight=1)
mainwindow.columnconfigure(1,weight=1)
mainwindow.columnconfigure(2,weight=1)


mainwindow.rowconfigure(0,weight=5)
mainwindow.rowconfigure(1,weight=20)
mainwindow.rowconfigure(2,weight=20)
mainwindow.rowconfigure(3,weight=10)

cardframe.rowconfigure(0,weight=1)
cardframe.rowconfigure(1,weight=1)
cardframe.rowconfigure(2,weight=1)
cardframe.rowconfigure(3,weight=1)

mainwindow.mainloop()
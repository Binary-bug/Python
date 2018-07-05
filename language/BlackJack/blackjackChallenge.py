import tkinter
import random




def load_images(cardimages):
    suits=['heart','club','diamond','spade']
    facecards=['jack','queen','king']

    for suit in suits:
        for card in range(1,11):
            name= 'cards/{}_{}.{}'.format(str(card),suit,'png')
            image=tkinter.PhotoImage(file=name)
            cardimages.append((card,image))

    # the face cards
        for card in facecards:
            name='cards/{}_{}.{}'.format(card,suit,'png')
            image=tkinter.PhotoImage(file=name)
            cardimages.append((10,image))


def dealcard(frame):
    nextcard = deck.pop(0) # get the new card from deck
    tkinter.Label(frame,image=nextcard[1],relief='raised').pack(side='left')
    return nextcard


#calculate score given a hand
def scorehand(hand):
    score = 0
    ace = False
    for nextcard in hand:
        cardvalue = nextcard[0]
        if cardvalue == 1 and not ace:
            cardvalue = 11
            ace =True
        score +=cardvalue
        if score > 21 and ace:
            score -= 10
            ace = False
    return score

def dealerdeal():
    dealerscore = scorehand(dealerhand)
    while 0 < dealerscore < 17:
        dealerhand.append(dealcard(dealercardframe))
        dealerscore=scorehand(dealerhand)
        dealerscorelabel.set(dealerscore)

    playerscore = scorehand(playerhand)
    if playerscore < dealerscore <= 21:
        result_text.set("Dealer wins!")
    elif dealerscore == playerscore:
        result_text.set("Its A Draw")
    else:
        result_text.set("Player wins!")


def playerdeal():
    playerhand.append(dealcard(playercardframe))
    playerscore=scorehand(playerhand)
    playerscorelabel.set(playerscore)
    if playerscore > 21:
        result_text.set("Dealer wins!")



def newgame():
    global deck
    global dealercardframe
    global playercardframe
    # creating a new deck of cards and shuffle them
    deck = list(cards)
    random.shuffle(deck)

    #empty dealer and playerhands
    dealerhand.clear()
    playerhand.clear()

    #clearing frames but not destroying it
    dealercardframe.destroy()
    playercardframe.destroy()

    #creating two new frames
    dealercardframe = tkinter.Frame(cardframe, background="green")
    dealercardframe.grid(row=0, column=1, sticky="ew", rowspan=2)

    # embedded frame to hold the player card images
    playercardframe = tkinter.Frame(cardframe, background="green")
    playercardframe.grid(row=2, column=1, sticky='ew', rowspan=2)

    # initialise table
    playerdeal()
    dealerhand.append(dealcard(dealercardframe))
    dealerscorelabel.set(scorehand(dealerhand))
    playerdeal()

    #clear result field
    result_text.set("")

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


#Embedded frame to hold the dealer card images

dealercardframe=tkinter.Frame(cardframe,background="green")
dealercardframe.grid(row=0,column=1,sticky="ew",rowspan=2)


playerscorelabel = tkinter.IntVar()
tkinter.Label(cardframe,text="Player",background="green",fg="white").grid(row=2,column=0)
tkinter.Label(cardframe,textvariable=playerscorelabel,background="green",fg="white").grid(row=3,column=0)


#embedded frame to hold the player card images
playercardframe = tkinter.Frame(cardframe,background="green")
playercardframe.grid(row=2,column=1,sticky='ew',rowspan=2)

#adding buttons
button_frame = tkinter.Frame(mainwindow)
button_frame.grid(row =3,column=0,columnspan=3,sticky='w')

dealerbutton = tkinter.Button(button_frame,text="Dealer",command=dealerdeal) # since we cannot pass arguments to function here
dealerbutton.grid(row=0,column=0)

playerbutton = tkinter.Button(button_frame,text="Player",command=playerdeal)
playerbutton.grid(row=0,column=1)



mainwindow.columnconfigure(0,weight=1)
mainwindow.columnconfigure(1,weight=1)
mainwindow.columnconfigure(2,weight=1)
mainwindow.columnconfigure(3,weight=1)
mainwindow.columnconfigure(4,weight=1)


mainwindow.rowconfigure(0,weight=5)
mainwindow.rowconfigure(1,weight=20)
mainwindow.rowconfigure(2,weight=20)
mainwindow.rowconfigure(3,weight=10)

cardframe.rowconfigure(0,weight=1)
cardframe.rowconfigure(1,weight=1)
cardframe.rowconfigure(2,weight=1)
cardframe.rowconfigure(3,weight=1)


# loading cards
cards=[]
load_images(cards)


#creating a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

#create list to store dealers hand
dealerhand=[]

#creating list to store players hand
playerhand=[]


#initialise table
playerdeal()
dealerhand.append(dealcard(dealercardframe))
dealerscorelabel.set(scorehand(dealerhand))
playerdeal()


#Button to restart a new game PART of CHALLENGE
newgamebutton_frame = tkinter.Frame(mainwindow)
newgamebutton_frame.grid(row =3,column=3,columnspan=2,sticky='w')

newgamebutton = tkinter.Button(newgamebutton_frame,text="New Game",command=newgame)
newgamebutton.grid(row=0,column=0)


#Stop game

stopgamebutton = tkinter.Button(newgamebutton_frame,text="Stop",command=mainwindow.quit)
stopgamebutton.grid(row=0,column=1)
mainwindow.mainloop()
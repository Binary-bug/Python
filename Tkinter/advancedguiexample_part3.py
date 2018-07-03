import tkinter
import os

mainwindow = tkinter.Tk()

mainwindow.title("GridGeomertyManager")
mainwindow.geometry('640x480-0-200')
mainwindow['padx'] = 8

#creating the label
label = tkinter.Label(mainwindow,text='Grid Demo')
label.grid(row=0,column=0,columnspan=3)




mainwindow.columnconfigure(0,weight=100)
mainwindow.columnconfigure(1,weight=1)
mainwindow.columnconfigure(2,weight=1000)
mainwindow.columnconfigure(3,weight=600)
mainwindow.columnconfigure(4,weight=1000)

mainwindow.rowconfigure(0,weight=1)
mainwindow.rowconfigure(1,weight=10)
mainwindow.rowconfigure(2,weight=1)
mainwindow.rowconfigure(3,weight=3)
mainwindow.rowconfigure(4,weight=5)

#adding the listbox
filelist = tkinter.Listbox(mainwindow)
filelist.grid(row=1,column=0,sticky='news',rowspan=2)
filelist.config(border=2,relief='sunken')

#code to populate the listbox

for zone in os.listdir('/usr/bin'):
    filelist.insert(tkinter.END,zone) # when inserting an item in the listbox
# we need to specify the insertion point , hence we are using tkinter constant called tkinter.END
#end places at the end of the list, you can also specify a number



#adding a scroll bar
scrollbar = tkinter.Scrollbar(mainwindow,orient=tkinter.VERTICAL,command=filelist.yview) ##command is used to associate actions to widgets
scrollbar.grid(row=1,column=1,rowspan=2,sticky='nsw')
#additional to command we need this to link scrollbox to listbox
filelist['yscrollcommand'] = scrollbar.set


#frame for the radiobuttons
optionframe = tkinter.LabelFrame(mainwindow,text='File Details') # labelframe is chosen since it allows a caption to be set
optionframe.grid(row=1,column=2,sticky='ne')

#creating 3 radiobuttons that share the same variable so that only one can be selected
#at any point of time

rbvalue = tkinter.IntVar()
rbvalue.set(1) # sets the default button
radio1 = tkinter.Radiobutton(optionframe,text='Filename',value=1,variable=rbvalue)
radio2 = tkinter.Radiobutton(optionframe,text='Path',value=2,variable=rbvalue)
radio3 = tkinter.Radiobutton(optionframe,text='TimeStamp',value=3,variable=rbvalue)

radio1.grid(row=0,column=0,sticky='w')
radio2.grid(row=1,column=0,sticky='w')
radio3.grid(row=2,column=0,sticky='w')


#creating result widget
resultlabel = tkinter.Label(mainwindow,text="result")
resultlabel.grid(row=2,column=2,sticky='nw')
result=tkinter.Entry(mainwindow)
result.grid(row=2,column=2,sticky='sw')


#frame for the time spinners
timeframe = tkinter.LabelFrame(mainwindow,text="Time")
timeframe.grid(row=3,column=0,sticky='new')

#creating spinners
hourspinner = tkinter.Spinbox(timeframe,width=2,values=tuple(range(0,24)))
hourspinner.grid(row=0,column=0)
tkinter.Label(timeframe,text=':').grid(row=0,column=1)

minutespinner=tkinter.Spinbox(timeframe,width=2,values=tuple(range(0,60)))
minutespinner.grid(row=0,column=2)
tkinter.Label(timeframe,text=':').grid(row=0,column=3)

secondspinner=tkinter.Spinbox(timeframe,width=2,from_=0,to=59) # alternative to values
secondspinner.grid(row=0,column=4)


#padding to adjust the position of widgets, can be done for both vertically and horizontally
timeframe['padx'] = 36

#frame for the date spinners
dateframe = tkinter.Frame(mainwindow)
dateframe.grid(row=4,column=0,sticky='new')

#creating date labels
daylabel = tkinter.Label(dateframe,text="Day")
monthlabel = tkinter.Label(dateframe,text="Month")
yearlabel = tkinter.Label(dateframe,text="Year")

daylabel.grid(row=0,column=0,sticky='w')
monthlabel.grid(row=0,column=1,sticky='w')
yearlabel.grid(row=0,column=2,sticky='w')


#creating date spinners
dayspinner = tkinter.Spinbox(dateframe,width=5,values=tuple(range(1,32)))
dayspinner.grid(row=1,column=0)

monthspinner=tkinter.Spinbox(dateframe,width=5,values=('jan',"feb","mar","apr","may","jun","aug","sep","oct","nov","dec"))
monthspinner.grid(row=1,column=1)


yearspinner=tkinter.Spinbox(dateframe,width=5,from_=2000,to=2020) # alternative to values
yearspinner.grid(row=1,column=2)



## adding functionarlity

# OK and Cancel Buttons
okbutton=tkinter.Button(mainwindow,text="OK")
okbutton.grid(row=4,column=3,sticky='e')

cancelbutton=tkinter.Button(mainwindow,text="Cancel",command=mainwindow.quit) # should use destroy since it cleans up
cancelbutton.grid(row=4,column=4,sticky='w')





mainwindow.mainloop()

print(rbvalue.get()) # to print button selected value

# resize the gui window to see the effect of weight
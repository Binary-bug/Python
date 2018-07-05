import tkinter
import os

mainwindow = tkinter.Tk()

mainwindow.title("GridGeomertyManager")
mainwindow.geometry('640x480-0-200')

#creating the label
label = tkinter.Label(mainwindow,text='Grid Demo')
label.grid(row=0,column=0,columnspan=3)




mainwindow.columnconfigure(0,weight=1)
mainwindow.columnconfigure(1,weight=1)
mainwindow.columnconfigure(2,weight=3)
mainwindow.columnconfigure(3,weight=3)
mainwindow.columnconfigure(4,weight=3)

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

mainwindow.mainloop()

print(rbvalue.get()) # to print button selected value


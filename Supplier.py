from tkinter import *
from FindFrame import *
def sup_find():
    Sup1 = Tk()
    frame1=Frame(Sup1,padx=20,pady=100)
    suppframe = Frame(frame1, relief=RAISED, borderwidth=1, pady=10)

    # add supplier id Label
    suppid = Label(suppframe, text="Supplier ID : ", padx=10, pady=10)
    suppid.config(font=('ariel', 12, 'bold'))
    suppid.grid(row=0, column=0)

    # add text entry block
    b = StringVar()
    findentry = Entry(suppframe, textvariable=b)
    findentry.grid(row=0, column=1, padx=10)

    # add find button
    findbutton = Button(suppframe, text="Find", padx=30,)
    findbutton.grid(row=0, column=3, padx=10)

    # add Cancel button
    cancelbutton = Button(suppframe, text="Cancel", padx=30, command=quit)
    cancelbutton.grid(row=0, column=4, padx=10)

    suppframe.pack()
    label0=Label(frame1,text="Supplier ID : ")
    label0.config(font = ('ariel',12,'bold'))
    label1 = Label(frame1, text="Supplier Name : ")
    label1.config(font = ('ariel',12,'bold'))
    label2 = Label(frame1, text="Address : ")
    label2.config(font = ('ariel',12,'bold'))
    label3 = Label(frame1, text="Contact Number : ")
    label3.config(font = ('ariel',12,'bold'))
    label4 = Label(frame1, text="Supply Item : ")
    label4.config(font = ('ariel',12,'bold'))
    label5 = Label(frame1, text="Price/Per : ")
    label5.config(font = ('ariel',12,'bold'))


    entryid = Text(frame1,width=30,height=1,state=DISABLED)
    entryname = Text(frame1,width=30,height=1,state=DISABLED)
    entryaddress = Text(frame1,width=30,height=1,state=DISABLED)
    entrynumber = Text(frame1,width=30,height=1,state=DISABLED)
    entryitem = Text(frame1,width=30,height=1,state=DISABLED)
    entryprice = Text(frame1,width=30,height=1,state=DISABLED)

    label0.grid(row=0,column=0,sticky=E)
    label1.grid(row=1, column=0,sticky=E)
    label2.grid(row=2, column=0,sticky=E)
    label3.grid(row=3, column=0,sticky=E)
    label4.grid(row=4, column=0,sticky=E)
    label5.grid(row=5, column=0,sticky=E)

    entryid.grid(row=0, column=1,padx=10,pady=10)
    entryname.grid(row=1, column=1, padx=10,pady=10)
    entryaddress.grid(row=2, column=1, padx=10,pady=10)
    entrynumber.grid(row=3, column=1, padx=10,pady=10)
    entryitem.grid(row=4, column=1, padx=10,pady=10)
    entryprice.grid(row=5, column=1, padx=10,pady=10)
    frame1.pack()

    Sup1.geometry("600x600+50+50")
    Sup1.mainloop()

if __name__=="__main__":
    sup_find()
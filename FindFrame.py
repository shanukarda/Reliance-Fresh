from tkinter import *
class Find_field:
    def __init__(self,FindID,id_name=""):
        self.findid = FindID
        self.id_name = str(id_name)
        self.findid.title(self.id_name)
        self.suppframe = Frame(self.findid,relief=RAISED,borderwidth=1,pady=10)

        #add supplier id Label
        self.suppid = Label(self.suppframe,text=self.id_name,padx=10,pady=10)
        self.suppid.config(font=('ariel',12,'bold'))
        self.suppid.grid(row=0,column=0)

        #add text entry block
        self.b = StringVar()
        self.findentry = Entry(self.suppframe,textvariable=self.b)
        self.findentry.grid(row=0,column=1,padx=10)

        #add find button
        self.findbutton = Button(self.suppframe,text="Find",padx=30,command=self.find_click)
        self.findbutton.grid(row=0,column=3,padx = 10)


        # add Cancel button
        self.cancelbutton = Button(self.suppframe, text="Cancel", padx=30,command=quit)
        self.cancelbutton.grid(row=0, column=4, padx=10)

        self.suppframe.pack()
        global entryid1
    def find_click(self):
        print("Hello")
def sup_find():

    Sup1 = Tk()
    findsupplier = Find_field(Sup1, "Supplier ID : ")
    frame1=Frame(Sup1,padx=20,pady=100)
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

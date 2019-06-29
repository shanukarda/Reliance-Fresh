from tkinter import *
import mysql.connector


class Add_Purchase:
    def __init__(self,FindID):
        self.findid = FindID
        self.findid.title("Add Purchase")

        self.frame1 = Frame(self.findid, padx=20, pady=50)
        self.mainlabel = Label(self.frame1, text="Add Purchase")
        self.mainlabel.config(font=('ariel', 25, 'bold'))

        self.label0 = Label(self.frame1, text="Purchase Number : ")
        self.label0.config(font=('ariel', 12, 'bold'))
        self.label1 = Label(self.frame1, text="Supplier Name : ")
        self.label1.config(font=('ariel', 12, 'bold'))
        self.label2 = Label(self.frame1, text="Total Billed Amount : ")
        self.label2.config(font=('ariel', 12, 'bold'))
        self.label3 = Label(self.frame1, text="Contact Number : ")
        self.label3.config(font=('ariel', 12, 'bold'))
        self.label4 = Label(self.frame1, text="Item Name: ")
        self.label4.config(font=('ariel', 12, 'bold'))
        self.label5 = Label(self.frame1, text="Price/Per : ")
        self.label5.config(font=('ariel', 12, 'bold'))

        self.entryid = Text(self.frame1, width=30, height=1, state=DISABLED)
        self.entryname = Text(self.frame1, width=30, height=1)
        self.entry_total_billed = Text(self.frame1, width=30, height=1,)
        self.entrynumber = Text(self.frame1, width=30, height=1,)
        self.entryitem = Text(self.frame1, width=30, height=1,)
        self.entryprice = Text(self.frame1, width=30, height=1,)

        self.mainlabel.grid(row=0, column=1)
        self.label0.grid(row=1, column=0, sticky=E)
        self.label1.grid(row=2, column=0, sticky=E)
        self.label2.grid(row=3, column=0, sticky=E)
        self.label3.grid(row=4, column=0, sticky=E)
        self.label4.grid(row=5, column=0, sticky=E)
        self.label5.grid(row=6, column=0, sticky=E)


        self.entryid.grid(row=1,column=1,padx=10,pady=10)
        self.entryname.grid(row=2, column=1, padx=10, pady=10)
        self.entry_total_billed.grid(row=3, column=1, padx=10, pady=10)
        self.entrynumber.grid(row=4, column=1, padx=10, pady=10)
        self.entryitem.grid(row=5, column=1, padx=10, pady=10)
        self.entryprice.grid(row=6, column=1, padx=10, pady=10)


        #add find button
        self.findbutton = Button(self.frame1,text="Save",padx=30,command=self.click_save)
        self.findbutton.grid(row=7,column=1,padx=2,pady=10)


        # add Cancel button
        self.cancelbutton = Button(self.frame1, text="Cancel", padx=30,command=quit)
        self.cancelbutton.grid(row=8, column=1, padx=2, pady=10)
        self.frame1.pack()

    def click_save(self):
        mydb = mysql.connector.connect(host ="localhost", user = "root", passwd ="Shanu0384", database="reliance_fresh")
        mycursor = mydb.cursor()
        self.name = self.entryname.get(1.0,'end-1c')
        self.total_billed = self.entry_total_billed.get(1.0,'end-1c')
        self.number = self.entrynumber.get(1.0,'end-1c')
        self.item = self.entryitem.get(1.0,'end-1c')
        self.price_per_item = self.entryprice.get(1.0,'end-1c')
        mycursor.execute(f"insert into purchase_table values (Default,'{self.name}',{self.total_billed},'{self.number}','{self.item}',{self.price_per_item});")
        mydb.commit()
        mydb.close()
        self.frame2 = Frame(self.findid, padx=10, pady=10)
        self.savelabel = Label(self.frame1, text="Record Successfully Saved")
        self.savelabel.config(fg = "green")
        self.savelabel.grid(row=9, column=1, padx=2, pady=10)
        self.frame2.pack()
        print(f"insert purchase_table values (Default,'{self.name}',{self.total_billed},'{self.number}','{self.item}',{self.price_per_item})")

def run_add_purchase():
    purchase_add1 = Tk()
    Add_Purchase(purchase_add1)
    purchase_add1.geometry("600x600+50+50")
    purchase_add1.mainloop()


if __name__=="__main__":
    run_add_purchase()

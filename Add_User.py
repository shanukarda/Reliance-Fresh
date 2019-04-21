from tkinter import *

class Add_User:
    def __init__(self,FindID):
        self.findid = FindID
        self.findid.title("Add New User")

        self.frame1 = Frame(self.findid, padx=20, pady=20)
        self.mainlabel = Label(self.frame1, text="Add New User")
        self.mainlabel.config(font=('ariel', 18, 'bold'))

        self.label0 = Label(self.frame1, text="Employee ID : ")
        self.label0.config(font=('ariel', 12, 'bold'))
        self.label1 = Label(self.frame1, text="Employee Name : ")
        self.label1.config(font=('ariel', 12, 'bold'))
        self.label2 = Label(self.frame1, text="User ID : ")
        self.label2.config(font=('ariel', 12, 'bold'))
        self.label3 = Label(self.frame1, text="Password : ")
        self.label3.config(font=('ariel', 12, 'bold'))
        self.label4 = Label(self.frame1, text="Designation: ")
        self.label4.config(font=('ariel', 12, 'bold'))

        self.entryid = Text(self.frame1, width=30, height=1, state=DISABLED)
        self.entryname = Text(self.frame1, width=30, height=1, state=DISABLED)
        self.entryaddress = Text(self.frame1, width=30, height=1, state=DISABLED)
        self.entrynumber = Text(self.frame1, width=30, height=1, state=DISABLED)
        self.entryitem = Text(self.frame1, width=30, height=1, state=DISABLED)

        self.mainlabel.grid(row=0, column=1)
        self.label0.grid(row=1, column=0, sticky=E)
        self.label1.grid(row=2, column=0, sticky=E)
        self.label2.grid(row=3, column=0, sticky=E)
        self.label3.grid(row=4, column=0, sticky=E)
        self.label4.grid(row=5, column=0, sticky=E)


        self.entryid.grid(row=1,column=1,padx=10,pady=10)
        self.entryname.grid(row=2, column=1, padx=10, pady=10)
        self.entryaddress.grid(row=3, column=1, padx=10, pady=10)
        self.entrynumber.grid(row=4, column=1, padx=10, pady=10)
        self.entryitem.grid(row=5, column=1, padx=10, pady=10)


        #add find button
        self.findbutton = Button(self.frame1,text="Save",padx=30,command=quit)
        self.findbutton.grid(row=7,column=1,padx=2,pady=10)


        # add Cancel button
        self.cancelbutton = Button(self.frame1, text="Cancel", padx=30,command=quit)
        self.cancelbutton.grid(row=8, column=1, padx=2, pady=10)
        self.frame1.pack()

def run_add_user():
    user_add1 = Tk()
    Add_User(user_add1)
    user_add1.geometry("500x400+50+50")
    user_add1.mainloop()

if __name__=="__main__":
    run_add_user()

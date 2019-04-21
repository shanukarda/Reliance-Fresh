from tkinter import *
class Emp_search:
    def __init__(self,FindID):
        self.findid = FindID
        self.findid.title("Employee Search")
        self.suppframe = Frame(self.findid,relief=RAISED,borderwidth=1,pady=10)

        #add supplier id Label
        self.suppid = Label(self.suppframe,text="Employee ID : ",padx=10,pady=10)
        self.suppid.config(font=('ariel',12,'bold'))
        self.suppid.grid(row=0,column=0)

        #add text entry block
        self.b = StringVar()
        self.findentry = Entry(self.suppframe,textvariable=self.b)
        self.findentry.grid(row=0,column=1,padx=10)

        #add find button
        self.findbutton = Button(self.suppframe,text="Find",padx=30,command=quit)
        self.findbutton.grid(row=0,column=3,padx = 10)


        # add Cancel button
        self.cancelbutton = Button(self.suppframe, text="Cancel", padx=30,command=quit)
        self.cancelbutton.grid(row=0, column=4, padx=10)

        self.suppframe.pack()

        self.frame1 = Frame(self.findid, padx=20, pady=100)
        self.label0 = Label(self.frame1, text="Employee ID : ")
        self.label0.config(font=('ariel', 12, 'bold'))
        self.label1 = Label(self.frame1, text="Employee Name : ")
        self.label1.config(font=('ariel', 12, 'bold'))
        self.label2 = Label(self.frame1, text="Address : ")
        self.label2.config(font=('ariel', 12, 'bold'))
        self.label3 = Label(self.frame1, text="Contact Number : ")
        self.label3.config(font=('ariel', 12, 'bold'))
        self.label4 = Label(self.frame1, text="Designation: ")
        self.label4.config(font=('ariel', 12, 'bold'))
        self.label5 = Label(self.frame1, text="Salary : ")
        self.label5.config(font=('ariel', 12, 'bold'))

        self.entryid = Text(self.frame1, width=30, height=1, state=DISABLED)
        self.entryname = Text(self.frame1, width=30, height=1, state=DISABLED)
        self.entryaddress = Text(self.frame1, width=30, height=1, state=DISABLED)
        self.entrynumber = Text(self.frame1, width=30, height=1, state=DISABLED)
        self.entryitem = Text(self.frame1, width=30, height=1, state=DISABLED)
        self.entryprice = Text(self.frame1, width=30, height=1, state=DISABLED)

        self.label0.grid(row=0, column=0, sticky=E)
        self.label1.grid(row=1, column=0, sticky=E)
        self.label2.grid(row=2, column=0, sticky=E)
        self.label3.grid(row=3, column=0, sticky=E)
        self.label4.grid(row=4, column=0, sticky=E)
        self.label5.grid(row=5, column=0, sticky=E)

        self.entryid.grid(row=0, column=1, padx=10, pady=10)
        self.entryname.grid(row=1, column=1, padx=10, pady=10)
        self.entryaddress.grid(row=2, column=1, padx=10, pady=10)
        self.entrynumber.grid(row=3, column=1, padx=10, pady=10)
        self.entryitem.grid(row=4, column=1, padx=10, pady=10)
        self.entryprice.grid(row=5, column=1, padx=10, pady=10)
        self.frame1.pack()

def run_emp_search():
    emp1 = Tk()
    Emp_search(emp1)
    emp1.geometry("600x600+50+50")
    emp1.mainloop()

if __name__=="__main__":
    run_emp_search()

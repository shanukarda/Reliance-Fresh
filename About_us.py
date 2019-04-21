from tkinter import *

class abount_us:
    def __init__(self,aboutus):
        self.aboutus = aboutus
        self.mainFrame0 = Frame(self.aboutus)
        self.label10 = Label(self.mainFrame0,text="Reliance Fresh Store")
        self.label10.config(font=('ariel',25,'bold'))
        self.label10.grid(sticky=E)
        self.mainFrame0.grid(row=0,column=2,rowspan=3,columnspan=2,padx=140)


        self.mainFrame1 = Frame(self.aboutus)
        self.label0 = Label(self.mainFrame1,text="WITH THIS PROJECT, YOU CAN MAINTAIN INFORMATION ABOUT SALE AND PURCHASE.",padx=2,pady=1)
        self.label0.config(font=('ariel',10,'bold'))
        self.label0.grid(row=5,column=0,sticky=E)

        self.label1 = Label(self.mainFrame1,text="IT PROVIDE EASY WAY TO MAINTAIN INFORMATION.",padx=10)
        self.label1.config(font=('ariel',10,'bold'))
        self.label1.grid(row=6,column=0)

        self.mainFrame1.grid(row=6,column=1,rowspan=5,columnspan=5,pady=20)


        self.mainFrame2 = Frame(self.aboutus)
        self.label2 = Label(self.mainFrame2,text="This project is developed by",padx=80)
        self.label2.config(font=('ariel',10,'bold'))
        self.label2.grid(row=2,column=0)

        self.label3 = Label(self.mainFrame2,text="MANINDER KARDA",padx=10)
        self.label3.config(font=('ariel',10,'bold'))
        self.label3.grid(row=5,column=0)


        self.mainFrame2.grid(row=15,column=1,rowspan=5,columnspan=5,pady=50)

        self.mainFrame3 = Frame(self.aboutus)
        self.label4 = Label(self.mainFrame3,text="FOR MORE INFORMATION CONTACT US ON:",padx=80)
        self.label4.config(font=('ariel',10,'bold'))
        self.label4.grid(row=2,column=0)

        self.label5 = Label(self.mainFrame3,text="Contact No. 95928-50384",padx=10)
        self.label5.config(font=('ariel',10,'bold'))
        self.label5.grid(row=5,column=0)

        self.label6 = Label(self.mainFrame3,text="Copyrigh (c) 2019-2020. All right Reserved.",padx=10)
        self.label6.config(font=('ariel',10,'bold'))
        self.label6.grid(row=7,column=0)


        self.mainFrame3.grid(row=40,column=1,rowspan=5,columnspan=5,pady=20)

def run_about_us():
    aboutus1 = Tk()
    abount_us(aboutus1)
    aboutus1.geometry("600x400+100+50")
    aboutus1.mainloop()

if __name__=="__main__":
    run_about_us()
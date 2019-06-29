from tkinter import *
from Welcome_Window import *
import mysql.connector

def SignIn():
    name = entry1.get()
    password = entry2.get()
    if name == "Shanu" and password == "Shanu0384":
        mainWindow.destroy()
        mydb = mysql.connector.connect(host ="localhost", user = "root", passwd ="Shanu0384")
        mycursor = mydb.cursor()
        mycursor.execute('DROP DATABASE IF EXISTS reliance_fresh;')
        mycursor.execute("create database reliance_fresh;")
        mycursor.execute('DROP TABLE IF EXISTS purchase_table;')
        mycursor.execute("create table purchase_table(Purchase_Number int(5) not null auto_increment,Supplier_Name varchar(50) not null, Total_Billed_Amount float(10) not null, Contact_Number varchar(10) not null, Item_name varchar(50), Price_per_item float(10), primary key(Purchase_Number));")
        mydb.commit()
        mydb.close()
        run1()
    else:
        mainFrame3 = Frame(mainWindow)
        WrongPass = Label(mainFrame3, text="Wrong User Name or Password.", padx=10, pady=5, fg="red")
        WrongPass.grid(row=0, column=1)
        mainFrame3.grid(row=80, column=1, rowspan=20, columnspan=20)


mainWindow = Tk()

mainFrame0 = Frame(mainWindow)
label10 = Label(mainFrame0, text="Reliance Fresh Store")
label10.config(font=('ariel', 25, 'bold'))
label10.grid(sticky=E)
mainFrame0.grid(row=0, column=2, rowspan=3, columnspan=2, padx=90)

mainFrame1 = Frame(mainWindow)
label0 = Label(mainFrame1, text="Name :", padx=10, pady=10)
label0.config(font=('ariel', 10, 'bold'))
label1 = Label(mainFrame1, text="Password :", padx=10)
label1.config(font=('ariel', 10, 'bold'))
entry1 = Entry(mainFrame1)
entry2 = Entry(mainFrame1, show="*")
label0.grid(row=0, column=0, sticky=E)
entry1.grid(row=0, column=2)
label1.grid(row=1, column=0)
entry2.grid(row=1, column=2)
mainFrame1.grid(row=6, column=1, rowspan=5, columnspan=5, pady=20)

mainFrame2 = Frame(mainWindow)
signin = Button(mainFrame2, text="Sign In", padx=30, command=SignIn)
Cancel1 = Button(mainFrame2, text="Cancel", padx=30, command=mainWindow.quit)
signin.grid(row=0, column=0, padx=10)
Cancel1.grid(row=0, column=1, padx=10)
mainFrame2.grid(row=35, column=1, rowspan=20, columnspan=10)

name = entry1.get()
password = entry2.get()

mainWindow.geometry("500x300+500+50")
mainWindow.mainloop()

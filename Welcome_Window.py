from tkinter import *
from About_us import *
from Find_Supplier import *
from Sale_Search import *
from Purchase_Search import *
from Employee_Search import *
from Add_sale import *
from Add_Emp import *
from Add_Supplier import *
from Add_User import *
from Add_Purchase import *
from Modify_sale import *
from Modify_Purchase import *
from Modify_Supplier import *
from Modify_Emp import *
from Delete_Sale import *
from Delete_Purchase import *
from Supplier_delete import *
from Delete_Emp import *
from Modify_User import *
from Delete_User import *
class Welcomescr:
    def __init__(self,mainscr):
        self.mainscr=mainscr
        self.mainscr.title("Wecome Screen")
        self.welcomeframe=Frame(self.mainscr,bg='black',relief=RAISED,borderwidth=20)
        self.welcomeframe.pack(fill=BOTH,expand=1)
        self.welcomelabel=Label(self.mainscr,text="Welcome to Reliance Fresh",bg="black",fg="blue")
        self.welcomelabel.config(font=('ariel', 25, 'bold'))
        self.welcomelabel.place(anchor=N,x=400,y=200,bordermode=OUTSIDE)
        #menu
        self.Main_menu=Menu()
        self.mainscr.config(menu=self.Main_menu)
        #Master Menu
        self.Master_menu = Menu(self.Main_menu)
        self.Main_menu.add_cascade(label="Master",menu=self.Master_menu)

        # Sales Menu
        self.Sales_menu = Menu(self.Master_menu)
        self.Master_menu.add_cascade(label="Sales", menu=self.Sales_menu)
        self.Sales_menu.add_command(label="Add Sale", command=run_add_sale)
        self.Sales_menu.add_command(label="Modify Sale", command=run_modify_sale)
        self.Sales_menu.add_command(label="Delete Sale", command=run_delete_sale)

        # Purchase Menu
        self.Purchase_menu = Menu(self.Master_menu)
        self.Master_menu.add_cascade(label="Purchase",menu=self.Purchase_menu)
        self.Purchase_menu.add_command(label="Add Purchase", command=run_add_purchase)
        self.Purchase_menu.add_command(label="Modify Purchase", command=run_modify_purchase)
        self.Purchase_menu.add_command(label="Delete Purchase", command=run_delete_purchase)

        # Supplier Menu
        self.Supplier_menu = Menu(self.Master_menu)
        self.Master_menu.add_cascade(label="Supplier", menu=self.Supplier_menu)
        self.Supplier_menu.add_command(label="Add Supplier", command=run_add_supplier)
        self.Supplier_menu.add_command(label="Modify Supplier", command=run_modify_supplier)
        self.Supplier_menu.add_command(label="Delete Supplier", command=run_delete_supplier)

        # Employee Menu
        self.Emp_menu = Menu(self.Master_menu)
        self.Master_menu.add_cascade(label="Employee", menu=self.Emp_menu)
        self.Emp_menu.add_command(label="Add Employee", command=run_add_emp)
        self.Emp_menu.add_command(label="Modify Employee", command=run_modify_emp)
        self.Emp_menu.add_command(label="Delete Employee", command=run_delete_emp)

        # User Menu
        self.User_menu = Menu(self.Master_menu)
        self.Master_menu.add_cascade(label="Users", menu=self.User_menu)
        self.User_menu.add_command(label="Add User", command=run_add_user)
        self.User_menu.add_command(label="Modify User", command=run_modify_user)
        self.User_menu.add_command(label="Delete User", command=run_delete_user)

        #Quit
        self.Quit_menu = Menu(self.Master_menu)
        self.Master_menu.add_command(label="Quit", command=quit)

        #adding Search menu list
        self.Search_menu = Menu(self.Main_menu)
        self.Main_menu.add_cascade(label="Search", menu=self.Search_menu)
        self.Search_menu.add_command(label="Purchase Search", command=run_purchase_search)
        self.Search_menu.add_command(label="Employee Search", command=run_emp_search)
        self.Search_menu.add_command(label="Sales Search", command=run_sale_search)
        self.Search_menu.add_command(label="Supplier Search", command=sup_find)

        # adding Report menu list
        self.Report_menu = Menu(self.Main_menu)
        self.Main_menu.add_cascade(label="Report", menu=self.Report_menu)
        self.Report_menu.add_command(label="Purchase Report", command=quit)
        self.Report_menu.add_command(label="Sales Report", command=quit)
        self.Report_menu.add_command(label="Stock Report", command=quit)

        # adding About Us
        self.Help_menu = Menu(self.Main_menu)
        self.Main_menu.add_cascade(label="Help", menu=self.Help_menu)
        self.Help_menu.add_command(label="About Us", command=run_about_us)

def run1():
    WelcomeWindow = Tk()
    Welcomescr(WelcomeWindow)
    WelcomeWindow.geometry("800x600+30+20")
    WelcomeWindow.mainloop()
if __name__=="__main__":
    run1()
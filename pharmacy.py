# Develop By Rohit Kapuria And Poonam Sakhare
# This Coding is for Pharmacy Management System
# Front-End Coding
# Created in Python3.8

from tkinter import*
import tkinter.messagebox
import os
import random
import time
import tempfile
import Store
    
class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.config(bg="grey")
        self.frame = Frame(self.master, bg="grey")
        self.master.geometry("1350x750+0+0")
        self.master.iconbitmap("xx.ico")
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()


        self.LabelTitle= Label(self.frame, text="Pharmacy Management System",font=('arial',50,'bold'),bg ="grey")
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=60)

        self.Loginframe1 =Frame(self.frame,width=1010,height=300,relief='ridge',bg ="grey")
        self.Loginframe1.grid(row=1,column=0,pady=30)

        self.Loginframe2 =Frame(self.frame,width=1000,height=100,relief='ridge',bg ="grey")
        self.Loginframe2.grid(row=2,column=0,pady=30)

        self.Loginframe3 =Frame(self.frame,width=1000,height=200,relief='ridge',bg ="grey")
        self.Loginframe3.grid(row=3,column=0,pady=20)

        #==========================================================================================================
        self.lblUsername= Label(self.Loginframe1, text="Username",font=('arial',30,'bold'),bd=0,bg ="grey")
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername= Entry(self.Loginframe1, text="Username",font=('arial',30,'bold'),bd=0,
                                textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1)

        self.lblPassword= Label(self.Loginframe1, text="Password",font=('arial',30,'bold'),bd=0,bg ="grey")
        self.lblPassword.grid(row=1,column=0,pady=10)
        self.txtPassword= Entry(self.Loginframe1, text="Password",font=('arial',30,'bold'),bd=0,
                                textvariable=self.Password,show="*")
        self.txtPassword.grid(row=1,column=1, padx=85,pady=20)


        #==========================================================================================================

        self.btnLogin = Button(self.Loginframe2, text="Login",width=17,font=('arial',20,'bold'),bg="grey",
                               command=self.Login_System)
        self.btnLogin.grid(row=0,column=0)

        self.btnReset = Button(self.Loginframe2,text="Reset",width=17,font=('arial',20,'bold'),bg="grey", command=self.Reset)
        self.btnReset.grid(row=0,column=1)

        self.btnExit = Button(self.Loginframe2,text="Exit",width=17,font=('arial',20,'bold'),bg="grey" ,command=self.Exit)
        self.btnExit.grid(row=0,column=2)
        #==========================================================================================================


        self.btnInventory = Button(self.Loginframe3, bg="grey",text="Manager",font=('arial',20,'bold'),
                                      state=DISABLED,command=self.Inventory_window)
        self.btnInventory.grid(row=0,column=0)

        self.btnBilling = Button(self.Loginframe3,bg="grey",text="Billing", font=('arial', 20, 'bold'),
                                   state=DISABLED, command=self.Billing_window)
        self.btnBilling.grid(row=0, column=3)

        self.btnAbout = Button(self.Loginframe3, text="About",bg="grey", width=20, font=('arial', 20, 'bold'),
                               command=self.About_window)
        self.btnAbout.grid(row=3, column=2)



        #==========================================================================================================

    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())

        if (user == str(1234)) and (pas == str(4321)):
            self.btnInventory.config(state = NORMAL)
            self.btnBilling.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System","You have entered an invalid login details")
            self.btnInventory.config(state = DISABLED)
            self.btnBilling.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.btnInventory.config(state = DISABLED)
        self.btnBilling.config(state= DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def Exit(self):
        self.Exit =tkinter.messagebox.askyesno("Pharmacy Management System","Confirm if you want to exit")
        if self.Exit > 0:
            self.master.destroy()
            return

        #==========================================================================================================

    
    def Inventory_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Inventory(self.newWindow)

    def Billing_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Billing(self.newWindow)

    def About_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = About(self.newWindow)
#==========================================Inventory======================================
# Managing Data

class Inventory:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Manager")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="grey")
        self.frame = Frame(self.master, bg="grey")
        self.master.iconbitmap("xx.ico")
        self.master.overrideredirect(1)
        self.frame.pack()
        # ==========================================================================================================

        Date = StringVar()
        Date.set(time.strftime("%d/%m/%Y"))
        DistributorName = StringVar()
        MobileNo = StringVar()
        Medicine = StringVar()
        Amount = StringVar()
        ExpDate = StringVar()
        ReferenceNo = StringVar()
        Payment = StringVar()

        # ========================================Function declared================================================

        def iLogout():
            iLogout = tkinter.messagebox.askyesno("Data Manager", "Confirm if you want to Logout ?")
            if iLogout > 0:
                self.master.destroy()
            else:
                self.newWindow = Toplevel(self.master)
                self.app = Inventory(self.newWindow)
                return

        def iReset():
            ReferenceNo.set("")
            DistributorName.set("")
            Date.set("")
            MobileNo.set("")
            ExpDate.set("")
            Medicine.set("")
            Amount.set("")
            Payment.set("")

            Ref_No()

        def Ref_No():
            x = random.randint(10903, 600873)
            randomReferenceNo = str(x)
            ReferenceNo.set(randomReferenceNo)

        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END," " + ReferenceNo.get() + "\t       " + DistributorName.get() + "\t\t    " + Date.get() + \
                                   "\t\t    " + MobileNo.get() + "\t\t    " + ExpDate.get() \
                                   + "\t\t    " + Medicine.get() + "\t\t    " + Amount.get() + "\t\t" + Payment.get() + "\n")

        # ========================================Database function Registration================================

        def ClearData():
            self.txtReferenceNo.delete(0, END)
            self.txtDistributorName.delete(0, END)
            self.txtDate.delete(0, END)
            self.txtMobileNo.delete(0, END)
            self.txtExpDate.delete(0, END)
            self.txtMedicine.delete(0, END)
            self.txtAmount.delete(0, END)
            self.txtPayment.delete(0, END)

        def add():
            if (len(ReferenceNo.get()) != 0):
                Store.addRegRec(ReferenceNo.get(), DistributorName.get(), Date.get(), \
                                MobileNo.get(), ExpDate.get(), Medicine.get(), Amount.get(), \
                                Payment.get())
                storelist.delete(0, END)
                storelist.insert(END, (ReferenceNo.get(), DistributorName.get(), Date.get(), \
                                       MobileNo.get(), ExpDate.get(), Medicine.get(), Amount.get(), \
                                       Payment.get()))

        def DisplayData():
            storelist.delete(0, END)
            for row in Store.displayData():
                storelist.insert(END, row, str(""))

        def StoreRec(event):
            global sd
            searchDistributor = storelist.curselection()[0]
            sd = storelist.get(searchDistributor)

            self.txtReferenceNo.delete(0, END)
            self.txtReferenceNo.insert(END, sd[1])
            self.txtDistributorName.delete(0, END)
            self.txtDistributorName.insert(END, sd[2])
            self.txtDate.delete(0, END)
            self.txtDate.insert(END, sd[3])
            self.txtMobileNo.delete(0, END)
            self.txtMobileNo.insert(END, sd[4])
            self.txtExpDate.delete(0, END)
            self.txtExpDate.insert(END, sd[5])
            self.txtMedicine.delete(0, END)
            self.txtMedicine.insert(END, sd[6])
            self.txtAmount.delete(0, END)
            self.txtAmount.insert(END, sd[7])
            self.txtPayment.delete(0, END)
            self.txtPayment.insert(END, sd[8])

        def Delete():
            if (len(ReferenceNo.get()) != 0):
                Store.deleteRecord(sd[0])
                ClearData()
                DisplayData()

        def Update():
            if (len(ReferenceNo.get()) != 0):
                Store.deleteRecord(sd[0])
            if (len(ReferenceNo.get()) != 0):
                Store.addRegRec(ReferenceNo.get(), DistributorName.get(), Date.get(), \
                                MobileNo.get(), ExpDate.get(), Medicine.get(), Amount.get(), \
                                Payment.get())
                storelist.delete(0, END)
                storelist.insert(END, (ReferenceNo.get(), DistributorName.get(), Date.get(), \
                                       MobileNo.get(), ExpDate.get(), Medicine.get(), Amount.get(), \
                                       Payment.get()))

        # ========================================Frame=======================================================

        Mainframe = Frame(self.frame, bg="grey")
        Mainframe.grid()

        TitleFrame = Frame(Mainframe, padx=26, relief=RIDGE, bg="grey")
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 59, 'bold'), text="Data Manager", padx=2, bg="grey")
        self.lblTitle.grid()

        # ================================LowerFrame==================================================
        MemberDetailsFrame = LabelFrame(Mainframe, bd=0, pady=5, relief=RIDGE, bg="grey")
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=0, relief=RIDGE, bg="grey")
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=0, bg="grey", font=('arial', 12, 'bold'), text='Add Details',
                                   relief=RIDGE)
        MembersName_F.grid(row=0, column=0)

        Database1 = LabelFrame(FrameDetails, bd=0, font=('arial', 12, 'bold'), relief=RIDGE, bg="grey")
        Database1.grid(row=1, column=0)

        Database = LabelFrame(FrameDetails, bd=0, font=('arial', 12, 'bold'), relief=RIDGE, bg="grey")
        Database.grid(row=2, column=0)

        Databutton = LabelFrame(FrameDetails, bd=10, font=('arial', 12, 'bold'), relief=RIDGE, bg="grey")
        Databutton.grid(row=3, column=0)

        Receipt_ButtonFrame = LabelFrame(MemberDetailsFrame, bd=10, padx=20, width=1000, height=400, relief=RIDGE,
                                         bg="grey")
        Receipt_ButtonFrame.pack(side=RIGHT)
        # ================================LowerFrame==================================================
        self.lblReferenceNo = Label(MembersName_F, font=('arial', 14, 'bold'), text="Reference No", bd=7, bg="grey")
        self.lblReferenceNo.grid(row=0, column=0, sticky=W)
        self.txtReferenceNo = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=ReferenceNo,
                                    state=DISABLED, insertwidth=2)
        self.txtReferenceNo.grid(row=0, column=1)

        self.lblDistributorName = Label(MembersName_F, font=('arial', 14, 'bold'), text="Distributor Name", bd=7,
                                        bg="grey")
        self.lblDistributorName.grid(row=1, column=0, sticky=W)
        self.txtDistributorName = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=DistributorName,
                                        insertwidth=2)
        self.txtDistributorName.grid(row=1, column=1)

        self.lblExpDate = Label(MembersName_F, font=('arial', 14, 'bold'), text="Exp.Date", bd=7, bg="grey")
        self.lblExpDate.grid(row=3, column=0, sticky=W)
        self.txtExpDate = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=ExpDate,
                                insertwidth=2)
        self.txtExpDate.grid(row=3, column=1)

        self.lblMobileNo = Label(MembersName_F, font=('arial', 14, 'bold'), text="Mobile No.", bd=7, bg="grey")
        self.lblMobileNo.grid(row=4, column=0, sticky=W)
        self.txtMobileNo = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=MobileNo, insertwidth=2)
        self.txtMobileNo.grid(row=4, column=1)

        self.lblDate = Label(MembersName_F, font=('arial', 14, 'bold'), text="Date", bd=7, bg="grey")
        self.lblDate.grid(row=5, column=0, sticky=W)
        self.txtDate = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=Date, insertwidth=2)
        self.txtDate.grid(row=5, column=1)

        self.lblMedicine = Label(MembersName_F, text="Medicine's", font=('arial', 14, 'bold'), bd=7, bg="grey")
        self.lblMedicine.grid(row=6, column=0, sticky=W)
        self.txtMedicine = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Medicine, bd=7, insertwidth=2)
        self.txtMedicine.grid(row=6, column=1)

        self.lblAmount = Label(MembersName_F, text="Amount", font=('arial', 14, 'bold'), bd=7,
                               bg="grey")
        self.lblAmount.grid(row=7, column=0, sticky=W)
        self.txtAmount = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Amount, bd=7,
                               insertwidth=2)
        self.txtAmount.grid(row=7, column=1)

        self.lblPayment = Label(MembersName_F, text="Payment", font=('arial', 14, 'bold'), bd=7,
                                bg="grey")
        self.lblPayment.grid(row=9, column=0, sticky=W)
        self.txtPayment = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Payment, bd=7,
                                insertwidth=2)
        self.txtPayment.grid(row=9, column=1)

        # ======================================================WidgetReceipt===========================================================
        self.lblLabel = Label(Receipt_ButtonFrame, font=('arial', 10, 'bold'), bg="grey", pady=10,
                              text="Ref\t Distributor\t  Date\t\t Mobile No.\t Exp.Date\t Medicines\t Amt\t Payment  ",
                              bd=7)
        self.lblLabel.grid(row=0, column=0, columnspan=4)

        self.txtReceipt = Text(Receipt_ButtonFrame, width=112, height=18, font=('arial', 10, 'bold'))
        self.txtReceipt.grid(row=1, column=0, columnspan=4)

        # =====================widget2========================================

        scrollbar = Scrollbar(Database1)
        scrollbar.grid(row=0, column=1, sticky="ns")

        storelist = Listbox(Database1, width=50, height=3, font=("arial", 12, "bold"),
                            yscrollcommand=scrollbar.set)
        storelist.bind("<<ListboxSelect>>", StoreRec)
        storelist.grid(row=0, column=0)
        scrollbar.config(command=storelist.yview)

        # ===============================================Buttons================================================================
        self.btnReceipt = Button(Receipt_ButtonFrame, bg="grey", bd=0, font=('arial', 16, 'bold'), width=10,
                                 text="Receipt", command=Receipt).grid(row=2, column=0)
        self.btnReset = Button(Receipt_ButtonFrame, bg="grey", bd=0, font=('arial', 16, 'bold'), width=10, text="Reset",
                               command=iReset).grid(row=2, column=1)
        self.btnLogout = Button(Receipt_ButtonFrame, bg="grey", bd=0, font=('arial', 16, 'bold'), width=10, text="Logout",
                              command=iLogout).grid(row=2, column=2)
        # =================================================Buttons===============================================
        self.btnSave = Button(Databutton, bg="grey", bd=0, font=('arial', 16, 'bold'), width=10, text="Save",
                              command=add).grid(row=0, column=0)
        self.btnUpdate = Button(Databutton, bg="grey", bd=0, font=('arial', 16, 'bold'), width=10, text="Update",
                                command=Update).grid(row=0, column=1)
        self.btnDelete = Button(Databutton, bg="grey", bd=0, font=('arial', 16, 'bold'), width=10, text="Delete",
                                command=Delete).grid(row=1, column=0)
        self.btnDisplay = Button(Databutton, bg="grey", bd=0, font=('arial', 16, 'bold'), width=10, text="Display",
                                 command=DisplayData).grid(row=1, column=1)
        # ==========================================================================================================================
# Creating Bills

class Billing:
    def __init__(self, master):
        self.master = master
        self.master.title("Billing")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="grey")
        self.frame = Frame(self.master, bg="grey")
        self.master.iconbitmap("xx.ico")
        self.master.overrideredirect(1)
        self.frame.pack()
        # ==========================================================================================================

        iDate = StringVar()
        CustomerName = StringVar()
        Medicine = StringVar()
        Amount = StringVar()
        ReferenceNo = StringVar()
        MPayment = StringVar()
        Total = StringVar()

        # ========================================Function declared================================================
        def iPrint():
            q = self.txtReceipt.get("1.0", "end-1c")
            filename = tempfile.mktemp(".txt")
            open(filename, "w").write(q)
            os.startfile(filename, "print")


        def jLogout():
            jLogout = tkinter.messagebox.askyesno("Billing", "Confirm if you want to Logout ?")
            if jLogout > 0:
                self.master.destroy()
            else:
                self.newWindow = Toplevel(self.master)
                self.app = Billing(self.newWindow)
                return

        def iReset():
            ReferenceNo.set("")
            CustomerName.set("")
            iDate.set("")
            Medicine.set("")
            Amount.set("")
            MPayment.set("")
            Total.set("")

            Ref_No()

        def Ref_No():
            x = random.randint(10903, 600873)
            randomReferenceNo = str(x)
            ReferenceNo.set(randomReferenceNo)

        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END,"===============Pharmacy Bill=================""\n"" INV No "+ ReferenceNo.get()\
                                   + "\t\t""Customer Name " + CustomerName.get() + "\n\n"" Date " + iDate.get() + \
                                   "\t\t\t""Payment Type " + MPayment.get() + "\n\n\t\t""Total " + Total.get() +"\n")

        def RefNo():
            x = random.randint(10903, 600873)
            randomReferenceNo = str(x)
            ReferenceNo.set(randomReferenceNo)

        def Add():
            RefNo()
            self.txtReceipt.insert(END,"\n\t"+ Medicine.get() + "\t\t\t\t" + Amount.get() +"\n")

        # ========================================Database function Registration================================

        def DisplayData():
            storelist.delete(0, END)
            for row in Store.displayData1():
                storelist.insert(END, row, str(""))

        def StoreRec(event):
            global sd
            searchDistributorName = storelist.curselection()[0]
            sd = storelist.get(searchDistributorName)

            self.txtReferenceNo.delete(0, END)
            self.txtReferenceNo.insert(END, sd[1])
            self.txtDistributorName.delete(0, END)
            self.txtDistributorName.insert(END, sd[2])
            self.txtDate.delete(0, END)
            self.txtDate.insert(END, sd[3])
            self.txtMobileNo.delete(0, END)
            self.txtMobileNo.insert(END, sd[4])
            self.txtExpDate.delete(0, END)
            self.txtExpDate.insert(END, sd[5])
            self.txtMedicine.delete(0, END)
            self.txtMedicine.insert(END, sd[6])
            self.txtAmount.delete(0, END)
            self.txtAmount.insert(END, sd[7])
            self.txtPayment.delete(0, END)
            self.txtPayment.insert(END, sd[8])



        # ========================================Frame=======================================================

        Mainframe = Frame(self.frame, bg="grey")
        Mainframe.grid()

        TitleFrame = Frame(Mainframe, padx=26, relief=RIDGE, bg="grey")
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 59, 'bold'), text="Billing", padx=2, bg="grey")
        self.lblTitle.grid()

        # ================================LowerFrame==================================================
        MemberDetailsFrame = LabelFrame(Mainframe, bd=0, pady=5, relief=RIDGE, bg="grey")
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=0, relief=RIDGE, bg="grey")
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=0, bg="grey", font=('arial', 12, 'bold'), text='Add Details',
                                   relief=RIDGE)
        MembersName_F.grid(row=0, column=0)

        Database1 = LabelFrame(FrameDetails, bd=0, font=('arial', 12, 'bold'), relief=RIDGE, bg="grey")
        Database1.grid(row=1, column=0)

        Database = LabelFrame(FrameDetails, bd=0, font=('arial', 12, 'bold'), relief=RIDGE, bg="grey")
        Database.grid(row=2, column=0)

        Databutton = LabelFrame(FrameDetails, bd=10, font=('arial', 12, 'bold'), relief=RIDGE, bg="grey")
        Databutton.grid(row=3, column=0)

        Receipt_ButtonFrame = LabelFrame(MemberDetailsFrame, bd=10, padx=2, width=100, height=400, relief=RIDGE,
                                         bg="grey")
        Receipt_ButtonFrame.pack(side=RIGHT)
        # ================================LowerFrame==================================================
        self.lblReferenceNo = Label(MembersName_F, font=('arial', 14, 'bold'), text="Reference No", bd=7, bg="grey")
        self.lblReferenceNo.grid(row=0, column=0, sticky=W)
        self.txtReferenceNo = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=ReferenceNo,
                                    state=DISABLED, insertwidth=2)
        self.txtReferenceNo.grid(row=0, column=1)
#==========================trju+++++++++++++++++++++++++++++++++++
        self.lblDistributorName = Label(MembersName_F)
        self.txtDistributorName = Entry(MembersName_F,state=DISABLED, insertwidth=2)

        self.lblMobileNo = Label(MembersName_F)
        self.txtMobileNo = Entry(MembersName_F, state=DISABLED, insertwidth=2)

        self.lblExpDate = Label(MembersName_F)
        self.txtExpDate = Entry(MembersName_F, state=DISABLED, insertwidth=2)

        self.lblPayment = Label(MembersName_F)
        self.txtPayment = Entry(MembersName_F, state=DISABLED, insertwidth=2)

        self.lblDate = Label(MembersName_F)
        self.txtDate = Entry(MembersName_F, state=DISABLED, insertwidth=2)
#========================================================================================

        self.lblCustomerName = Label(MembersName_F, font=('arial', 14, 'bold'), text="Customer Name", bd=7, bg="grey")
        self.lblCustomerName.grid(row=1, column=0, sticky=W)
        self.txtCustomerName = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=CustomerName,
                                  insertwidth=2)
        self.txtCustomerName.grid(row=1, column=1)



        self.lbliDate = Label(MembersName_F, font=('arial', 14, 'bold'), text="Date", bd=7, bg="grey")
        self.lbliDate.grid(row=5, column=0, sticky=W)
        self.txtiDate = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=iDate, insertwidth=2)
        self.txtiDate.grid(row=5, column=1)

        self.lblMedicine = Label(MembersName_F, text="Medicine's", font=('arial', 14, 'bold'), bd=7, bg="grey")
        self.lblMedicine.grid(row=6, column=0, sticky=W)
        self.txtMedicine = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Medicine, bd=7, insertwidth=2)
        self.txtMedicine.grid(row=6, column=1)

        self.lblAmount = Label(MembersName_F, text="Amount", font=('arial', 14, 'bold'), bd=7,
                               bg="grey")
        self.lblAmount.grid(row=7, column=0, sticky=W)
        self.txtAmount = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Amount, bd=7,
                               insertwidth=2)
        self.txtAmount.grid(row=7, column=1)


        self.lblMPayment = Label(MembersName_F, text="Payment", font=('arial', 14, 'bold'), bd=7,
                                        bg="grey")
        self.lblMPayment.grid(row=8, column=0, sticky=W)
        self.txtMPayment = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=MPayment, bd=7,
                                        insertwidth=2)
        self.txtMPayment.grid(row=8, column=1)

        self.lblTotal = Label(MembersName_F, text="Total", font=('arial', 14, 'bold'), bd=7,
                                 bg="grey")
        self.lblTotal.grid(row=9, column=0, sticky=W)
        self.txtTotal = Entry(MembersName_F, font=('arial', 14, 'bold'), textvariable=Total, bd=7,
                                 insertwidth=2)
        self.txtTotal.grid(row=9, column=1)

        # ======================================================WidgetReceipt===========================================================
        self.lblLabel = Label(Receipt_ButtonFrame, font=('arial', 10, 'bold'), bg="grey", pady=10,
                              bd=7)
        self.lblLabel.grid(row=0, column=0, columnspan=2)

        self.txtReceipt = Text(Receipt_ButtonFrame, width=50, height=30, font=('arial', 10, 'bold'))
        self.txtReceipt.grid(row=1, column=0, columnspan=4)



        #=====================widget2========================================

        scrollbar = Scrollbar(Database1)
        scrollbar.grid(row=0, column=1, sticky="ns")

        storelist = Listbox(Database1, width=50, height=3, font=("arial", 12, "bold"),
                              yscrollcommand=scrollbar.set)
        storelist.bind("<<ListboxSelect>>", StoreRec)
        storelist.grid(row=0, column=0)
        scrollbar.config(command=storelist.yview)


        # ===============================================Buttons================================================================
        self.btnReceipt = Button(Receipt_ButtonFrame, bg="grey", bd=0, font=('arial', 16, 'bold'), width=10,
                                 text="Receipt", command=Receipt).grid(row=2, column=0)

        self.btnReset = Button(Receipt_ButtonFrame, bg="grey", bd=0, font=('arial', 16, 'bold'), width=10, text="Reset",
                               command=iReset).grid(row=2, column=1)

        self.btnCalculator = Button(Receipt_ButtonFrame, bg="grey",bd="0", font=('arial', 16, 'bold'), width=13,
                                 text="Calculator", command=self.cal_window).grid(row=2, column=2)

        self.btnLogout = Button(Receipt_ButtonFrame, bg="grey", bd=0, font=('arial', 16, 'bold'), width=10, text="Logout",
                              command=jLogout).grid(row=2, column=3)
        # =================================================Buttons===============================================
        self.btnDisplay = Button(Databutton, bg="grey", bd=0, font=('arial', 16, 'bold'), width=10, text="Display",
                                 command=DisplayData).grid(row=1, column=1)
        self.btnPrint = Button(Databutton,bg="grey", bd=0, font=('arial', 16, 'bold'), width=10, text="Print",
                               command=iPrint).grid(row=1, column=2)
        self.btnAdd = Button(Databutton,bg="grey", bd=0, font=('arial', 16, 'bold'), width=10, text="Add Item",
                             command=Add).grid(row=1, column=3)
        # ==========================================================================================================================
    def cal_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = calc(self.newWindow)

class calc:

    def getandreplace(self):

        """replace x with * and ÷ with /"""
        self.expression = self.e.get()
        self.newtext = self.expression.replace('/', '/')
        self.newtext = self.newtext.replace('x', '*')

    def equals(self):
        """when the equal button is pressed"""
        self.getandreplace()
        try:
            # evaluate the expression using the eval function
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def squareroot(self):
        """squareroot method"""
        self.getandreplace()
        try:
            # evaluate the expression using the eval function
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.sqrtval = math.sqrt(self.value)
            self.e.delete(0, END)
            self.e.insert(0, self.sqrtval)

    def square(self):
        """square method"""
        self.getandreplace()
        try:
            # evaluate the expression using the eval function
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.sqval = math.pow(self.value, 2)
            self.e.delete(0, END)
            self.e.insert(0, self.sqval)

    def clearall(self):
        """when clear button is pressed,clears the text input area"""
        self.e.delete(0, END)

    def clear1(self):
        self.txt = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def action(self, argi):
        """pressed button's value is inserted into the end of the text area"""
        self.e.insert(END, argi)

    def __init__(self, master):
        """Constructor method"""
        master.title('Calculator')
        master.geometry("270x250+0+0")
        master.resizable(0, 0)
        self.e = Entry(master)
        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        master.iconbitmap("xx.ico")
        self.e.focus_set()  # Sets focus on the input text area

        # Generating Buttons
        Button(master, text="=", width=11, height=3, fg="black",
               bg="grey", command=lambda: self.equals()).grid(
            row=4, column=4, columnspan=2)

        Button(master, text='AC', width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.clearall()).grid(row=1, column=4)

        Button(master, text='C', width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.clear1()).grid(row=1, column=5)

        Button(master, text="+", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('+')).grid(row=4, column=3)

        Button(master, text="x", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('x')).grid(row=2, column=3)

        Button(master, text="-", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('-')).grid(row=3, column=3)

        Button(master, text="÷", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('/')).grid(row=1, column=3)

        Button(master, text="%", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('%')).grid(row=4, column=2)

        Button(master, text="7", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('7')).grid(row=1, column=0)

        Button(master, text="8", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action(8)).grid(row=1, column=1)

        Button(master, text="9", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action(9)).grid(row=1, column=2)

        Button(master, text="4", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action(4)).grid(row=2, column=0)

        Button(master, text="5", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action(5)).grid(row=2, column=1)

        Button(master, text="6", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action(6)).grid(row=2, column=2)

        Button(master, text="1", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action(1)).grid(row=3, column=0)

        Button(master, text="2", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action(2)).grid(row=3, column=1)

        Button(master, text="3", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action(3)).grid(row=3, column=2)

        Button(master, text="0", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action(0)).grid(row=4, column=0)

        Button(master, text=".", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('.')).grid(row=4, column=1)

        Button(master, text="(", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action('(')).grid(row=2, column=4)

        Button(master, text=")", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.action(')')).grid(row=2, column=5)

        Button(master, text="?", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.squareroot()).grid(row=3, column=4)

        Button(master, text="x²", width=5, height=3,
               fg="black", bg="grey",
               command=lambda: self.square()).grid(row=3, column=5)

class About:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="grey")
        self.frame = Frame(self.master, bg="grey")
        self.master.iconbitmap("xx.ico")
        self.master.overrideredirect(1)
        self.frame.pack()

        Mainframe = Frame(self.frame, bg="grey")
        Mainframe.grid()

        TitleFrame = Frame(Mainframe, padx=26, relief=RIDGE, bg="grey")
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 59, 'bold'), text="About", padx=2, bg="grey")
        self.lblTitle.grid()

        self.lblTitle1 = Label(TitleFrame, font=('arial', 20, 'bold'), text="\n\nThis  Application is created by",
                               padx=2, bg="grey")
        self.lblTitle1.grid()

        self.lblTitle2 = Label(TitleFrame, font=('arial', 20, 'bold'),
                               text="\n\nPoonam Sakhare and Rohit Kapuria\n\nPharmacy Management System ",
                               padx=2, bg="grey")
        self.lblTitle2.grid()

        self.lblTitle3 =Label(TitleFrame,font=('arial',20,'bold'),
                              text="\nVersion 1.1.01\n\nDesktop Application \n\n\n\n",padx=2,bg="grey")
        self.lblTitle3.grid()

        Buttonframe = Frame(Mainframe, width=40, height=10, bg="grey", relief=RIDGE)
        Buttonframe.pack(side=TOP)

        def Back():
            Back = tkinter.messagebox.askyesno("About","Confirm if you want to Back ?")
            if Back > 0:
                self.master.destroy()
            else:
                self.newWindow = Toplevel(self.master)
                self.app = About(self.newWindow)
                return



        self.btnBack = Button(Buttonframe, bg="grey", bd=2, font=('arial', 16, 'bold'), width=10, text="Back",
                                command=Back).grid(row=2, column=3)







if __name__=='__main__':
    root=Tk()
    application = Window1 (root)
    root.mainloop()

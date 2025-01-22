import customtkinter as ctk
from tkinter import ttk
import sqlite3
import time

#__________database for user pass and user name
connection = sqlite3.connect("user_data.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS user_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    password TEXT NOT NULL
    )
""")

connection.commit()
connection.close()
print("created user_data database")

#___________________database for user purchase
connection = sqlite3.connect("user_purchase.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS user_purchase (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    date TEXT NOT NULL,
    Item_action TEXT NOT NULL
)
""")

connection.commit()
connection.close()

print("created user_purchases database")




class app:
    
    
    
    def __init__(self):
        self.root = ctk.CTk()
        
        
        
        self.root.attributes("-fullscreen",True)
        self.root.config(bg="#1971c2")
        self.rootwidth = self.root.winfo_width()
        self.rootheight = self.root.winfo_height()
        
        self.Wigets()
        
        
        
        self.root.bind("<Escape>", lambda event: self.root.destroy())
        self.root.mainloop()
        
        
        
        
        
    def Wigets(self):
        self.root.update_idletasks()
        height = (self.rootheight-40)
        width = (self.rootwidth -120 )/2
        
        
        x = ((self.rootwidth)-width) - 30
        
        
        #first labelframe
        self.frame1 = ctk.CTkFrame(self.root,
                                  width=width,
                                  height=height,
                                  bg_color="#1971c2",
                                  fg_color="#a5d8ff",
                                  corner_radius=50,
                                  border_color="black", 
                                  border_width=2)
        self.frame1.place(x=30,y=20)
        
        self.f1label1 = ctk.CTkLabel(self.frame1,width=width / 10,height=80,text="Login",text_color="black",font=("Arial", 50),fg_color="#a5d8ff",bg_color="#a5d8ff")
        self.f1label1.place(x=(width - (width / 10)) / 2-5,y=50)
        
        self.f1labe2 = ctk.CTkLabel(self.frame1,width=(width / 4 )*3 ,height=80,text="Enter Your Username:",text_color="black",font=("Arial", 30),fg_color="#a5d8ff",bg_color="#a5d8ff")
        self.f1labe2.place(x=(width - (width / 4 )*3) / 2 +17,y=150)
        
        self.f1Entery1 = ctk.CTkEntry(self.frame1,width=width / 2,height=100,fg_color="#4292c7",bg_color="#a5d8ff",corner_radius=25,font=("Arial", 30))
        self.f1Entery1.place(x=(width / 2)/2 + 12,y=250)
        
        self.f1labe3 = ctk.CTkLabel(self.frame1,width=(width / 4 )*3 ,height=80,text="Enter Your Password:",text_color="black",font=("Arial", 30),fg_color="#a5d8ff",bg_color="#a5d8ff")
        self.f1labe3.place(x=(width - (width / 4 )*3) / 2 +17,y=350)
        
        self.f1Entery2 = ctk.CTkEntry(self.frame1,width=width / 2,height=100,fg_color="#4292c7",bg_color="#a5d8ff",corner_radius=25,font=("Arial", 30))
        self.f1Entery2.place(x=(width / 2)/2 + 12,y=450)
        
        self.f1labe4 = ctk.CTkLabel(self.frame1,width=(width / 4 )*3 ,height=80,text="",text_color="black",font=("Arial", 30),fg_color="#a5d8ff",bg_color="#1971c2")
        self.f1labe4.place(x=(width - (width / 4 )*3) / 2 +17,y=550)
        
        self.f1button1 = ctk.CTkButton(self.frame1,width=(width / 3 ),height=80,fg_color="#4292c7",bg_color="#a5d8ff",text="Go!",text_color="black",font=("Arial", 30),border_color="black", border_width=2,command=self.login)
        self.f1button1.place(x=(width - (width / 3)) / 2 + 12,y = 750)
        
        
        
        
        
        
        
        #second labelframe
        self.frame2 = ctk.CTkFrame(self.root,
                                  width=width,
                                  height=height,
                                  bg_color="#1971c2",
                                  fg_color="#a5d8ff",
                                  corner_radius=50,
                                  border_color="black", 
                                  border_width=2)
        self.frame2.place(x=x,y=20)
        
        self.f2label1 = ctk.CTkLabel(self.frame2,width=width / 10,height=80,text="Create Account",text_color="black",font=("Arial", 50),fg_color="#a5d8ff",bg_color="#a5d8ff")
        self.f2label1.place(x=(width / 2)/2 + 36,y=50)
        
        
        self.f2labe2 = ctk.CTkLabel(self.frame2,width=(width / 4 )*3 ,height=80,text="Enter Your Username:",text_color="black",font=("Arial", 30),fg_color="#a5d8ff",bg_color="#a5d8ff")
        self.f2labe2.place(x=(width - (width / 4 )*3) / 2 +17 ,y=150)
        
        self.f2Entery1 = ctk.CTkEntry(self.frame2,width=width / 2,height=100,fg_color="#4292c7",bg_color="#a5d8ff",corner_radius=25,font=("Arial", 30))
        self.f2Entery1.place(x=(width / 2)/2 + 12,y=250)
        
        self.f2labe3 = ctk.CTkLabel(self.frame2,width=(width / 4 )*3 ,height=80,text="Enter Your Password:",text_color="black",font=("Arial", 30),fg_color="#a5d8ff",bg_color="#a5d8ff")
        self.f2labe3.place(x=(width - (width / 4 )*3) / 2 +17,y=350)
        
        self.f2Entery2 = ctk.CTkEntry(self.frame2,width=width / 2,height=100,fg_color="#4292c7",bg_color="#a5d8ff",corner_radius=25,font=("Arial", 30))
        self.f2Entery2.place(x=(width / 2)/2 + 12,y=450)
        
        self.f2labe4 = ctk.CTkLabel(self.frame2,width=(width / 4 )*3 ,height=80,text="",text_color="black",font=("Arial", 30),fg_color="#a5d8ff",bg_color="#a5d8ff")
        self.f2labe4.place(x=(width - (width / 4 )*3) / 2 +17,y=550)
        
        self.f2button1 = ctk.CTkButton(self.frame2,width=(width / 3 ),height=80,fg_color="#4292c7",bg_color="#a5d8ff",text="Create!",text_color="black",font=("Arial", 30),border_color="black", border_width=2,command=self.CreateAcc)
        self.f2button1.place(x=(width - (width / 3)) / 2 + 12,y = 750)
    
    
    
        
        
        
    def CreateAcc(self):
        Entery1 = self.f2Entery1.get().strip()
        Entery2 = self.f2Entery2.get().strip()
        text = ""
        if not Entery1 or not Entery2:
            for i in "Both username and password must be filled!":
                text += i
                self.f2labe4.configure(
                    text=text,
                    text_color="red"
                )
                self.f2labe4.update()
            return
        
        
        with sqlite3.connect("user_data.db") as connection:
            cursor = connection.cursor()
            
            cursor.execute("SELECT user_name FROM user_data WHERE user_name == ? ",
                           (Entery1,))
            test_name = cursor.fetchone()
            
            if test_name:
                for i in "User_name already in use!":
                    text += i
                    time.sleep(0.001)
                    self.f2labe4.configure(
                        text =text,
                        text_color="red"
                    )
                    self.f2labe4.update()
            else :
                cursor.execute("INSERT INTO user_data (user_name, password) VALUES (?,?)", 
                               (Entery1,Entery2))
                connection.commit()
                b = 0
                while True:
                    b += 1
                    text = "Please wait"
                    for i in range(3):
                        time.sleep(0.5)
                        text += "."
                        self.f2labe4.configure(
                            text=text,
                            text_color="#1b9c02"
                        )
                        self.f1labe4.update()
                    if b == 1:
                        text = ""
                        break
                for i in "Done!":
                    text += i
                    time.sleep(0.001)
                    self.f2labe4.configure(
                    text=text,
                    text_color="#1b9c02"
                    )
                    self.f2labe4.update()






    def login(self):
        self.Entery1 = self.f1Entery1.get().strip()
        Entery2 = self.f1Entery2.get().strip()
        text = ""
        if not self.Entery1 or not Entery2:
            for i in "Both username and password must be filled!":
                text += i
                self.f1labe4.configure(
                    text=text,
                    text_color="red"
                )
                self.f1labe4.update()
            return
        
        
        with sqlite3.connect("user_data.db") as connection:
            cursor = connection.cursor()
            
            
            cursor.execute("SELECT user_name FROM user_data WHERE user_name == ? ",
                           (self.Entery1,))
            name = cursor.fetchone()
            
            
            cursor.execute("SELECT password FROM user_data WHERE user_name == ? ",
                           (self.Entery1,))
            password = cursor.fetchone()
            
        if name == None:
            for i in "Username does not exist!":
                text += i
                self.f1labe4.configure(
                    text=text,
                    text_color="red"
                )
                self.f1labe4.update()
            return
        elif password[0] != Entery2 :
            for i in "Incorrect password!":
                text += i
                self.f1labe4.configure(
                    text=text,
                    text_color="red"
                )
                self.f1labe4.update()
            return
        
        else:
            b = 0
            while True:
                b += 1
                text = "Please wait"
                for i in range(3):
                    time.sleep(0.5)
                    text += "."
                    self.f1labe4.configure(
                        text=text,
                        text_color="#1b9c02"
                    )
                    self.f1labe4.update()
                if b == 2:
                    
                    self.destroy_widgets()
                    self.root.update()
                    break
            self.new_window()
            
            
        
    def destroy_widgets(self):
        
        for widget in self.root.winfo_children():
            widget.destroy()
        

        
        
    def new_window(self):
        self.newframe = ctk.CTkFrame(self.root,
                                  width=400,
                                  height=self.rootheight - 60,
                                  bg_color="#1971c2",
                                  fg_color="#a5d8ff",
                                  corner_radius=30,
                                  border_color="black", 
                                  border_width=2)
        self.newframe.place(x=30 ,y=20)
        self.nameLabel = ctk.CTkLabel(self.newframe,text="Welcom",text_color="black",fg_color="#a5d8ff",font=("Arial", 50))
        self.nameLabel.place(x = (self.newframe.winfo_width() / 2) + 110 , y = 60)
        self.nameLabel1 = ctk.CTkLabel(self.newframe,text=self.Entery1,text_color="black",fg_color="#a5d8ff",font=("Arial", 50))
        self.nameLabel1.place(x = (self.newframe.winfo_width() / 2) + 110 , y = 110)
        
        
        self.wellcomframe = ctk.CTkFrame(self.newframe,
                                         width=360,
                                         height=(self.rootheight * 0.7  ),
                                         bg_color="#a5d8ff",
                                         fg_color="#a5d8ff",
                                         corner_radius=30,
                                         border_color="black", 
                                         border_width=2)
        self.wellcomframe.place(x=20 ,y=240)
        
        
        self.newframe2 = ctk.CTkFrame(self.root,
                                  width=self.rootwidth - 490,
                                  height=self.rootheight - 60,
                                  bg_color="#1971c2",
                                  fg_color="#a5d8ff",
                                  corner_radius=30,
                                  border_color="black", 
                                  border_width=2)
        self.newframe2.place(x=460 ,y=20)
        newf2f1_width = (self.rootwidth - 290) / 2 - 30

        self.newf2f1 = ctk.CTkFrame(self.newframe2,
                                  width=newf2f1_width,
                                  height=(self.rootheight - 60) - 40,
                                  bg_color="#a5d8ff",
                                  fg_color="#a5d8ff",
                                  corner_radius=30,
                                  border_color="black", 
                                  border_width=2)
        self.newf2f1.place(x=20 ,y=20)
        self.newf2f2 = ctk.CTkFrame(self.newframe2,
                                  width=(self.rootwidth - 690) / 2 - 30,
                                  height=(self.rootheight - 60) - 40,
                                  bg_color="#a5d8ff",
                                  fg_color="#a5d8ff",
                                  corner_radius=30,
                                  border_color="black", 
                                  border_width=2)
        self.newf2f2.place(x=(self.rootwidth - 290) / 2 + 10 ,y=20)
        
        width_labels=newf2f1_width - 10
        self.labelAmount = ctk.CTkLabel(
            self.newf2f1,width=width_labels,text="Enter Amount:",text_color="black",fg_color="#a5d8ff",font=("Arial", 45)
        )
        self.labelAmount.place(x = 5 , y = 50)
        
        self.EnteryAmount = ctk.CTkEntry(
            self.newf2f1,placeholder_text="Example: 35000",width=(newf2f1_width) / 2,height=80,fg_color="#4292c7",bg_color="#a5d8ff",corner_radius=25,font=("Arial", 28)
        )
        self.EnteryAmount.place(x = (newf2f1_width - (newf2f1_width) / 2)/2, y = 125)
        
        
        self.labelDate = ctk.CTkLabel(
            self.newf2f1,width=width_labels,text="Select Date:",text_color="black",fg_color="#a5d8ff",font=("Arial", 45)
        )
        self.labelDate.place(x = 5 , y = 275)
        
        
        self.combobox_year = ctk.CTkComboBox(
            self.newf2f1,values=[str(year) for year in range(1950, 2026)], width=80,text_color="black",bg_color="#a5d8ff",fg_color="#a5d8ff",command=self.date_picker
        )
        self.combobox_year.set("year")  
        self.combobox_year.place(x = 180, y = 350)
        
        
        months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
        ]

        self.combobox_month = ctk.CTkComboBox(
            self.newf2f1,
            values=months,
            width=80,
            text_color="black",
            bg_color="#a5d8ff",
            fg_color="#a5d8ff",
            command=self.date_picker1  
        )

        self.combobox_month.set("month")  
        self.combobox_month.place(x=305, y=350)

        self.combobox_day = ctk.CTkComboBox(
            self.newf2f1,
            values=[str(day) for day in range(1, 31 + 1)],  
            width=80,
            text_color="black",
            bg_color="#a5d8ff",
            fg_color="#a5d8ff",
            command=self.date_picker2
        )

        self.combobox_day.set("day")  
        self.combobox_day.place(x=430, y=350)




        self.Labelreason = ctk.CTkLabel(
            self.newf2f1,width=width_labels,text="Description:",text_color="black",fg_color="#a5d8ff",font=("Arial", 45)
            )
        
        self.Labelreason.place(x=5,y=450)




        self.Enteryreason = ctk.CTkEntry(
            self.newf2f1,width=(newf2f1_width) / 2,height=80,fg_color="#4292c7",bg_color="#a5d8ff",corner_radius=25,font=("Arial", 28)
            )
        self.Enteryreason.place(x=(newf2f1_width - (newf2f1_width) / 2)/2,y=530)






        

        self.Labelerror = ctk.CTkLabel(self.newf2f1,text="",width=width_labels,text_color="black",fg_color="#a5d8ff",font=("Arial", 35))
        self.Labelerror.place(x=5,y=700)


        












        self.button_add = ctk.CTkButton(self.newf2f1,width=(newf2f1_width) / 2 , height=80 ,text="Add",fg_color="#4292c7",bg_color="#a5d8ff",text_color="black",font=("Arial", 30),border_color="black", border_width=2,command=self.add_function)
        self.button_add.place(x=(newf2f1_width- newf2f1_width / 2)/2,y=self.root.winfo_height() - 200)
        
        
        
        
        self.treeview = ttk.Treeview(self.newf2f2,columns=("Amount", "Description", "Date"), show="headings", height=15)
        
        
        self.treeview.heading("Amount", text="Amount")
        self.treeview.heading("Description", text="Description")
        self.treeview.heading("Date", text="Date")
        
        self.treeview.column("Amount", width=100, anchor='center')
        self.treeview.column("Description", width=200, anchor='center')
        self.treeview.column("Date", width=160, anchor='center')
        
        
        
        with sqlite3.connect("user_purchase.db") as connection:
            cursor = connection.cursor()
            
            cursor.execute("SELECT id FROM user_data WHERE user_name == ? ",
                                (self.Entery1,))

            IdName = cursor.fetchone()
            IdName = IdName[0]
            
            cursor.execute("SELECT amount, item_action, date FROM user_purchase WHERE user_id == ?",
                           (IdName,))
            data = cursor.fetchall()

        for record in data:
            self.treeview.insert("", "end", values=record)

        


        self.treeview.pack(side="left", fill="both", expand=True)
        
       
       
       
       
    
    def add_function(self):
        
        self.Labelerror.configure(text="")
        try:
            print(type(self.EnteryAmount.get()))
            if self.EnteryAmount.get() == "":
                text = ""
                for i in "please enter amount":
                    text+=i
                    self.Labelerror.configure(text=text,text_color="red")
                    self.Labelerror.update()
                return
            elif self.Enteryreason.get() == "":
                text = ""
                for i in "please enter Label":
                    text+=i
                    self.Labelerror.configure(text=text,text_color="red")
                    self.Labelerror.update()
                return
            else:
                Label = str(self.Enteryreason.get())
                Amount = int(self.EnteryAmount.get())
                Name =  str(self.Entery1)
        except ValueError:
            text = ""
            for i in "please enter a valid amount":
                text+=i
                self.Labelerror.configure(text=text,text_color="red")
                self.Labelerror.update()
            return
        
        
        try:
            if self.date and self.date1 and self.date2:
                date =str(self.date) +"-"+ str(self.date1) +"-"+ str(self.date2)
                
                with sqlite3.connect("user_data.db") as connection:
                    cursor = connection.cursor()
                    
                    
                    cursor.execute("SELECT id FROM user_data WHERE user_name == ? ",
                                (Name,))
                    IdName = cursor.fetchone()
                    IdName = IdName[0]
                with sqlite3.connect("user_purchase.db") as connection:
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO user_purchase (user_id,amount,item_action,date) VALUES (?,?,?,?)",
                                   (IdName,Amount,Label,date,))
                self.user_id = IdName
                self.show_data()

                
        except AttributeError:
            text = ""
            for i in "please select date":
                text+=i
                self.Labelerror.configure(text=text,text_color="red")
                self.Labelerror.update()
            return
        
        
        

       
       
       
       
       
       
       
    def show_data(self):
        
        with sqlite3.connect("user_purchase.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT amount, item_action, date FROM user_purchase WHERE user_id == ?",
                           (self.user_id,))
            data = cursor.fetchall()
            while True:
                try: 
                    for i, names in enumerate(data[0]):
                        print(data[0][i])
                    data.remove(data[0])
                except IndexError:
                    break
        
        
        
        
        
        
        
    def date_picker(self, selected_year):
         
        self.date=selected_year
           
    def date_picker1(self, selected_month):
        days_in_month = {
                "January": 31,
                "February": 28,
                "March": 31,
                "April": 30,
                "May": 31,
                "June": 30,
                "July": 31,
                "August": 31,
                "September": 30,
                "October": 31,
                "November": 30,
                "December": 31
            }
        self.days = days_in_month[selected_month]
        
        
        self.combobox_day.configure(values=[str(day) for day in range(1, self.days + 1)])
        self.combobox_day.set("day")
        
        
        self.date1=selected_month
        self.date2=None
        
    def date_picker2(self, selected_day):
    
        self.date2=selected_day

       
app = app()
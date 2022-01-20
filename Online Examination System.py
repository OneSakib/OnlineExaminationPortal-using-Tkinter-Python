import json
import shutil
from tkinter import *
import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
import time
from functools import partial
from tkinter.filedialog import *
import os


class OnlineExaminationPortal(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.geometry('1200x650')
        self.logo = PhotoImage(file='logo.png')
        self.iconphoto(False, self.logo)
        self.filename = PhotoImage(file='background.png')
        self.canvas = Canvas(self, width=1200, height=650)
        self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
        self.canvas.place(x=0, y=0)
        self.LoginPanel()

    def LoginPanel(self):
        self.title("Login Panel")
        self.filename = PhotoImage(file='background.png')
        self.canvas = Canvas(self, width=1200, height=650)
        self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
        self.canvas.place(x=0, y=0)
        self.label = Label(self, text="Online Examination System", font='TimesNewRoman 30 bold italic underline',
                           fg='red',
                           bd=5, bg=None)
        self.label.place(relx=0.3, rely=0.06)
        self.labelsign = Label(self, text='Sign In ', font='TimesNewRoman 25 bold italic ', fg='blue')
        self.labelsign.place(relx=0.45, rely=0.2)
        # Variable Declearion
        self.uservalue = StringVar()
        self.usertype = StringVar()
        self.passvalue = StringVar()
        # Decleration
        self.utype = ttk.Combobox(self, textvariable=self.usertype, values=('Admin', 'Student'),
                                  state='readonly',
                                  justify=CENTER, font='TimesNewRoman 15 bold')
        self.utype.set("Admin")
        self.userlabel = Label(self, text='User Name: ', font='TimesNewRoman 15 bold italic', fg='blue')
        self.userentry = Entry(self, font='TimesNewRoman 15 bold italic', textvariable=self.uservalue, width=19,
                               bd=3)
        self.passlabel = Label(self, text='Password: ', font='TimesNewRoman 15 bold italic', fg='blue')
        self.passentry = Entry(self, font='TimesNewRoman 15 bold italic', textvariable=self.passvalue, width=19,
                               bd=3,
                               show='*')
        self.subbtn = Button(self, text='Login', font='TimesNewRoman 15 bold italic', width=19, bd=3,
                             command=self.login)
        self.exitbtn = Button(self, text='Exit', font='TimesNewRoman 15 bold italic', width=19, bd=3,
                              command=self.destroy)
        self.signupbtn = Button(self, text='SignUp', font='TimesNewRoman 15 bold italic', width=19, bd=3,
                                command=self.signup)
        self.forgetbtn = Button(self, text='Forget Password', font='TimesNewRoman 15 bold italic', width=19, bd=3,
                                command=self.Forget)

        # located the widgets
        self.utype.place(relx=0.4, rely=0.3)
        self.userlabel.place(relx=0.3, rely=0.4)
        self.userentry.place(relx=0.5, rely=0.4)
        self.passlabel.place(relx=0.3, rely=0.46)
        self.passentry.place(relx=0.5, rely=0.46)
        self.subbtn.place(relx=0.6, rely=0.55)
        self.exitbtn.place(relx=0.3, rely=0.55)
        self.signupbtn.place(relx=0.3, rely=0.66)
        self.forgetbtn.place(relx=0.6, rely=0.66)
        self.mainloop()

    def signup(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.title("Sign Up Panel")
        self.filename = PhotoImage(file='background.png')
        self.canvas = Canvas(self, width=1200, height=650)
        self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
        self.canvas.place(x=0, y=0)
        self.label = Label(self, text="Online Examination System", font='TimesNewRoman 30 bold italic underline',
                           fg='red',
                           bd=5, bg=None)
        self.label.place(relx=0.3, rely=0.06)
        self.labelsignup = Label(self, text='Sign Up ', font='TimesNewRoman 25 bold italic ', fg='blue')
        self.labelsignup.place(relx=0.45, rely=0.2)
        # Variable Declearion
        self.uservalue = StringVar()
        self.passvalue = StringVar()
        self.emailvalue = StringVar()
        # Decleration
        self.userlabel = Label(self, text='User Name: ', font='TimesNewRoman 15 bold italic', fg='blue')
        self.userentry = Entry(self, font='TimesNewRoman 15 bold italic', textvariable=self.uservalue, width=19,
                               bd=3)
        self.emaillabel = Label(self, text='Email: ', font='TimesNewRoman 15 bold italic', fg='blue')
        self.emailentry = Entry(self, font='TimesNewRoman 15 bold italic', textvariable=self.emailvalue, width=19,
                                bd=3)
        self.passlabel = Label(self, text='Password: ', font='TimesNewRoman 15 bold italic', fg='blue')
        self.passentry = Entry(self, font='TimesNewRoman 15 bold italic', textvariable=self.passvalue, width=19,
                               bd=3,
                               show='*')
        self.subbtn = Button(self, text='Submit', font='TimesNewRoman 15 bold italic', width=19, bd=3,
                             command=self.signupinner)
        self.exitbtn = Button(self, text='Exit', font='TimesNewRoman 15 bold italic', width=19, bd=3,
                              command=self.exitfun)

        # located the widgets
        self.userlabel.place(relx=0.3, rely=0.4)
        self.userentry.place(relx=0.5, rely=0.4)
        self.emaillabel.place(relx=0.3, rely=0.46)
        self.emailentry.place(relx=0.5, rely=0.46)
        self.passlabel.place(relx=0.3, rely=0.52)
        self.passentry.place(relx=0.5, rely=0.52)
        self.subbtn.place(relx=0.6, rely=0.7)
        self.exitbtn.place(relx=0.3, rely=0.7)
        self.mainloop()

    def signupinner(self):
        if len(self.uservalue.get()) == 0:
            mb.showinfo("Login", 'Please Enter login Name')
        elif len(self.emailvalue.get()) == 0:
            mb.showinfo("Login", 'Please Enter Email Address')
        elif len(self.passvalue.get()) == 0:
            mb.showinfo("Login", 'Please Enter login Password')
        else:
            try:
                with open('login.json', 'r') as outfile:
                    data = json.load(outfile)
                    newdata = {
                        "username": f"{self.uservalue.get()}", "email": f"{self.emailvalue.get()}",
                        "pass": f"{self.passvalue.get()}"
                    }
                    data['userdetail'].append(newdata)
                    with open('login.json', 'w') as w:
                        json.dump(data, w, indent=4)
                mb.showinfo("Sign Up", 'Successfully SignUp')
                for widgets in self.winfo_children():
                    widgets.destroy()
                self.LoginPanel()
            except:
                mb.showerror("Sign Up", 'Not Successfully Sign Up')
                for widgets in self.winfo_children():
                    widgets.destroy()
                self.LoginPanel()

    def exitfun(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.LoginPanel()

    def Forget(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.title("Forget Password")
        self.filename = PhotoImage(file='background.png')
        self.canvas = Canvas(self, width=1200, height=650)
        self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
        self.canvas.place(x=0, y=0)
        self.label = Label(self, text="Online Examination System", font='TimesNewRoman 30 bold italic underline',
                           fg='red',
                           bd=5, bg=None)
        self.label.place(relx=0.3, rely=0.06)
        self.labelsignup = Label(self, text='Forget Password', font='TimesNewRoman 25 bold italic ', fg='blue')
        self.labelsignup.place(relx=0.45, rely=0.2)
        # Variable Declearion
        self.uservalue = StringVar()
        # Decleration
        self.userlabel = Label(self, text='User Name: ', font='TimesNewRoman 15 bold italic', fg='blue')
        self.userentry = Entry(self, font='TimesNewRoman 15 bold italic', textvariable=self.uservalue, width=19,
                               bd=3)
        self.subbtn = Button(self, text='Submit', font='TimesNewRoman 15 bold italic', width=19, bd=3,
                             command=self.forgetinner)
        self.exitbtn = Button(self, text='Exit', font='TimesNewRoman 15 bold italic', width=19, bd=3,
                              command=self.exitfun)
        self.passLabel = Label(self, text='', font='TimesNewRoman 15 bold italic', fg='red')
        # located the widgets
        self.userlabel.place(relx=0.3, rely=0.4)
        self.userentry.place(relx=0.5, rely=0.4)
        self.subbtn.place(relx=0.6, rely=0.5)
        self.exitbtn.place(relx=0.3, rely=0.5)
        self.passLabel.place(relx=0.3, rely=0.7)
        self.mainloop()

    def forgetinner(self):
        if self.uservalue.get() == 0:
            mb.showinfo("Forget", "Please Enter User Name")
        else:
            try:
                with open('login.json', 'r') as fileopen:
                    data = json.load(fileopen)
                    for i in range(len(data['userdetail'])):
                        if self.uservalue.get() == data['userdetail'][i]['username']:
                            self.passLabel.config(text=f"Your Password is: {data['userdetail'][i]['pass']}")
                            mb.showinfo("Forget", "Successfully")
                            break
            except Exception as e:
                mb.showerror("Error", f"Error is : {e}")

    def login(self):
        if len(self.uservalue.get()) == 0:
            mb.showinfo("Login", 'Please Enter login Name')
        elif len(self.passvalue.get()) == 0:
            mb.showinfo("Login", 'Please Enter login Password')
        else:
            if self.usertype.get() == 'Admin':
                try:
                    with open('adminlogin.json', 'r') as fileread:
                        data = json.load(fileread)
                        for i in range(len(data['userdetail'])):
                            if data['userdetail'][i]['username'] == (self.uservalue.get()).strip():
                                if data['userdetail'][i]['pass'] == (self.passvalue.get()).strip():
                                    mb.showinfo("Login", "Successfully Login")
                                    for widgets in self.winfo_children():
                                        widgets.destroy()
                                    self.AdminPanel(self.uservalue.get())
                                    break
                            elif i == (len(data['userdetail']) - 1):
                                mb.showerror("Login", "login Error Your Username and password did not match")
                                for widgets in self.winfo_children():
                                    widgets.destroy()
                                self.LoginPanel()
                except Exception as e:
                    mb.showerror("Error", f"Error is : {e}")
                    mb.showerror("Login", "login Error ")
                    for widgets in self.winfo_children():
                        widgets.destroy()
                    self.LoginPanel()
            else:
                try:
                    with open('login.json', 'r') as fileread:
                        data = json.load(fileread)
                        for i in range(len(data['userdetail'])):
                            if data['userdetail'][i]['username'] == (self.uservalue.get()).strip():
                                if data['userdetail'][i]['pass'] == (self.passvalue.get()).strip():
                                    mb.showinfo("Login", "Successfully Login")
                                    for widgets in self.winfo_children():
                                        widgets.destroy()
                                    self.StudentPanel(self.uservalue.get())
                                    break
                            elif i == (len(data['userdetail']) - 1):
                                mb.showerror("Login", "login Error Your Username and password did not match")
                                for widgets in self.winfo_children():
                                    widgets.destroy()
                                self.LoginPanel()
                except Exception as e:
                    mb.showerror("Error", f"Error is : {e}")
                    for widgets in self.winfo_children():
                        widgets.destroy()
                    self.LoginPanel()

    def StudentPanel(self, username):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.title("Student Panel")
        self.filename = PhotoImage(file='background.png')
        self.canvas = Canvas(self, width=1200, height=650)
        self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
        self.canvas.place(x=0, y=0)
        self.username = username
        self.label = Label(self, text="Online Examination System", font='TimesNewRoman 30 bold italic underline',
                           fg='red', bd=5)
        self.label.place(relx=0.3, rely=0.06)
        self.label = Label(self, text=f"Welcome {self.username}", font='TimesNewRoman 20 bold italic ',
                           fg='blue',
                           bd=5, justify=CENTER)
        self.label.place(relx=0.4, rely=0.2)
        self.exitbtn = Button(self, text='Exit',
                              font='TimesNewRoman 20 bold italic ',
                              fg='white', bg='red',
                              bd=5,
                              justify=CENTER, wraplength=180,
                              command=self.exitfun)
        self.exitbtn.place(relx=0.9, rely=0.9)
        # Decleration
        try:
            with open('paper.json', 'r') as paperfile:
                data = json.load(paperfile)
                count = 0.2
                count2 = 0.3
                for i in range(len(data["Papers"])):
                    if count != 1:
                        Button(self, text=f'{data["Papers"][i]["Name"]}',
                               font='TimesNewRoman 20 bold italic ',
                               fg='blue',
                               bd=5,
                               justify=CENTER, wraplength=180,
                               command=partial(self.examquiz, data["Papers"][i]["filename"])).place(relx=count,
                                                                                                    rely=count2,
                                                                                                    width=220,
                                                                                                    height=110)
                        count += 0.2
                    else:
                        count = 0.2
                        count2 += 0.2

        except Exception as e:
            mb.showerror("Error", f"Error is : {e}")

    def examquiz(self, file):
        self.file = file
        for widgets in self.winfo_children():
            widgets.destroy()
        self.Quiz(self.username, self.file)

    def AdminPanel(self, username):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.title("Admin Panel")
        self.filename = PhotoImage(file='background.png')
        self.canvas = Canvas(self, width=1200, height=650)
        self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
        self.canvas.place(x=0, y=0)
        self.username = username
        self.label = Label(self, text="Online Examination System", font='TimesNewRoman 30 bold italic underline',
                           fg='red',
                           bd=5)
        self.label.place(relx=0.3, rely=0.06)
        self.label = Label(self, text=f"Welcome Admin: {self.username}", font='TimesNewRoman 20 bold italic ',
                           fg='blue',
                           bd=5, justify=CENTER)
        self.label.place(relx=0.4, rely=0.2)
        self.exitbtn = Button(self, text='Exit',
                              font='TimesNewRoman 20 bold italic ',
                              fg='white', bg='red',
                              bd=5,
                              justify=CENTER, wraplength=180,
                              command=self.exitfun)
        self.exitbtn.place(relx=0.9, rely=0.9)
        self.addexam = Button(self, text='Add New Exam',
                              font='TimesNewRoman 20 bold italic ',
                              fg='blue', bg='gray',
                              bd=5,
                              justify=CENTER, wraplength=180, width=13, height=5,
                              command=self.adddexamfun)
        self.editexam = Button(self, text='Edit Exam',
                               font='TimesNewRoman 20 bold italic ',
                               fg='blue', bg='gray',
                               bd=5,
                               justify=CENTER, wraplength=180, width=13, height=5,
                               command=self.editexamfun)
        self.examlist = Button(self, text='Show Exam List',
                               font='TimesNewRoman 20 bold italic ',
                               fg='blue', bg='gray',
                               bd=5,
                               justify=CENTER, wraplength=180, width=13, height=5,
                               command=self.examlistfun)
        self.addexam.place(relx=0.1, rely=0.3)
        self.editexam.place(relx=0.4, rely=0.3)
        self.examlist.place(relx=0.7, rely=0.3)

    def adddexamfun(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.AddExam(self.username)

    def editexamfun(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.EditExam(self.username)

    def examlistfun(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.ListExam(self.username)

    def AddExam(self, username):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.title("Add Exam Panel")
        self.filename = PhotoImage(file='background.png')
        self.canvas = Canvas(self, width=1200, height=650)
        self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
        self.canvas.place(x=0, y=0)
        self.username = username
        self.label = Label(self, text="Online Examination System", font='TimesNewRoman 30 bold italic underline',
                           fg='red',
                           bd=5)
        self.label.place(relx=0.3, rely=0.06)
        self.label = Label(self, text=f"Add New Exam", font='TimesNewRoman 20 bold italic ',
                           fg='blue',
                           bd=5, justify=CENTER)
        self.label.place(relx=0.4, rely=0.2)
        # Variable Declearion
        self.filepath = StringVar()
        self.ExamName = StringVar()
        # Decleration
        self.filepathlabel = Label(self, text='File Path:', font='TimesNewRoman 18 bold italic', fg='blue')
        self.filepathentry = Entry(self, font='TimesNewRoman 15 bold italic', textvariable=self.filepath, width=45,
                                   bd=3, state='readonly')
        self.filebtn = Button(self, text='File Open', font='TimesNewRoman 10 bold italic', command=self.fileopenfun,
                              width=19, bd=3)
        self.examnamelabel = Label(self, text='Exam Name: ', font='TimesNewRoman 18 bold italic', fg='blue')
        self.examnameentry = Entry(self, font='TimesNewRoman 15 bold italic', textvariable=self.ExamName, width=45,
                                   bd=3)
        self.subbtn = Button(self, text='Exam Add', font='TimesNewRoman 15 bold italic', width=19, bd=3,
                             command=self.examadd)

        # located the widgets
        self.filepathlabel.place(relx=0.1, rely=0.4)
        self.filepathentry.place(relx=0.25, rely=0.4)
        self.filebtn.place(relx=0.69, rely=0.4)
        self.examnamelabel.place(relx=0.1, rely=0.55)
        self.examnameentry.place(relx=0.25, rely=0.55)
        self.subbtn.place(relx=0.5, rely=0.65)
        self.exitbtn = Button(self, text='Exit',
                              font='TimesNewRoman 20 bold italic ',
                              fg='white', bg='red',
                              bd=5,
                              justify=CENTER, wraplength=180,
                              command=self.exitadmin)
        self.exitbtn.place(relx=0.9, rely=0.9)

    def exitadmin(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.AdminPanel(self.username)

    def fileopenfun(self):
        self.path = askopenfilename(initialdir='/Desktop', title='Select File Exam File',
                                    filetypes=(('Json Files', '*.json'),))
        self.filepath.set(self.path)
        self.update()

    def examadd(self):
        self.filenames = os.path.basename(self.path)
        self.newfilepath = r'./papers'
        try:
            shutil.copy(self.path, os.path.join(self.newfilepath, self.ExamName.get().replace(" ", "") + ".json"))
        except Exception as e:
            mb.showerror("File Error", f"File Error: {e}")
        try:
            if os.path.exists(self.filepath.get()):
                if len(self.ExamName.get().strip()) != 0:
                    with open('paper.json', 'r') as readfile:
                        self.data = json.load(readfile)
                        self.newdata = {
                            "Name": f"{self.ExamName.get()}",
                            "filename": f"{self.ExamName.get().replace(' ', '') + '.json'}"
                        }
                        self.data['Papers'].append(self.newdata)
                        with open('paper.json', 'w') as writefile:
                            json.dump(self.data, writefile, indent=4)
                        mb.showinfo("File", "File Successfully Add")
                        for widgets in self.winfo_children():
                            widgets.destroy()
                        self.AdminPanel(self.username)
                else:
                    mb.showerror("Error", "Please Enter File Name")
            else:
                mb.showerror("Error", "File is Not find")
        except Exception as e:
            mb.showerror("File Error", f"File Error: {e}")

    def EditExam(self, username):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.title("Edit Exam Panel")
        self.filename = PhotoImage(file='background.png')
        self.canvas = Canvas(self, width=1200, height=650)
        self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
        self.canvas.place(x=0, y=0)
        self.username = username
        self.label = Label(self, text="Online Examination System", font='TimesNewRoman 30 bold italic underline',
                           fg='red',
                           bd=5)
        self.label.place(relx=0.3, rely=0.06)
        self.label = Label(self, text=f"Edit Exam", font='TimesNewRoman 20 bold italic ',
                           fg='blue',
                           bd=5, justify=CENTER)
        self.label.place(relx=0.4, rely=0.2)
        self.removebtn = Button(self, text='Remove Exam',
                                font='TimesNewRoman 20 bold italic ',
                                fg='white', bg='red',
                                bd=5,
                                justify=CENTER, wraplength=180,
                                command=self.removeexam)
        self.removebtn.place(relx=0.8, rely=0.5)
        self.exitbtn = Button(self, text='Exit',
                              font='TimesNewRoman 20 bold italic ',
                              fg='white', bg='red',
                              bd=5,
                              justify=CENTER, wraplength=180,
                              command=self.exitadmin)
        self.exitbtn.place(relx=0.9, rely=0.9)
        self.examlist = Listbox(self, bg='white', fg='blue', font='Helvetica 20 bold', height=10, width=50,
                                highlightcolor='red',
                                highlightthickness=5, relief=RAISED, bd=5, selectbackground='red',
                                selectmode=EXTENDED)
        self.xscroll = Scrollbar(self, orient=VERTICAL)
        self.examlist.config(yscrollcommand=self.xscroll.set)
        self.xscroll.config(command=self.examlist.yview)
        self.xscroll.pack(side=RIGHT, fill=Y)
        try:
            with open('paper.json', 'r') as readfile:
                data = json.load(readfile)
                for i in range(len(data['Papers'])):
                    self.examlist.insert(i, f"{i + 1}:{data['Papers'][i]['Name']}")
        except Exception as e:
            mb.showerror("Error", f"Error is : {e}")
        self.examlist.place(relx=0.1, rely=0.2)
        mainloop()

    def removeexam(self):
        self.currselection = self.examlist.curselection()[0]
        try:
            with open('paper.json', 'r') as readfile:
                data = json.load(readfile)
                print(data['Papers'][self.currselection])
                del data['Papers'][self.currselection]
                with open('paper.json', 'w') as writefile:
                    json.dump(data, writefile, indent=4)
                    mb.showinfo("Edit", "Remove Successfully Exam in the List")
                    self.update()
        except Exception as e:
            mb.showerror("Error", f"File Not Found:{e}")

    def ListExam(self, username):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.title("List of Exam")
        self.filename = PhotoImage(file='background.png')
        self.canvas = Canvas(self, width=1200, height=650)
        self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
        self.canvas.place(x=0, y=0)
        self.username = username
        self.label = Label(self, text="Online Examination System", font='TimesNewRoman 30 bold italic underline',
                           fg='red',
                           bd=5)
        self.label.place(relx=0.3, rely=0.06)
        self.label = Label(self, text=f"Show All Exams", font='TimesNewRoman 20 bold italic ',
                           fg='blue',
                           bd=5, justify=CENTER)
        self.label.place(relx=0.4, rely=0.2)
        self.exitbtn = Button(self, text='Exit',
                              font='TimesNewRoman 20 bold italic ',
                              fg='white', bg='red',
                              bd=5,
                              justify=CENTER, wraplength=180,
                              command=self.exitadmin)
        self.exitbtn.place(relx=0.9, rely=0.9)
        self.examlist = Listbox(self, bg='white', fg='blue', font='Helvetica 20 bold', height=10, width=50,
                                highlightcolor='red',
                                highlightthickness=5, relief=RAISED, bd=5, selectbackground='red',
                                selectmode=EXTENDED)
        self.xscroll = Scrollbar(self, orient=VERTICAL)
        self.examlist.config(yscrollcommand=self.xscroll.set)
        self.xscroll.config(command=self.examlist.yview)
        self.xscroll.pack(side=RIGHT, fill=Y)
        try:
            with open('paper.json', 'r') as readfile:
                data = json.load(readfile)
                for i in range(len(data['Papers'])):
                    self.examlist.insert(i, f"{i + 1}:{data['Papers'][i]['Name']}")
        except Exception as e:
            mb.showerror("Error", f"Error is : {e}")
        self.examlist.place(relx=0.1, rely=0.2)
        mainloop()

    def Quiz(self, username, filename):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.title("Examination Questions")
        self.filename = PhotoImage(file='background.png')
        self.canvas = Canvas(self, width=1200, height=650)
        self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
        self.canvas.place(x=0, y=0)
        self.username = username
        self.filepath = os.path.join('./papers', filename)
        try:
            with open(self.filepath) as f:
                data = json.load(f)
        except Exception as e:
            mb.showerror("Error", f"Error is: {e}")
        self.timelabel = Label(self, font='arial 15 bold', text='00:30:00', fg='gray25', bg='papaya whip')
        self.timelabel.place(relx=0.8, rely=0.1)
        self.questions = (data['questions'])
        self.options = (data['options'])
        self.answer = (data['answers'])
        self.q_no = 0
        self.display_title()
        self.display_questions()
        self.opt_selected = IntVar()
        self.opts = self.radio_button()
        self.display_options()
        self.buttons()
        self.data_size = len(self.questions)
        self.correct = 0
        self.countdown()

    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"Correct {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        mb.showinfo("Result: ", f"{result} \n {correct} \n {wrong}")

    def check_ans(self, q_no):
        if self.opt_selected.get() == self.answer[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no == self.data_size:
            self.submitfun()
        else:
            self.display_questions()
            self.display_options()

    def countdown(self):
        self.times = int(0) * 3600 + int(30) * 60 + int(0)
        while self.times > -1:
            minute, second = (self.times // 60, self.times % 60)
            hour = 0
            if minute > 60:
                hour, minute = (minute // 60, minute % 60)
            if (self.times == 0):
                self.submitfun()
            try:
                self.timelabel.config(text=f"{hour}:{minute}:{second}")
            except:
                break
            self.update()
            time.sleep(1)
            self.times -= 1

    def prev_btn(self):
        if self.q_no > 0:
            if self.check_ans(self.q_no):
                self.correct -= 1
            self.q_no -= 1
            if (False):
                pass
            else:
                self.display_questions()
                self.display_options()

    def submitfun(self):
        self.display_result()
        for widgets in self.winfo_children():
            widgets.destroy()
        self.StudentPanel(self.username)

    def buttons(self):
        prev_button = Button(self, text='Previous', command=self.prev_btn, width=10, bg='blue', fg='white',
                             font=('arial', 16, 'bold'))
        prev_button.place(relx=0.2, rely=0.7)
        next_button = Button(self, text='Next', command=self.next_btn, width=10, bg='blue', fg='white',
                             font=('arial', 16, 'bold'))
        next_button.place(relx=0.5, rely=0.7)
        submit_button = Button(self, text='Submit', command=self.submitfun, width=10, bg='black', fg='white',
                               font='arial 16 bold')
        submit_button.place(relx=0.8, rely=0.7)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in self.options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_questions(self):
        q_no = Label(self, text=self.questions[self.q_no], width=60, font='arial 16 bold', anchor='w')
        q_no.place(x=70, y=100)

    def display_title(self):
        title = Label(self, text='Examination Questions', width=70, bg='green', fg='white', font='arial 20 bold')
        title.place(relx=0, rely=0)

    def radio_button(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(self, text='', variable=self.opt_selected, value=len(q_list) + 1,
                                    font='arial 14 ')
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40

        return q_list


def run():
    splash.destroy()
    OnlineExaminationPortal()


if __name__ == '__main__':
    splash = Tk()
    splash.geometry('600x450')
    splash.title("Online Examination System")
    splash.overrideredirect(True)
    filename = PhotoImage(file='dev.png')
    canvas = Canvas(splash, width=600, height=400)
    imageset = canvas.create_image(50, 140, anchor=NW, image=filename)
    canvas.pack()
    wtitle = Label(splash, text='Dev Bhoomi Group Of Institutions  Saharanpur',
                   font='TimesNewRoman 25 bold italic',
                   fg='red', justify=CENTER,
                   wraplength=700)
    wtitle.place(relx=0.05, rely=0.05)
    wtitle2 = Label(splash, text='Mini Project On Online Examination System',
                    font='TimesNewRoman 15 bold italic',
                    fg='red', justify=CENTER,
                    wraplength=700)
    wtitle2.place(relx=0.15, rely=0.25)
    wtitle3 = Label(splash, text=' Sakib Malik\n MCA 2nd Year',
                    font='TimesNewRoman 15 bold italic',
                    fg='red', justify=CENTER,
                    wraplength=700)
    wtitle3.place(relx=0.7, rely=0.88)
    splash.after(5000, run)
    mainloop()

from tkinter import *
import tkinter.messagebox as tm
import requests

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")

        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()
    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)
        if("OK" ==(requests.get("http://35.200.177.225:8099/uname/pass")).text): #and (password == requests.get("http://35.200.234.5:8090/username/password"):
            root1 = Tk()
            DFrame(root1)
            root1.mainloop()
            #tm.showinfo("Login info", "Welcome")
        else:
            tm.showerror("Login error", "Incorrect username")



class DFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_req = Label(self, text="Requests")

        self.label_apprv = Label(self, text="APprove?")

        self.entry_req = Entry(self)
        self.entry_apprv = Entry(self)

        self.label_req.grid(row=0, sticky=E)
        self.label_apprv.grid(row=1, sticky=E)
        self.entry_req.grid(row=0, column=1)
        self.entry_apprv.grid(row=1, column=1)

        #self.checkbox = Checkbutton(self, text="Keep me logged in")
        #self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Make Request", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()
    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_req.get()
        password = self.entry_apprv.get()
        print(req,apprv)
        # print(username, password)
       # if("OK" ==(requests.get("http://35.200.177.225:8099/uname/pass")).text): #and (password == requests.get("http://35.200.234.5:8090/username/password"):
        #    tm.showinfo("Login info", "Welcome")
        #else:
         #   tm.showerror("Login error", "Incorrect username")


    
root = Tk()
#root1 = Tk()
lf = LoginFrame(root)
#if(x!=1):
#    df= DFrame(root1)
#root.mainloop()

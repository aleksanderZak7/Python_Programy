from tkinter import *
from tkinter import messagebox
import smtplib
import re

class Before_login(Frame):
    trials=0
    def __init__(self,master):
        super(Before_login,self).__init__(master)
        self.my_widgets()
        self.grid()
    
    def my_widgets(self):
        self.main_menu=Menu(self)
        self.sub_menu=Menu(self.main_menu,tearoff=0)
        root.configure(menu=self.main_menu)
        self.main_menu.add_cascade(label='About program',menu=self.sub_menu)
        self.sub_menu.add_command(label='Help',command=self.help_me)
        self.sub_menu.add_command(label='Exit',command=root.destroy)
        
        self.welcome_label=Label(self,width=30,text='Enter your email and password:',font=('Calibri 18 bold',18))
        self.welcome_label.grid(row=0,columnspan=3,pady=10,padx=10)
        
        self.enter_your_email=Label(self,text='Email:',font=('Calibri 18 bold',12)) 
        self.enter_your_email.grid(row=1,sticky=E,pady=5,padx=10)
        
        self.entry_for_email=Entry(self,width=35)
        self.entry_for_email.grid(row=1,column=1,pady=5)
        
        self.enter_your_password=Label(self,text='Password:',font=('Calibri 18 bold',12)) 
        self.enter_your_password.grid(row=2,sticky=E,pady=5,padx=10)
        
        self.entry_for_password=Entry(self,show='*',width=35) 
        self.entry_for_password.grid(row=2,column=1,pady=5)
        
        self.login_button=Button(self,text='Login',font=('Calibri 18 bold',18),bg='black',fg='white',command=self.login) 
        self.login_button.grid(row=3,columnspan=3,pady=10,padx=40)
    
    def help_me(self):
        messagebox.showinfo('Help!',"To send an email you must:\n1)Login to your email by using your true email\nand your true email password for the application:\nhttps://support.google.com/accounts/answer/185833?hl=pl\n2)Fill all of the blanks\n3)Provide a good recipient's email\n4)Click send")
    
    def login(self):
        Before_login.trials+=1
        if self.login_verification(): 
            self.username=str(self.entry_for_email.get())
            self.password=str(self.entry_for_password.get())
            self.server=smtplib.SMTP('smtp.gmail.com:587')
            
            self.server.ehlo
            self.server.starttls()
            self.server.login(self.username,self.password)
            Second_Frame.pack()
            Second_Frame.logout_button.grid()
            First_Frame.pack_forget()
        else:
            if Before_login.trials==3:
                Before_login.trials=0
                messagebox.showinfo('Help message!',"if you entered your real e-mail and you can't log in,\nyou must use the password for the application:\nhttps://support.google.com/accounts/answer/185833?hl=pl")
      
    def login_verification(self):
        your_email=str(self.entry_for_email.get())
        your_password=str(self.entry_for_password.get())
        
        if your_email=='' or your_password=='':
            messagebox.showerror('Login error!',"You can't leave a blank in any column!")
            return False
        else:
            your_true_email=re.compile(r'[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$')
            if not your_true_email.match(your_email):
                messagebox.showerror('Login error!','Enter a valid email!')
                return False
            else:
                try:
                    server=smtplib.SMTP('smtp.gmail.com:587')
                    server.ehlo
                    server.starttls()
                    server.login(your_email,your_password)
                    server.quit()
                    return True
                except:
                    messagebox.showerror('Login error!','Enter a valid password!')
                    return False
                             
class After_login(Frame):
    def __init__(self,master):
        super(After_login,self).__init__(master)
        self.pack(side=TOP,expand=NO,fill=NONE)
        self.my_widgets()
        self.pack_forget()
    
    def my_widgets(self):
        self.logout_button=Button(self,text='logout',bg='black',fg='white',command=self.logout) 
        self.logout_button.grid(row=0,column=3,sticky=E,pady=10,padx=(5,0))
        
        self.new_email=Label(self,width=20,text="Creating new email:",font='Calibri 18 bold') 
        self.new_email.grid(row=0,columnspan=2,pady=10)
        
        self.recipients_email=Label(self,width=20,text="Recipient's email:") 
        self.recipients_email.grid(row=1,sticky=E,pady=5)
        
        self.entry_for_recipients_email=Entry(self) 
        self.entry_for_recipients_email.grid(row=1,column=1,pady=5)
        
        self.email_subject=Label(self,width=20,text="Email subject:")
        self.email_subject.grid(row=2,sticky=E,pady=5)
        
        self.entry_for_email_subject=Entry(self) 
        self.entry_for_email_subject.grid(row=2,column=1,pady=5)
        
        self.email_message=Label(self,width=20,text="Email message:") 
        self.email_message.grid(row=3,sticky=E)
        
        self.entry_for_email_message=Entry(self,width=30)
        self.entry_for_email_message.grid(row=3,column=1,pady=5,rowspan=3,ipady=10)
        
        self.send_email_button=Button(self,text='Send email!',width=10,bg='black',fg='white',command=self.send_email) 
        self.send_email_button.grid(row=6,columnspan=3,pady=10)
        
        self.label_for_message=Label(self,width=20,font=('Calibri 18 bold',20),fg='black') 
        self.label_for_message.grid(row=7,columnspan=3,pady=5)
        
    def logout(self):
        try:
            First_Frame.server.quit()
            Second_Frame.pack_forget()
            First_Frame.pack()
            First_Frame.entry_for_email.delete(0,END)
            First_Frame.entry_for_password.delete(0,END)
        except:
            messagebox.showerror('Login out error!','Error occurred while logging out!')
            
    def send_email(self):
        if self.message_verification():
            recipient=str(self.entry_for_recipients_email.get())
            subject= str(self.entry_for_email_subject.get())
            message_content=str( self.entry_for_email_message.get())
            message='From: '+First_Frame.username+'\n'+'To:'+recipient+'\n'+'Subject: '+subject+'\n'+message_content
    
            try:
                First_Frame.server.sendmail(First_Frame.username,recipient,message)
                self.label_for_message['text']='Email sent!'
            except:
                messagebox.showerror('Sending error!','Error sending email')
    
    def message_verification(self):
        recipient_email=str( self.entry_for_recipients_email.get())
        subject_text=str(self.entry_for_email_subject.get())
        message_text=str( self.entry_for_email_message.get())
        recipient_true_email=re.compile(r'[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$')
        
        if recipient_email=='' or subject_text=='' or message_text=='':
            messagebox.showerror('Email error!',"You can't leave a blank!")
            return False
        else:
            if not recipient_true_email.match(recipient_email):
                messagebox.showerror('Email error!',"Check the recipient's email address again!")
                return False
            else:
                return True
         
root=Tk()
root.title('Email Sender App')
root.geometry('425x250')
root.resizable(width=False,height=False)
First_Frame=Before_login(root)
First_Frame.pack(side=TOP)
Second_Frame=After_login(root)
root.mainloop()
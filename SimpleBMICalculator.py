from tkinter import *
from tkinter import messagebox

class Application(Frame):
    BMI=' 0.0'
    BMI_Status=''
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.configure(width=100,height=100)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.main_menu=Menu(self)
        self.sub_menu=Menu(self.main_menu,tearoff=0)
        root.configure(menu=self.main_menu)
        self.main_menu.add_cascade(label='About program',menu=self.sub_menu)
        self.sub_menu.add_command(label='Help',command=self.help_me)
        self.sub_menu.add_command(label='Exit',command=root.destroy)
        
        self.height_label=Label(self,text='Your height (cm):',font=('Calibri 18 bold'),pady=5,padx=8)
        self.height_label.grid(row=2)
        
        self.entry_for_height=Entry(self)
        self.entry_for_height.grid(row=2,column=1,columnspan=2,padx=5)
        
        self.mass_label=Label(self,text='Your mass (kg):',font=('Calibri 18 bold'),pady=5,padx=8)
        self.mass_label.grid(row=4)
        
        self.entry_for_mass=Entry(self)
        self.entry_for_mass.grid(row=4,column=1,columnspan=2,padx=5)
        
        self.bmi_label=Label(self,text='Your BMI:',font=('Calibri 18 bold'),pady=2,padx=10,justify=LEFT)
        self.bmi_label.grid(row=6)
        
        self.your_bmi=Label(self,text=Application.BMI,font=('Calibri 18 bold'),pady=10,padx=2)
        self.your_bmi.grid(row=6,column=1)
        
        self.status_label=Label(self,text='Your BMI status:',font=('Calibri 18 bold'),pady=10,padx=2)
        self.status_label.grid(row=7)
        
        self.your_bmi_status=Label(self,pady=10,padx=2,font=('Calibri 18 bold',11))
        self.your_bmi_status.grid(row=7,column=1)
        
        self.calculate_button=Button(self,text='Calculate!',font=('Calibri 18 bold'),command=self.calculate)
        self.calculate_button.grid(row=8)
        
        self.reset_button=Button(self,text='Reset',font=('Calibri 18 bold'),command=self.reset)
        self.reset_button.grid(row=8,column=1)
        
    def calculate(self):
        self.user_height=str(self.entry_for_height.get())
        self.user_mass=str(self.entry_for_mass.get())
        if self.user_height=='' or self.user_mass=='':
            messagebox.showerror('Input error!',"You can't leave a blank in any column!")
        else:
            if ',' in self.user_height:
                self.user_height=self.user_height.replace(',','.')
            if ',' in self.user_mass:
                self.user_mass=self.user_mass.replace(',','.')
            try:
                self.user_height=float( self.user_height)/100
                self.user_mass=float(self.user_mass)
                self.user_BMI=round(self.user_mass/self.user_height**2,2)
                self.your_bmi['text']=self.user_BMI
                if self.user_BMI<16:
                    self.your_bmi_status['text']='Starvation <16'
                elif self.user_BMI<17:
                    self.your_bmi_status['text']='Emaciation [16,17)'
                elif self.user_BMI<18.5:
                    self.your_bmi_status['text']='Underweight [17,18.5)'
                elif self.user_BMI<25:
                    self.your_bmi_status['text']='Optimum [18.5,25)'
                elif self.user_BMI<30:
                    self.your_bmi_status['text']='Overweight [25,30)'
                elif self.user_BMI>=30:
                    self.your_bmi_status['text']='Obesity 30≤'
            except:
                messagebox.showerror('Input error!','Input must be numbers!')
    
    def help_me(self):
        messagebox.showinfo('Help!',"First you have to enter your height and mass,\nafter that click on 'Calculate!' button and check your BMI!")
    
    def reset(self):
        self.entry_for_height.delete(0,END)
        self.entry_for_mass.delete(0,END)
        self.your_bmi['text']=Application.BMI
        self.your_bmi_status['text']=Application.BMI_Status

root=Tk()
root.title('BMI Calculator')
root.resizable(width=False,height=False)
Calculator=Application(root)
root.mainloop()
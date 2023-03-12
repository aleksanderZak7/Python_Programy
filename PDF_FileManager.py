from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2

class Main_Window(Frame):
    def __init__(self,master):
        super(Main_Window,self).__init__(master)
        self.grid()
        self.picked_file=False
        self.create_widgets()
    def create_widgets(self):
        self.main_menu=Menu(self)
        self.sub_menu=Menu(self.main_menu,tearoff=0)
        root.configure(menu=self.main_menu)
        self.main_menu.add_cascade(label='File',menu=self.sub_menu)
        self.sub_menu.add_command(label='Open',command=self.pick_pdf_file)
        self.sub_menu.add_command(label='Exit',command=root.destroy)
        self.sub_menu=Menu(self.main_menu,tearoff=0)
        self.main_menu.add_cascade(label='About program',menu=self.sub_menu)
        self.sub_menu.add_command(label='Help',command=self.help_me)
        
        self.welcome_label=Label(self,text='Change *.pdf to *.txt:',font=('Calibri 18 bold',35),pady=10,padx=20)
        self.welcome_label.grid(pady=(0,10),padx=100)
        
        self.choose_file_button=Button(self,text='Choose your \n*.pdf file!',font=('Calibri 18 bold',20),pady=15,padx=30,command=self.pick_pdf_file)
        self.choose_file_button.grid(pady=(0,20))
        
        self.name_of_pdf_file_label=Label(self,text='',font=('Calibri 18 bold',10))
        self.name_of_pdf_file_label.grid(pady=(0,25))
        
        self.message_label=Label(self,text='After changing the file format, select where you want to save it:',font=('Calibri 18 bold',15))
        self.message_label.grid(pady=(0,30))
        
        self.changing_button=Button(self,text="Let's change!",font=('Calibri 18 bold',30),pady=15,padx=20,command=self.change_format)
        self.changing_button.grid(pady=(0,35))
        
    def pick_pdf_file(self):
        self.pdf_file=filedialog.askopenfile(parent=root,mode='rb',title='Choose a PDF file:')
        self.name_of_pdf_file_label['text']=self.pdf_file
        self.picked_file=True
    
    def help_me(self):
        if self.picked_file==False:
            messagebox.showinfo('Help!',"Pick some file! File -> Open\nOr click on 'Choose your *.pdf file!' button!")
        else:
            messagebox.showinfo('Help!',"Now click on 'Let's change!' button and change your file extension!\nIf you have some errors remember,\nyou have to load a *.pdf file!")
    
    def change_format(self):
        if self.name_of_pdf_file_label['text']=='':
            messagebox.showerror('File error!','Pick your *.pdf file first!')
        else:
            try:
                PDF_reader=PyPDF2.PdfReader(self.pdf_file)
                self.txt=''
                for page in range(len(PDF_reader.pages)):
                    self.txt+=PDF_reader.pages[page].extract_text()
                self.pdf_file.close()
                self.txt_file=filedialog.asksaveasfile(defaultextension='.txt',filetypes=[('Text file','*.txt'),('Microsoft Word','*.doc'),('OpenDocument','*.odt'),('All files','.*')])
                self.txt_file.write(self.txt)
                self.txt_file.close()
                Second_Frame=After_Changing(root)
                Second_Frame.pack()
                self.pack_forget()
            except:
                messagebox.showerror('File error!','Pick *.pdf file!')

class After_Changing(Frame):
    def __init__(self,master):
        super(After_Changing,self).__init__(master)
        self.create_widgets()
    
    def create_widgets(self):
        self.welcome_label=Label(self,text='Success!',font=('Calibri 18 bold',35),pady=10,padx=20)
        self.welcome_label.grid(pady=(0,10),padx=100)
        
        self.reset_button=Button(self,text='Reset program',font=('Calibri 18 bold',20),pady=15,padx=30,command=self.reset)
        self.reset_button.grid(pady=(0,20))
    
    def reset(self):
        self.pack_forget()
        First_Frame.pack()
        First_Frame.name_of_pdf_file_label['text']=''
        First_Frame.picked_file=False
      
root=Tk()
root.title('PDF File Manager')
root.resizable(width=False,height=False)
First_Frame=Main_Window(root)
First_Frame.pack(side=TOP)
root.mainloop()
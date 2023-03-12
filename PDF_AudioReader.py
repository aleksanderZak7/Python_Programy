from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2
import pyttsx3

class Application(Frame):
    file_reading_speed=100
    pdf_file_reading=pyttsx3.init()
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.create_widgets()
        self.picked_file=False
        self.grid()
    
    def create_widgets(self):
        self.main_menu=Menu(self)
        self.sub_menu=Menu(self.main_menu,tearoff=0)
        root.configure(menu=self.main_menu)
        self.main_menu.add_cascade(label='File',menu=self.sub_menu)
        self.sub_menu.add_command(label='Open',command=self.choose_file)
        self.sub_menu.add_command(label='Exit',command=root.destroy)
        self.sub_menu=Menu(self.main_menu,tearoff=0)
        self.main_menu.add_cascade(label='About program',menu=self.sub_menu)
        self.sub_menu.add_command(label='Help',command=self.help_me)
        
        self.welcome_label=Label(self,text='PDF to Audio:',font='Calibri 18 bold',padx=70,pady=10)
        self.welcome_label.grid(columnspan=2)
        
        self.choose_file_button=Button(self,text='Select your PDF file',command=self.choose_file,padx=70,pady=10)
        self.choose_file_button.grid(row=1,columnspan=2)
        
        self.name_of_file_label=Label(self,text='',font=('Calibri 18 bold',8))
        self.name_of_file_label.grid(row=2,pady=25,columnspan=2)
        
        self.speed_label=Label(self,text='Enter speed of reading your PDF file:',font=('Calibri 18 bold',15))
        self.speed_label.grid(row=3,column=0,pady=15,padx=0,sticky=W)
        
        self.entry_for_speed=Entry(self)
        self.entry_for_speed.grid(row=3,column=1,padx=30,pady=15,sticky=W)
        
        play_button=Button(self,text="Lets' Play!",command=self.play_pdf_file,padx=60,pady=10)
        play_button.grid(row=4,columnspan=2,padx=100)  
        
    def choose_file(self):
        self.file_text=''
        self.your_file=filedialog.askopenfile(parent=root,mode='rb',title='Choose a PDF file:')
        self.name_of_file_label['text']=self.your_file
        self.picked_file=True
    
    def help_me(self):
        if self.picked_file==False:
            messagebox.showinfo('Help!',"Pick some file! File -> Open\nOr click on 'Select your PDF file' button!")
        else:
            messagebox.showinfo('Help!',"Now click on 'Lets' Play!' button and hear your PDF speaker!\nIf you have some errors try to load another file!")
                       
    def play_pdf_file(self):
        try:
            pdf_Reader=PyPDF2.PdfReader(self.your_file)
            number_of_pages=len(pdf_Reader.pages)
            for page in range(number_of_pages):
                self.file_text+=pdf_Reader.pages[page].extract_text()
            self.your_file.close()
            try:
                self.file_reading_speed=int(self.entry_for_speed.get())
                Application.pdf_file_reading.setProperty('rate',self.file_reading_speed)
            except:
                Application.pdf_file_reading.setProperty('rate',Application.file_reading_speed)
                
            Application.pdf_file_reading.setProperty('voice','f1')
            Application.pdf_file_reading.say(self.file_text)
            Application.pdf_file_reading.runAndWait()
        except:
            messagebox.showerror('File error!','Choose *.pdf file!!!!')
        
root=Tk()
root.title('PDF Audio Reader')
root.resizable(width=False,height=False)
PDF_Audio_Reader=Application(root)
root.mainloop()
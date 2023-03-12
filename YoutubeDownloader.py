from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
import re

class Download_Manager(Frame):
    def __init__(self,master):
        super(Download_Manager,self).__init__(master)
        self['bg']='red'
        self.grid_rowconfigure(0,weight=2)
        self.grid_columnconfigure(0,weight=1)
        self.my_widgets()
        self.Folder_name=''
        self.frame=True
        self.grid()
    
    def my_widgets(self):
        self.main_menu=Menu(self)
        self.sub_menu=Menu(self.main_menu,tearoff=0)
        root.configure(menu=self.main_menu)
        self.main_menu.add_cascade(label='File',menu=self.sub_menu)
        self.sub_menu.add_command(label='Save downloaded file',command=self.saving_youtube_file)
        self.sub_menu.add_command(label='Exit',command=root.destroy)
        self.sub_menu=Menu(self.main_menu,tearoff=0)
        self.main_menu.add_cascade(label='About program',menu=self.sub_menu)
        self.sub_menu.add_command(label='Help',command=self.help_me)
        
        self.welcome_label=Label(self,text='Youtube Downloader',font=('Calibri 18 bold',35),bg='red',padx=15)
        self.welcome_label.grid(pady=(0,10))
        
        self.link_label=Label(self,text='Insert a link to a YouTube video:',font=('Calibri 18 bold',15),bg='red')
        self.link_label.grid(pady=(0,20))
        
        self.entry_for_youtube_link=Entry(self,width=70)
        self.entry_for_youtube_link.grid(pady=(0,15),ipady=2)
        
        self.link_message_label=Label(self,bg='red')
        self.link_message_label.grid()
        
        self.youtube_file_save_label=Label(self,text='Choose where you want to save the file:',font=('Calibri 18 bold',15),bg='red')
        self.youtube_file_save_label.grid()
        
        self.youtube_file_save_button=Button(self,text='Click here to choose',command=self.saving_youtube_file,font=('Calibri 18 bold',12))
        self.youtube_file_save_button.grid(pady=(10,3))
        
        self.folder_name_label=Label(self,font=('Calibri 18 bold',12),bg='red')
        self.folder_name_label.grid()
        
        self.type_of_youtube_file_label=Label(self,text='Choose type of file to download:',font=('Calibri 18 bold',15),bg='red')
        self.type_of_youtube_file_label.grid()
        
        self.type_of_file=StringVar()
        self.type_of_file.set('Video')
        
        self.first_choice=Radiobutton(self,text='Video',variable=self.type_of_file,value='Video',font=('Calibri 18 bold',12),bg='red')
        self.first_choice.grid()
        
        self.second_choice=Radiobutton(self,text='Only Audio',variable=self.type_of_file,value='Audio',font=('Calibri 18 bold',12),bg='red')
        self.second_choice.grid()
        
        self.downloand_button=Button(self,text='Download!',width=10,command=self.start_downloading,font=('Calibri 18 bold',25))
        self.downloand_button.grid()
        
    def saving_youtube_file(self):
        self.Folder_name=filedialog.askdirectory()
        
        if len(self.Folder_name)>0:
            self.folder_name_label['text']=self.Folder_name
    def help_me(self):
        if len(self.entry_for_youtube_link.get())==0:
            messagebox.showinfo('Help!',"First you have to enter the link from the YouTube video you want to download")
        elif len(self.Folder_name)==0:
            messagebox.showinfo('Help!',"Now click on 'Click here to choose' button,\nor File->'Save downloaded file'\nto choose directory for your downloaded file")
        elif First_Frame.frame==False:
            messagebox.showinfo('Help!',"Now click on 'Download again!' button,\nto download file again to the same folder\nand with the same format,\nclick on 'Reset downloader!' to reset your program and your choices")
        else:
            messagebox.showinfo('Help!',"Now choose type of file to download:\nVideo\nOnly Audio\nand finally you can download your youtube video!\njust click on 'Download!' button!")
    
    def start_downloading(self):
        self.true_youtube_link=re.match('^https://www.youtube.com/.',str(self.entry_for_youtube_link.get()))
        
        if not self.true_youtube_link:
            messagebox.showerror('File error!','You provided the wrong youtube link!')
        elif self.Folder_name=='':
            messagebox.showerror('File error!','You have to choose where you want to save the file!') 
        elif self.true_youtube_link and self.Folder_name!='':
            self.youtube_video=YouTube(self.entry_for_youtube_link.get())
            self.type_of_video=self.type_of_file.get()
            
            if self.type_of_video=='Video':
                self.youtube_video.streams.first().download(self.Folder_name)
            if self.type_of_video=='Audio':
                self.youtube_video.streams.filter(only_audio=True).first().download(self.Folder_name)
                
            self.frame=False
            self.pack_forget()
            Second_Frame=After_Downloading(root)
            Second_Frame.pack()

class After_Downloading(Frame):
    def __init__(self,master):
        super(After_Downloading,self).__init__(master)
        self['bg']='red'
        self.grid_rowconfigure(0,weight=0)
        self.grid_columnconfigure(0,weight=1)
        First_Frame.pack_forget()
        self.my_widgets()
        self.grid()
        
    def my_widgets(self):
        self.downloading_label=Label(self,text='Download completed!',font=('Calibri 18 bold',25),bg='red')
        self.downloading_label.grid(pady=(0,10))
        
        self.file_title_label=Label(self,text='Title: '+First_Frame.youtube_video.title,font=('Calibri 18 bold',15),bg='red')
        self.file_title_label.grid(pady=(0,15))
        
        self.download_again_button=Button(self,text='Download again!',command=self.download_again,font=('Calibri 18 bold',15))
        self.download_again_button.grid(pady=(0,20))
        
        self.reset_button=Button(self,text='Reset downloader!',command=self.downloader_reset,font=('Calibri 18 bold',15))
        self.reset_button.grid(pady=(0,25))
    
    def download_again(self):
        First_Frame.entry_for_youtube_link.delete(0,END)
        First_Frame.pack()
        First_Frame.frame=False
        self.pack_forget()
        
    def downloader_reset(self):
        First_Frame.entry_for_youtube_link.delete(0,END)
        First_Frame.folder_name_label['text']=''
        First_Frame.type_of_file.set('Video')
        First_Frame.pack()
        First_Frame.frame=False
        self.pack_forget()
            
root=Tk()
root.title('Youtube Downloader')
root.resizable(width=False,height=False)
First_Frame=Download_Manager(root)
First_Frame.pack(side=TOP)
root.mainloop()
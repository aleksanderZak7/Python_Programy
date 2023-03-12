from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from pygame import mixer

class Top_Pack(Frame):
    def __init__(self,master):
        super(Top_Pack,self).__init__(master)
        self.pack(padx=10,pady=10)
        self.grid()
        self.file_name='0'
        self.paused=False # I suggest changing the size of all the images to 75x75
        self.rewind_image=Image.open('rewindbutton.jpg') #image ->https://www.google.com/search?q=rewind+image+button&client=opera&hs=0kT&sxsrf=AJOqlzXL9ncJ2_oAJGBu4X4kT-RM5SnXmQ:1677530359160&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj01aDJx7b9AhVFkokEHfO4B1wQ_AUoAXoECAEQAw&biw=1326&bih=658&dpr=1#imgrc=WUFEYDN987Pc7M
        self.rewind_image=ImageTk.PhotoImage(self.rewind_image)
        self.play_image=Image.open('playbutton.jpg') #image->https://www.google.com/search?q=play+button&tbm=isch&hl=pl&chips=q:play+button,online_chips:png:Dueb88UX1e0%3D,online_chips:symbol:CvImFGz8HJA%3D,online_chips:transparent:lGVhptqcF48%3D&client=opera&hs=d54&sa=X&ved=2ahUKEwj3q9GUkbb9AhXHvioKHQD0AtoQ4lYoAHoECAEQLA&biw=1311&bih=658#imgrc=tX4gbsvB8tOtAM
        self.play_image=ImageTk.PhotoImage(self.play_image)
        self.stop_image=Image.open('stopbutton.jpg') #image-> https://www.google.com/search?q=stop+music+image&tbm=isch&ved=2ahUKEwjhxYHfnbb9AhUQsCoKHf4XDaAQ2-cCegQIABAA&oq=stop+music+image&gs_lcp=CgNpbWcQA1C2BljrC2DTDGgAcAB4AIABRogB1AOSAQE3mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=Gun8Y-HQHZDgqgH-r7SACg&bih=658&biw=1326&client=opera&hs=UA6#imgrc=X7Xgb7SW4unopM
        self.stop_image=ImageTk.PhotoImage(self.stop_image)
        self.pause_image=Image.open('pausebutton.jpg') #image ->https://www.google.com/search?q=music+pause+button&tbm=isch&client=opera&hs=lH8&hl=pl&sa=X&ved=2ahUKEwjot7-IvLb9AhXTBGIAHSeDCDkQBXoECAEQRQ&biw=1311&bih=658#imgrc=TKvp3jxEESKJEM
        self.pause_image=ImageTk.PhotoImage(self.pause_image)
        self.create_widgets()
    
    def create_widgets(self):
        self.main_menu=Menu(self)
        self.sub_menu=Menu(self.main_menu,tearoff=0)
        root.configure(menu=self.main_menu)
        self.main_menu.add_cascade(label='File',menu=self.sub_menu)
        self.sub_menu.add_command(label='Open',command=self.pick_new_file)
        self.sub_menu.add_command(label='Exit',command=root.destroy)
        self.sub_menu=Menu(self.main_menu,tearoff=0)
        self.main_menu.add_cascade(label='About program',menu=self.sub_menu)
        self.sub_menu.add_command(label='Help',command=self.help_me)
        
        self.welcome_label=Label(self,text='This is play and pause buttons:',font='Calibri 18 bold')
        self.welcome_label.pack(padx=15)
        
        self.rewind_button=Button(self,image=self.rewind_image,command=self.rewind_music)
        self.rewind_button.pack(side=LEFT,padx=5)
        
        self.play_button=Button(self,image=self.play_image,command=self.start_playing)
        self.play_button.pack(side=LEFT,padx=5)
        
        self.pause_button=Button(self,image=self.stop_image,command=self.stop_playing)
        self.pause_button.pack(side=LEFT,padx=5)
        
        self.resume_button=Button(self,image=self.pause_image,command=self.pause_playing)
        self.resume_button.pack(side=LEFT,padx=5)
    
    def pick_new_file(self):
        self.file_name=filedialog.askopenfilename()
        
    def help_me(self):
        if len(self.file_name)==1:
            messagebox.showinfo('Help!','Pick some file! File -> Open')
        else:
            messagebox.showinfo('Help!','Click the Start button if you want to start listening!\nIf you want to stop the music, click the Stop button!\nIf you want to pause the music, click the Pause button!\nTo play music again, click the Start button again!\nIf you want to rewind the music, click the Rewind button!')
    
    def rewind_music(self):
        if len(self.file_name)>1:
            self.start_playing()
            Second_Pack.status_label['text']='Music is rewinded :)'
        else:
            messagebox.showerror('File error!','Pick file before playing!')
        
    def start_playing(self):
        if self.paused==True:
            self.paused=False
            mixer.music.unpause()
            Second_Pack.status_label['text']='Enjoy your music! :)'
        else:
            try:
                mixer.music.load(self.file_name)
                mixer.music.play()
                Second_Pack.status_label['text']='Enjoy your music! :)'
            except:
                if len(self.file_name)==1:
                    messagebox.showerror('File error!','Pick file before playing!')
                else:
                    messagebox.showerror('File error!','Pick another file extension!')
    
    def stop_playing(self):
        if len(self.file_name)>1:
            mixer.music.stop()
            Second_Pack.status_label['text']='Music is stopped :('
        else:
            messagebox.showerror('File error!','Pick file first!')
    
    def pause_playing(self):
        if len(self.file_name)>1:
            self.paused=True
            mixer.music.pause()
            Second_Pack.status_label['text']='Music is paused :('
        else:
            messagebox.showerror('File error!','Pick file first!')

class Bottom_Pack(Frame):
    def __init__(self,master):
        super(Bottom_Pack,self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.volume_scale=Scale(self,from_=0,to=100,orient=HORIZONTAL,command=self.set_volume)
        self.volume_scale.set(50)
        self.volume_scale.grid(columnspan=2)
        
        self.status_label=Label(self,text='Enjoy your music!',font=('Calibri 18 bold',20),anchor=W)
        self.status_label.grid(row=1,columnspan=2)
        
    def set_volume(self,value):
        self.volume=int(value)
        mixer.music.set_volume(self.volume)

mixer.init()
root=Tk()
root.title('Music Player')
root.geometry('370x200')
root.resizable(width=False,height=False)
First_Pack=Top_Pack(root)
Second_Pack=Bottom_Pack(root)
root.mainloop()
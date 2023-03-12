from tkinter import *

class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.current_Button=[-1,-1]
        self.button_list=[[]]
        self.varRow=1
        self.varColumn=0
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.text_space=Text(self,width=97,height=8)
        self.text_space.grid(row=0,columnspan=15)
        
        for button in keys:
            if button!='SPACE':
                new_button=Button(self,text=button,width=5,bg='black',fg='white',highlightthickness=4,activebackground='gray',activeforeground='red',highlightcolor='red',relief='raised',padx=12,pady=4,bd=4,command=lambda x=button,i=self.varRow-1,j=self.varColumn:self.select(x,i,j))
                new_button.bind('<Return>',lambda event,x=button,i=self.varRow-1,j=self.varColumn:self.select(x,i,j))
                self.button_list[self.varRow-1].append(new_button)
                new_button.grid(row=self.varRow,column=self.varColumn)
            elif button=='SPACE':
                new_button=Button(self,text=button,width=60,bg='black',fg='white',highlightthickness=4,activebackground='gray65',activeforeground='red',highlightcolor='red',relief='raised',padx=4,pady=4,bd=4,command=lambda x=button,i=self.varRow-1,j=self.varColumn:self.select(x,i,j))
                new_button.bind('<Return>',lambda event,x=button,i=self.varRow-1,j=self.varColumn:self.select(x,i,j))
                self.button_list[self.varRow-1].append(new_button)
                new_button.grid(row=6,columnspan=16)
            self.varColumn+=1
            if self.varColumn>10:
                self.varColumn=0
                self.varRow+=1
                self.button_list.append([])
    
    def select(self,value,x,y):
        if self.current_Button!=[-1,1]:
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightcolor='red')
        self.current_Button[:]=[x,y]
        self.button_list[x][y].configure(highlightbackground='red')
        self.button_list[x][y].configure(highlightcolor='red')
        
        if value=='DEL':
            input_value=self.text_space.get(0.0,'end-2c')
            self.text_space.delete(0.0,END)
            self.text_space.insert(0.0,input_value)
        elif value=='SPACE':
            self.text_space.insert('insert',' ')
        elif value=='TAB':
            self.text_space.insert('insert','    ')
        else:
            self.text_space.insert(END,value)
    
    def upKey(self,event):
        if self.current_Button==[-1,-1]:
            self.current_Button=[0,0]
            self.button_list[0][0].configure(highlightbackground='red')
        elif self.current_Button[0]==0:
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
            self.current_Button[:]=[(self.current_Button[0]-1)%5,0]
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
        elif self.current_Button[0]==4:
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
            self.current_Button[:]=[(self.current_Button[0]-1)%5,5]
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
        else:
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
            self.current_Button[:]=[(self.current_Button[0]-1)%5,self.current_Button[1]]
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
        self.button_list[self.current_Button[0]][self.current_Button[1]].focus_set()
    
    def downKey(self,event):
        if self.current_Button==[-1,-1]:
            self.current_Button=[0,0]
            self.button_list[0][0].configure(highlightbackground='red')
        elif self.current_Button[0]==3:
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
            self.current_Button[:]=[(self.current_Button[0]+1)%5,0]
            self.button_list[self.current_Button[0]][self.current_Button[1]%11].configure(highlightbackground='red')
        elif self.current_Button[0]==4:
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
            self.current_Button[:]=[(self.current_Button[0]+1)%5,5]
            self.button_list[self.current_Button[0]][self.current_Button[1]%11].configure(highlightbackground='red')
        else:
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
            self.current_Button[:]=[(self.current_Button[0]+1)%5,self.current_Button[1]]
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
        self.button_list[self.current_Button[0]][self.current_Button[1]].focus_set()
    
    def leftKey(self,event):
        if self.current_Button==[-1,1]:
            self.current_Button=[0,0]
            self.button_list[0][0].configure(highlightbackground='red')
        elif self.current_Button[0]==4:
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
            self.current_Button[:]=[0,0]
            self.button_list[0][10].configure(highlightbackground='red')
        else:
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
            self.current_Button[:]=[self.current_Button[0],(self.current_Button[1]-1)%11]
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
        self.button_list[self.current_Button[0]][self.current_Button[1]].focus_set()
    
    def rightKey(self,event):
        if self.current_Button==[-1,1]:
            self.current_Button=[0,0]
            self.button_list[0][0].configure(highlightbackground='red')
        elif self.current_Button[0]==4:
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
            self.current_Button[:]=[0,10]
            self.button_list[0][10].configure(highlightbackground='red')
        else:
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
            self.current_Button[:]=[self.current_Button[0],(self.current_Button[1]+1)%11]
            self.button_list[self.current_Button[0]][self.current_Button[1]].configure(highlightbackground='red')
        self.button_list[self.current_Button[0]][self.current_Button[1]].focus_set()      
        
keys=['1','2','3','4','5','6','7','8','9','0','=',
        'q','w','e','r','t','y','u','i','o','p','DEL',
        'a','s','d','f','g','h','j','k','l',';','"',
        'z','x','c','v','b','n','m',',','.','!','TAB',
        'SPACE']

root=Tk()
root.title('Keyboard application')
app=Application(root)
root.bind('<Left>',app.leftKey)
root.bind('<Right>',app.rightKey)
root.bind('<Up>',app.upKey)
root.bind('<Down>',app.downKey)
root.mainloop()
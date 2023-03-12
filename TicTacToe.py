from tkinter import *
from tkinter import messagebox
import random

class Before_Game(Frame):
    Second_Player=True
    def __init__(self,master):
        super(Before_Game,self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.welcome_label=Label(self,text='Choose a game mode:',font=('Calibri 18 bold',35))
        self.welcome_label.grid(columnspan=2,pady=5,padx=15)
        
        self.player_v_player_button=Button(self,text='PlayerVsPlayer',font=('Calibri 18 bold',15),command=self.Player_vs_Player)
        self.player_v_player_button.grid(row=1,column=0,pady=15)
        
        self.player_v_computer_button=Button(self,text='PlayerVsComputer',font=('Calibri 18 bold',15),command=self.Player_vs_Computer)
        self.player_v_computer_button.grid(row=1,column=1,pady=15)
        
    def Player_vs_Player(self):
        self.pack_forget()
        choice=Who_Starts(root)
        choice.pack(side=TOP)

    def Player_vs_Computer(self):
        Before_Game.Second_Player=False
        self.pack_forget()
        choice=Who_Starts(root)
        choice.pack(side=TOP)
        
class Who_Starts(Frame):
    def __init__(self,master):
        super(Who_Starts,self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        self.welcome_label=Label(self,font=('Calibri 18 bold',35))
        self.welcome_label.grid(columnspan=2,padx=20,pady=5)
        if Before_Game.Second_Player:
            self.welcome_label['text']='Choose who starts!'
        else:
            self.welcome_label['text']='Choose your role!'
        
        self.o_button=Button(self,text='O',font=('Calibri 18 bold',35),bg='red',command=lambda role=False:self.choice(role))
        self.o_button.grid(row=1,column=0,pady=15)
        
        self.x_button=Button(self,text='X',font=('Calibri 18 bold',35),bg='blue',command=lambda role=True:self.choice(role))
        self.x_button.grid(row=1,column=1)
    
    def choice(self,role):
        if Before_Game.Second_Player:
            Who_Starts.role=role
            Who_Starts.computer=False
        else:
            self.roles=[True,False]
            Who_Starts.role=random.choice(self.roles)
            Who_Starts.computer=True
        Who_Starts.Player_role=role
        
        self.pack_forget()
        TicTacToe=Game(root)
        TicTacToe.pack(side=TOP)

class Game(Frame):
    def __init__(self,master):
        super(Game,self).__init__(master)
        self.buttons=[]
        self.turn=Who_Starts.role
        self.moves=0
        self.create_widgets()
        self.grid()
    
    def create_widgets(self):
        for row in range(3):
            self.rows=[]
            for column in range(3):
                self.rows.append(Button(self,width=10,height=3,font=('Calibri 18 bold',35),command=lambda x=row,y=column:self.your_move(x,y)))
                self.rows[column].grid(row=row,column=column)
            self.buttons.append(self.rows)
            
        self.avaiable_moves=[self.buttons[0][0],self.buttons[0][1],self.buttons[0][2],
                            self.buttons[1][0],self.buttons[1][1],self.buttons[1][2],
                            self.buttons[2][0],self.buttons[2][1],self.buttons[2][2]]  
        
        self.best_moves=[self.buttons[1][1],self.buttons[0][0],self.buttons[0][2],self.buttons[2][0],self.buttons[2][2]]
            
        self.reset_button=Button(self,text='Restart!',width=10,height=1,font=('Calibri 18 bold',15),bg='black',fg='white',activebackground='blue3',activeforeground='white',command=self.game_restart)
        self.reset_button.grid(row=1,column=3,padx=10)   
        
        self.role_label=Label(self,font=('Calibri 18 bold',25))
        self.role_label.grid(row=0,column=3,padx=10)
        
        self.player_turn()
        if self.turn!=Who_Starts.Player_role and Who_Starts.computer:
            self.computer_turn()
    
    def ways_to_win(self):
        if (
           (self.buttons[0][0]['text']==self.buttons[0][1]['text']==self.buttons[0][2]['text']!='')
        or (self.buttons[1][0]['text']==self.buttons[1][1]['text']==self.buttons[1][2]['text']!='')
        or (self.buttons[2][0]['text']==self.buttons[2][1]['text']==self.buttons[2][2]['text']!='')
        or (self.buttons[0][0]['text']==self.buttons[1][1]['text']==self.buttons[2][2]['text']!='')
        or (self.buttons[0][2]['text']==self.buttons[1][1]['text']==self.buttons[2][0]['text']!='')
        or (self.buttons[0][0]['text']==self.buttons[1][0]['text']==self.buttons[2][0]['text']!='')
        or (self.buttons[0][1]['text']==self.buttons[1][1]['text']==self.buttons[2][1]['text']!='')
        or (self.buttons[0][2]['text']==self.buttons[1][2]['text']==self.buttons[2][2]['text']!='')):
            return True
    
    def your_move(self,row,column):
        self.moves+=1
        if self.turn:
                self.role='X'
                self.buttons[row][column].config(text=self.role,bg='blue',state='disabled')
        else:
            self.role='O'
            self.buttons[row][column].config(text=self.role,bg='red',state='disabled')
        self.turn=not self.turn
        self.player_turn()
        self.win()
        self.avaiable_moves.remove(self.buttons[row][column])
        if Who_Starts.computer:
            self.computer_turn()
    
    def player_turn(self):
        if  Who_Starts.computer:
            self.role_label['text']="Your turn!"
        else:   
            if self.turn:
                self.role_label['text']="Player turn:\n'X'"
            else:
                self.role_label['text']="Player turn:\n'0'"
                
    def computer_turn(self):
        if self.moves==9:
            pass
        elif self.reset_button['text']=='New Game!':
            pass
        else:
            self.moves+=1
            if self.win_judge() or self.player_win():
                self.computer_move(self.move)
            else:
                disabled=0
                for move in self.best_moves:
                    if move in self.avaiable_moves:
                        self.computer_move(move)
                        break
                    else:
                        disabled+=1
                        if disabled==5:
                            move=random.choice(self.avaiable_moves)
                            self.computer_move(move)
            self.turn=not self.turn
            self.player_turn()
            self.computer_win()
    
    def computer_move(self,move):
        if self.turn:
            self.role='X'
            move.config(text=self.role,bg='blue',state='disabled')
        else:
            self.role='O'
            move.config(text=self.role,bg='red',state='disabled')
        self.avaiable_moves.remove(move)
    
    def win(self):
        if self.ways_to_win():
            self.reset_button['text']='New Game!'
            if Who_Starts.computer:
                messagebox.showinfo('Congratulasions!','Amazing! You won vs a computer!')
                self.role_label['text']=":)"
            else:
                messagebox.showinfo('Congratulasions!',f"Player '{self.role}' wins!")
        elif self.moves==9:
            messagebox.showinfo('DRAW!',"It's a draw! Better luck next time!")
            self.role_label['text']=":O"
    
    def computer_win(self):
        if self.ways_to_win():
            self.reset_button['text']='New Game!'
            messagebox.showinfo('Computer won!','Better luck next time :D!')
            self.role_label['text']=":("
        elif self.moves==9:
            messagebox.showinfo('DRAW!',"It's a draw! Better luck next time!")
            self.role_label['text']=":O"
            
    def win_judge(self):
        for move in self.avaiable_moves:
            if self.turn:
                self.role='X'
            else:
                self.role='O'
            move['text']=self.role
            if self.ways_to_win():
                self.move=move
                return True
            else:
                move['text']=''
    
    def player_win(self):
        for move in self.avaiable_moves:
            if self.turn:
                self.role='O'
            else:
                self.role='X'
            move['text']=self.role
            if self.ways_to_win():
                self.move=move
                return True
            else:
                move['text']=''
    
    def game_restart(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.buttons=[]
        self.moves=0
        self.create_widgets()

root=Tk()
root.title('TicTacToe')
root.resizable(width=False,height=False)
app=Before_Game(root)
app.pack(side=TOP)
root.mainloop()
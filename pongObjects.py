import tkinter as tk
from tkinter import messagebox


class Paddle():
    def __init__(self, xpos: int, state: str, player: int):
        xpos  = 0
        state = 'S'
        player = 1
        
    def Position(self) -> int:
        return self.xpos
    
    def currentState(self) -> str:
        return self.state
    
    def changePlayer(self, activePlayer: int):
        # player one layout WASD
        # player two layout IJKL
        if 1 <= activePlayer <= 2:
            self.player = activePlayer
    
    def changePos(self):
        direction = input()
        if self.player == 1 and direction == 'a' or direction == 'A':
            self.state = 'L'
        if self.player == 1 and direction == 'd' or direction == 'D':
            self.state = 'L'
        if self.player == 2 and direction == 'j' or direction == 'J':
            self.state = 'R'
        if self.player == 2 and direction == 'l' or direction == 'L':
            self.state = 'R'
        else: 
            self.state = 'S'
        
    
class Ball():
    def __init__(self, xpos: int, ypos: int, xmag: int, ymag: int):
        xpos = 0
        ypos = 0
        xmag = 0
        ymag = 0
        
    def Position(self) -> list[int]:
        return [self.xpos, self.ypos]
    
    def Velocity(self) -> list[int]:
        return [self.xmag, self.ymag]
    
    def updateState(self, boardXpos: int, boardYpos: int):
        self.xpos = boardXpos
        self.ypos = boardYpos



class pongGUI():
    def __init__(self):
         self.root = tk.Tk()
         
         self.label = tk.Label(self.root, text = 'Your message', font = ('Arial', 18))
         self.label.pack(padx = 10, pady = 10)
         
         self.textbox = tk.Text(self.root, height = 5, font = ('Arial', 16))
         self.textbox.bind("<KeyPress>", self.shortcut)
         self.textbox.pack(padx =10, pady =10)
         
         self.checkState = tk.IntVar()
         
         self.check = tk.Checkbutton(self.root, text = "Show Message Box", font = ('Arial', 16), variable = self.checkState)
         self.check.pack(padx =10, pady =10)
         
         self.button = tk.Button(self.root, text = "Show Message", font = ('Arial', 18), command = self.showMessage)
         self.button.pack(padx =10, pady =10)
         
         self.root.mainloop()

    def showMessage(self):
        #prints to the terminal
        if self.checkState.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title = "Message", message = self.textbox.get('1.0', tk.END))
        
    def shortcut(self, event):
        # you can make a shorcut by reading the key key press information
        #print(event.keysym)
        #print(event.state)
        
        #Mac shortcut Command + enter
        if event.state == 12 and event.keysym == "Return":
            self.showMessage()
        #Windows ctrl + enter
        if event.state == 8 and event.keysym == "Return":
            self.showMessage()



pongGUI()
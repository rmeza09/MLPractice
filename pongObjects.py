
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

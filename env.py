#environment for tic tac toe


#imps
import numpy as np


#main board
class tic_board():
    def __init__(self):
        self.board = np.zeros((1,9))[0]
        self.info = 0

    def reset(self):
        self.board = np.zeros((1,9))[0]
        return np.array(self.board)

    def board_diagram(self):
        print()
        print("|   {}   |   {}   |   {}   |".format(int(self.board[0]),int(self.board[1]),int(self.board[2])))
        print("----------------------")
        print("|   {}   |   {}   |   {}   |".format(int(self.board[3]),int(self.board[4]),int(self.board[5])))
        print("----------------------")
        print("|   {}   |   {}   |   {}   |".format(int(self.board[6]),int(self.board[7]),int(self.board[8])))
        print()
        
    def observation(self):
        return np.array(self.board),self.info
    
    def action(self,symbol,position):
        if not self.info:
            self.board[position] = symbol
            self.is_full()
            self.is_winner(symbol)

    def available_action(self):
        action = []
        for i in range(9):
            if self.board[i] == 0:
                action.append(i)
        action = np.array(action)
        return action

    def is_full(self):
        flag = 0
        for i in range(9):
            if self.board[i] == 0:
                flag = 1

        if flag == 0:
            self.info = "game-tie"

    def is_winner(self,symbol):
        win = 0
        if self.board[0] == self.board[1] and self.board[0] == self.board[2]:
            if self.board[0]:
                win = 1
        if self.board[3] == self.board[4] and self.board[3] == self.board[5]:
            if self.board[3]:
                win = 1
        if self.board[6] == self.board[7] and self.board[6] == self.board[8]:
            if self.board[6]:
                win = 1
        if self.board[0] == self.board[3] and self.board[0] == self.board[6]:
            if self.board[0]:
                win = 1
        if self.board[1] == self.board[4] and self.board[1] == self.board[7]:
            if self.board[1]:
                win = 1
        if self.board[2] == self.board[5] and self.board[2] == self.board[8]:
            if self.board[2]:
                win = 1
        if self.board[0] == self.board[4] and self.board[0] == self.board[8]:
            if self.board[0]:
                win = 1
        if self.board[2] == self.board[4] and self.board[2] == self.board[6]:
            if self.board[2]:
                win = 1

        if win:
            self.info = "winner - " + str(symbol)


def rotate_turns(turn,p1,p2):
    if turn.symbol()==1:
        turn = p2
    else:
        turn = p1

    return turn

    
        

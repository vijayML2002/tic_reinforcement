#tic tac toe 1vs1

from env import tic_board,rotate_turns
from agent import agent
import numpy as np


#creating the board
board = tic_board()

#creating the players
p1 = agent(1)
p2 = agent(-1)
win = [0,0,0]

#number of episodes
episode = 100

for i in range(episode):
    turn = np.random.choice([p1,p2])
    game_state = 0
    board = tic_board()
    current_board,info = board.observation()

    while not game_state:
        available_action = board.available_action()
        position = turn.act(current_board,available_action)
        board.action(turn.symbol(),position)
        new_board,info = board.observation()
        if info=='winner - -1':
            game_state = 1
            win[1] += 1
            p2.storage(current_board,position,10,new_board,1)

        if info=='winner - 1':
            game_state = 1
            win[0] += 1
            p1.storage(current_board,position,10,new_board,1)

        if info=='game-tie':
            game_state = 1
            win[2] += 1
            turn.storage(current_board,position,5,new_board,1)
        
        if not game_state:
            turn.storage(current_board,position,-1,new_board,1)
            turn = rotate_turns(turn,p1,p2)
            current_board = new_board

    p1.rewind_memory()
    p2.rewind_memory()
    print("Episode ---->  {}   Result ---->  {}   win_array ----> {}".format(i,info,win))    







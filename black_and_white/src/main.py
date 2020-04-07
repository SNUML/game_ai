import sys, os
from frame import State
from player1 import Player as player1
from player2 import Player as player2

def play_game(game_cnt,p1,p2) :
    #p1 = player1()
    #p2 = player2()
    p1.init()
    p2.init()
    s = State()
    print("{}th Game!".format(game_cnt+1))
    for _ in range(9) :
        (s1,s2) = s.player_states()
        if s.turn == 0 :
            c1 = p1.query(s1)
            s2.opp = (c1%2)
            c2 = p2.query(s2)
        else :
            c2 = p2.query(s2)
            s1.opp = (c2%2)
            c1 = p1.query(s1)
        s.draw(c1,c2)
    if s.score[0] > s.score[1] : return -1
    elif s.score[0] < s.score[1] : return 1
    return 0

game_num = int(sys.argv[1])
tot_sco = [0,0]

p1 = player1()
p2 = player2()
for game_cnt in range(game_num) :
    result = play_game(game_cnt,p1,p2)
    if result > 0 : 
        tot_sco[1] += 1
        print("Player 2 won!")
    elif result < 0 : 
        tot_sco[0] += 1
        print("Player 1 won!")

print("RESULT : {} vs {}".format(tot_sco[0],tot_sco[1]))
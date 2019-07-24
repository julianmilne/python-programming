#hoW many varieables needed


#how to track player 1, player 2

#input(role dice)
'''
import random

player_1 = 0
player_2 = 0
player1_total = 0
player2_total = 0
input()
val = random.randint(1,6)
turn = [0, 1]




while player1_total < 10:
    if turn == 0:
        roll =(input("Type 'r' to Roll Type 'h' to Hold"))
        val = random.randint(1,6)
        if val == 0:
            print("START AGAIN!")
            turn = 1
            player1_total = 0
        elif player1_total += val:
    print(player1_total)

#role dice 

print(val)

input('player 2 role dice')

print(val)

'''
'''
import random

def play_pig():
    player1_score, player2_score = 0, 0
    turn = 0
    #while either player has not reached a score of ten
    while(True):
        #if its player 1s turn roll or holl
        if turn == 0:
            choice = input('[player 1] roll or hold:  ')
            if choice == 'r':
                round_score = random.randint(1, 6)
                if round_score == 1:
                    player1_score = 0
                    turn = 1
                else:
                    player1_score += round_score
                print(f'round score {round_score}, total score {player1_score}')
            else:
                turn = 1
        

        if turn == 1:
            choice = input('[player 2] roll or hold:  ')
            if choice == 'r':
                round_score = random.randint(1, 6)
                if round_score == 1:
                    player2_score = 0
                    turn = 0
                else:
                    player2_score += round_score
                print(f'round score {round_score}, total score {player1_score}')
            else:
                turn = 0

#check if a plyer has won
        if player1_score >= 10 or player2_score >= 10:
            break

    if player1_score >= 10:
        print('PLAYER1 WINS!!!')
    else:
        print('PLAYER2 WINS!!!')

play_pig()

'''

#refactor round funtion
player_scores = [0, 0]
turn_var = [random.randint(0, 1)]

def roll(turn):
    choice = input(f'[PLAYER {}] Roll or Hold: ')
    if choice == 'r':
        round_score = random.randint(1, 6)
        if round_score == 1:
            player_scores[turn] = 0
            if turn == 1:
                turn = 0
            else:
                turn = 1
        else:
            player_scores[turn] += round_score
    
    print(f'round score {round_score}, total score {player_scores[turn]}')
    else:
        if turn = 0:
            turn = 1:
        else:
            turn = 0

turn = random.randint(0, 1)
while(True):
    roll(turn)
    if player_scores[0] >= 20 or player_scores[1] >= 20:
        break

if player1_score >= 10:
        print('PLAYER1 WINS!!!')
else:
        print('PLAYER2 WINS!!!')


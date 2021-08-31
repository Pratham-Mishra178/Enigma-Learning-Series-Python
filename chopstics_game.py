player_1 = [1, 1]
player_2 = [1, 1]
print("\nCurrent Status : ""\nplayer 1:", player_1, "\nplayer 2:", player_2)

def player1():
    player1_move = input('\nEnter move for Player 1 (A/S) : ')

    if player1_move == 'A' or player1_move == 'a':
        player1_attack = input('Enter the move combination (LR/LL/RL/RR): ')

        if player1_attack == 'lr' or player1_attack == 'LR':
            player_2[1] += player_1[0]
            if(player_2[1] >= 5):
                player_2[1] = 0

        if player1_attack == 'll' or player1_attack == 'LL':
            player_2[0] += player_1[0]
            if(player_2[0] >= 5):
                player_2[0] = 0

        if player1_attack == 'rr' or player1_attack == 'RR':
            player_2[1] += player_1[1]
            if(player_2[1] >= 5):
                player_2[1] = 0

        if player1_attack == 'rl' or player1_attack == 'RL':
            player_2[0] += player_1[1]
            if(player_2[0] >= 5):
                player_2[0] = 0

    if player1_move == 'S' or player1_move == 's':
        combo = input('Enter the move combination (L_ _/R_ _) : ')
        player1_hand = combo[0]
        player1_lefthand = int(combo[1])
        player1_righthand = int(combo[2])

        
        if(player1_hand == 'l' or player1_hand == 'L'):
                if(player_1[0] > 1):
                    player_1[0] = player1_lefthand
                    player_1[1] = player1_righthand
                else:
                    print('\nInvalid Move')
                    player1()

        if(player1_hand == 'r' or player1_hand == 'R'):
                if(player_1[1] > 1):
                    player_1[0] = player1_lefthand
                    player_1[1] = player1_righthand
                else:
                    print('\nInvalid Move')
                    player1()
                    

        

    print("\nCurrent Status : ""\nplayer 1:",player_1, "\nplayer 2:", player_2)

def player2():
    player2_move = input('\nEnter move for Player 2 : ')
    if player2_move == 'A' or player2_move == 'a':
        player2_attack = input('Enter the move combination (LR/LL/RL/RR) : ')

        if player2_attack == 'lr' or player2_attack == 'LR':
            player_1[1] += player_2[0]
            if(player_1[1] >= 5):
                player_1[1] = 0

        if player2_attack == 'll' or player2_attack == 'LL':
            player_1[0] += player_2[0]
            if(player_1[0] >= 5):
                player_1[0] = 0

        if player2_attack == 'rr' or player2_attack == 'RR':
            player_1[1] += player_2[1]
            if(player_1[1] >= 5):
                player_1[1] = 0

        if player2_attack == 'rl' or player2_attack == 'RL':
            player_1[0] += player_2[1]
            if(player_1[0] >= 5):
                player_1[0] = 0

    if player2_move == 'S' or player2_move == 's':
        combo = input('Enter the move combination (L_ _/R_ _) : ')
        player2_hand = combo[0]
        player2_lefthand = int(combo[1])
        player2_righthand = int(combo[2])

        
        if(player2_hand == 'l' or player2_hand == 'L'):
                if(player_2[0] > 1):
                    player_2[0] = player2_lefthand
                    player_2[1] = player2_righthand
                else:
                    print('\nInvalid Move')
                    player2()

        if(player2_hand == 'r' or player2_hand == 'R'):
                if(player_2[1] > 1):
                    player_2[0] = player2_lefthand
                    player_2[1] = player2_righthand
                else:
                    print('\nInvalid Move')
                    player2()
        
    print("\nCurrent Status : ""\nplayer 1:",player_1, "\nplayer 2:", player_2)






while ((player_1[0] != 0 or player_1[1] != 0) and (player_2[0] != 0 or player_2[1] != 0)):

    player1()

    player2()




if(player_1[0] == 0 and player_1[1] == 0):
    print('\n***PLAYER 2 WINS***\n')
if(player_2[0] == 0 and player_2[1] == 0):
    print('\n***PLAYER 1 WINS***\n')

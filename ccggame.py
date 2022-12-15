import random
print("Welcome to the Colors Choices Game")
print("Winning rules for the CCG are as follows:"+"/nEnter a number from 1 - 5 and match the computer choice")
computer_score = 0
player_score = 0

while True:
    print("red = 1/n yellow = 2 /n orange = 3 /n green = 4 / take a turn:")
    player_choice = int(input("Your turn: "))

    while player_choice > 5 and player_choice < 1:
        player_choice = int(input("Enter valid input: "))

    if player_choice == 1:
        choice_col_player = "red"
    if player_choice == 2:
        choice_col_player = "yellow"
    if player_choice == 3:
        choice_col_player = "orange"
    if player_choice == 4:
        choice_col_player= "green"
    else:
        choice_col_player = "blue"

    print("user color choice is: " + choice_col_player)
    print("Computer is going to choose option:.........")

    computer_choice = random.randint(1,5)

    if computer_choice == 1:
        choice_col_computer = "red"
    if computer_choice == 2:
        choice_col_computer = "yellow"
    if computer_choice == 3:
        choice_col_computer = "orange"
    if computer_choice == 4:
        choice_col_computer = "green"
    else:
        choice_col_computer = "blue"

    print("Computer color choice is: " + choice_col_computer)

    if(choice_col_player == choice_col_player):
        player_score += 1
        print("Player score: "+ str(player_score))
        print("computer score: " + str(computer_score))
    else:
        computer_score += 1
        print("Player score: "+ str(player_score))
        print("computer score: " + str(computer_score))
    print("DO you want to play again? (Y/N")
    answer = input()
    if answer == 'n' or answer == 'N':
        break
if computer_score == player_score:
    print("Game is Tied")
    print("Thanks for playing")
elif computer_score < player_score:
    print("You win the game")
    print("Thanks for playing")
elif computer_score > player_score:
    print("Computer wins the game")
    print("Thanks for playing")

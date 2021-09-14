import random, sys


print("""Let's play Rock, Paper, Scissors
Choose (r)ock, (p)aper of (s)cissors
Enter 'quit' at any time to quit""") 

wins = 0
ties = 0
loses = 0 
while True:
    score = f"Wins: {wins} Ties: {ties} Loses: {loses}"
    print(score)
    choice = input("Choose: ")
    computer = random.randint(1,3)
    if choice == 'quit':
        sys.exit()
    elif choice == 'r':
        print("You Chose Rock")
    elif choice == 'p':
        print("You Chose Paper")
    elif choice == 's':
        print("You Chose Scissors")

    if choice == 'r':
        choice = 1
    elif choice == 'p':
        choice = 2
    elif choice == 's':
        choice = 3


    if choice == computer:
        print("It's a draw!")
        ties += 1

    
    if choice == 1 and computer == 2:
        print("Rock loses to Paper!")
        loses += 1
    # rock beats scissors
    elif choice == 1 and computer == 3:
        print("Rock beats Scissors!")
        wins += 1
    elif choice == 2 and computer == 1:
        print("Paper Beats Rock!")
        wins += 1
    elif choice == 2 and computer == 3:
        print("Paper loses to Scissors")
        loses += 1
    elif choice == 3 and computer == 1:
        print("Scissors loses to Rock!")
        loses += 1
    elif choice == 3 and computer == 2:
        print("Paper beats Rock!")
        wins += 1
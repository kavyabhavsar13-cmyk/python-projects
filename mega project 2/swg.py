from random import choice




def play():
    list=["snake","water","gun"]
    import random
    computer=random.choice(list)
    print("\033[1;32m-----------------------------------------------------------------------------------------------\033[0m")
    print("\033[1;32m|                                                                                             |\033[0m")
    print("\033[1;32m|                                  Welcome to Snake Water Gun Game!                           |\033[0m")
    print("\033[1;32m|                                                                                             |\033[0m")
    print("\033[1;32m-----------------------------------------------------------------------------------------------\033[0m")

    print("\033[1;35m******************************************************************************************************************************************\033[0m")
    print("\033[1;35m* INSTRUCTIONS:                                                                                 \033[0m")
    print("\033[1;35m* 1. The game is played between the user and the computer.                                       \033[0m")
    print("\033[1;35m* 2. The user can choose between three options: snake, water, and gun. The computer will also randomly choose one of these options.     \033[0m")
    print("\033[1;35m* 3. The rules of the game are as follows: snake drinks water, gun shoots snake, and water douses gun. If both the user and the computer choose the same option, it's a tie.     \033[0m")
    print("\033[1;35m* 4. The game continues until the user decides to stop playing. After each round, the user will be asked if they want to play again.     \033[0m")
    print("\033[1;35m******************************************************************************************************************************************\033[0m")
    name=input("enter your name to start the game:")
    print(f"welcome \033[1;40m{name}\033[1;40m to snake water gun game! choose snake, water gun to play the game")

    
    choice=input("kindly choose between snake, water and gun to play the game: ")
    while choice not in list:
            print("invalid choice, please choose snake, water or gun")
            choice=input("kindly choose between snake, water and gun to play the game: ")
    print(f"\033[1;32myou chose:\033[0m {choice}")
    if(computer==choice):
            print(f"both you and computer chose {choice}. It's a tie!")
            with open("swg_leaderboard.txt","a") as f:
                f.write(f"{name}: both chose {choice}, it was a tie\n")
    elif(choice=="snake" and computer=="gun") or (choice=="water" and computer=="snake") or (choice=="gun" and computer=="water"):
            with open("swg_leaderboard.txt","a") as f:                
                   f.write(f"{name} chose {choice} and computer chose {computer}, \033[91m{name} lost the game\033[0m\n")
            print(f"You lose! You chose {choice} and the computer chose {computer}. \033[91mlost the game\033[0m, better luck next time")

    else:
            with open("swg_leaderboard.txt","a") as f:                
                f.write(f"{name} chose {choice} and computer chose {computer}, \033[92m{name} won the game\033[0m\n")
            print(f"You win! You chose {choice} and the computer chose {computer}. \033[92mCongratulations!\033[0m")

    print("\033[96m---------------------------leaderboard:-------------------------\033[0m")

    with open("swg_leaderboard.txt","r") as f:
        for line in f:
                print(line.strip())
    print("\033[96m----------------------------------------------------------------\033[0m")
    again=input("do you want to play again? Say yes or no: ")
    if again=="yes":
            play()
    if again=="no":
        print("Thanks for playing! Goodbye!")
        return
    else:
        print("invalid input, exiting the game.")
        return

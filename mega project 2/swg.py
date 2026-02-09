def swg():
    list=["snake","water","gun"]
    import random
    computer=random.choice(list)
    print("-----------------------------------------------------------------------------------------------")
    print("|                                                                                             |")
    print("|                                  Welcome to Snake Water Gun Game!                           |")
    print("|                                                                                             |")
    print("-----------------------------------------------------------------------------------------------")
    name=input("enter your name to start the game:")
    print(f"welcome {name} to snake water gun game! choose snake, water gun to play the game")
    
    choice=input("kindly choose between snake, water and gun to play the game: ")
    while choice not in list:
            print("invalid choice, please choose snake, water or gun")
            choice=input("kindly choose between snake, water and gun to play the game: ")
    print(f"you chose: {choice}")
    if(computer==choice):
            
            print(f"both you and computer chose {choice}. It's a tie!")
    elif(choice=="snake" and computer=="gun") or (choice=="water" and computer=="snake") or (choice=="gun" and computer=="water"):
            
            print(f"You lose! You chose {choice} and the computer chose {computer}.better luck next time")
    else:
            
            print(f"You win! You chose {choice} and the computer chose {computer}. Congratulations!")
    again=input("do you want to play again? Say yes or no: ")
    if again=="yes":
            swg()
    if again=="no":
        print("Thanks for playing! Goodbye!")
        return
    else:
        print("invalid input, exiting the game.")
        return
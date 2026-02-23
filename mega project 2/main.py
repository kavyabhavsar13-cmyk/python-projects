import swg 
import games.hangman
import guess
if __name__=="__main__":
    print("\033[1;93m=================================================WELCOME TO THE GAME ZONE!================================================\033[0m")
    print("Here you can play three different games: Snake Water Gun, Hangman and Guess the Number. Choose your game and have fun!")
    print("\033[1;93m================================================================================================================================\033[0m")
    print("1. Snake Water Gun")
    print("2. Hangman")
    print("3. Guess the Number")
    print("4. Exit")
    while(True):        
        choice=input("Please enter the number corresponding to the game you want to play: ")
        if choice in ["1","2","3","4"]:
            if choice == "1":
                print("\033[1;32mYou have chosen Snake Water Gun! Get ready to play!\033[0m")
                swg.play()
            elif choice == "2":
                print("\033[1;32mYou have chosen Hangman! Get ready to play!\033[0m")
                games.hangman.hangman()
            elif choice == "3":
                print("\033[1;32mYou have chosen Guess the Number! Get ready to play!\033[0m")
                guess.game()
            elif choice == "4":
                print("\033[1;32mThanks for playing! Goodbye!\033[0m")
                break
            
    
        
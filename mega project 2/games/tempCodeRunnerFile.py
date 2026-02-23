print("\033[1;35;103m**************************************************************************************************************\033[0m")
    print("\033[1;35;103m*                                                                                                            *\033[0m")
    print("\033[1;35;103m*                                              WELCOME TO HANGMAN!                                           *\033[0m")
    print("\033[1;35;103m*                                                                                                            *\033[0m")
    print("\033[1;35;103m**************************************************************************************************************\033[0m")


    print("=============================================================================================================")
    print("< INSTRUCTIONS:                                                                                              >")
    print("< 1. The computer will think of a word, and you have to guess it through letter or a whole word at once.     >")
    print("< 2. You have 6 lives. Each wrong guess will cost you a life.                                                >")
    print("< 3. If you guess the word correctly, you win! If you run out of lives, you lose.                            >")
    print("=============================================================================================================")
    name = input("Please enter your name to start the game: ")
    print(f"Welcome, {name}!")
    words = ["mango", "banana", "grape", "orange", "watermelon", "strawberry", "blueberry", "pineapple", "peach", "kiwi"]
    import random
    word = random.choice(words)
    lives=6
    attempts=0
    final=["_ "] * len(word)
    print(lives)
    while(lives>0 and "".join(final)!=word):
        print("=========================================================================================================")
        print("".join(final))
        print(f"You have {lives} lives remaining")
        choice=input("enter your guess:")
        while  not choice.isalpha():
            choice=input("Please enter a valid guess:")
        length=len(choice)
        attempts+=1
        
        for c in choice:
            index=-1
            if c in word:
                 print(f"\033[92mGood job! The letter '{c}' is in the word.\033[0m")
                 for l in word:
                      index+=1
                      if l==c and index<len(final):
                        final[index]=c
                        

            else:
                lives-=1
                print(f"\033[91mWrong guess! The letter '{c}' is not in the word.\033[0m")
    guessed="".join(final)
    if (guessed == word and lives>0):
                print(f"\033[92mYou guessed the word correctly in {attempts} attempts ＾▽＾ \033[0m")
                with open("hangman_leader.txt","a") as f:
                    f.write(f"{name}:{attempts}\n")
                
    elif(guessed!=word or lives==0):
                print(f"\033[91mOop! you ran out of lives.Better luck next time\033[0m")
                with open("hangman_leader.txt","a") as f:
                    f.write(f"{name}:lost the game\n")
    print(f"The word was {word} !")
    highscore = 7
    with open("hangman_leader.txt","r") as f:
        for line in f:
            parts = line.strip().split(":")

            if len(parts)==2:
                name,score = parts

                if score != "lost the game":
                    score = int(score)
                    if score < highscore:
                        highscore = score
    print("------------------------------LEADERBOARD------------------------------")
    with open("hangman_leader.txt","r") as f:
        for line in f:
            parts = line.strip().split(":")

            if len(parts)==2:
                name,score = parts

                if score != "lost the game":
                    score = int(score)
                    if score == highscore:
                        print(f"{name}: {score} attempts (high score)")
                    else:
                        print(f"{name}: {score} attempts")
                else:
                    print(f"{name}: {score}")
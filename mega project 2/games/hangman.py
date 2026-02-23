
'''def hangman():
    print("**************************************************************************************************************")
    print("                                               Welcome to Hangman!")
    print("**************************************************************************************************************")
    speak("say your name to start the game.")
    name=listen()
    
    if not name:
        speak("I didn't catch your name. Please say it again.")
        name = listen()

    speak(f"Welcome {name} to Hangman! Let's play!")
    speak("I will think of a word, and you have to guess it letter by letter. You have 5 lives. Good luck!")
    words=["mango","banana","grape","orange","watermelon","strawberry","blueberry","pineapple","peach","kiwi"]
    import random
    word=random.choice(words)
    final="_"*len(word)
    dict={}
    lives=5
    attempts=0
    while lives>0 and final!=word:
        
        print(f"Word: {final}")
        speak(f"the word is of length {len(word)}.  Please guess a letter.")
        if lives==1:
            speak("You have 1 life left. Be careful!")
        
        else:
            speak(f"You have {lives} lives left.")
            command=listen()

        if command == "":
            command = listen()
        
        attempts+=1
        if command in word:
           command = command[0]
           i=word.index(command)
           final=final[:i]+command+final[i+1:]
           speak(f"Good job! The letter {command} is in the word.")
           
        else:
            speak(f"Sorry, the letter {command} is not in the word.")
            lives-=1
    
    if final==word and lives>0:
        speak(f"Congratulations! You guessed the word {word} in {attempts} attempts!")
        dict[name]=attempts
        if attempts<highscore:
            speak("Wow! You set a new high score!")
    else:
        speak(f"Game over! The word was {word}. Better luck next time!")
        dict[name]="lost the game"
    print("--------------leaderboard:--------------")

    highscore=max(dict.values())
    for name, attempts in dict.items():
        if attempts!="lost the game" and attempts!=highscore:
            print(f"{name}: {attempts} attempts")
        elif attempts==highscore:
            print(f"{name}: {attempts} attempts (high score)")
        else:            print(f"{name}: {attempts}")'''
def hangman():
    
    print("\033[1;96;40m***********************************************************************************************************************************************\033[0m")
    print("\033[1;96;40m*                                                                                                                                             *\033[0m")
    print("\033[1;96;40m*                                                              WELCOME TO HANGMAN!                                                            *\033[0m")
    print("\033[1;96;40m*                                                                                                                                             *\033[0m")
    print("\033[1;96;40m***********************************************************************************************************************************************\033[0m")



    print("\033[1;35m=============================================================================================================\033[0m")
    print("\033[1;35m< INSTRUCTIONS:                                                                                              >\033[0m")
    print("\033[1;35m< 1. The computer will think of a word, and you have to guess it through letter or a whole word at once.     >\033[0m")
    print("\033[1;35m< 2. You have 6 lives. Each wrong guess will cost you a life.                                                >\033[0m")
    print("\033[1;35m< 3. If you guess the word correctly, you win! If you run out of lives, you lose.                            >\033[0m")
    print("\033[1;35m=============================================================================================================\033[0m")

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
        print(f"\033[1;96m{''.join(final)}\033[0m")

        print(f"You have \033[1;35m{lives} lives\033[0m remaining")
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
    print("\033[1;93m--------------------------------------------------------LEADERBOARD-------------------------------------------------------------\033[0m")

    with open("hangman_leader.txt","r") as f:
        for line in f:
            parts = line.strip().split(":")

            if len(parts)==2:
                name,score = parts

                if score != "lost the game":
                    score = int(score)
                    if score == highscore:
                        print(f"{name}: {score} attempts \033[1;96m(high score)\033[0m")

                    else:
                        print(f"{name}: {score} attempts")
                else:
                    print(f"{name}: {score}")







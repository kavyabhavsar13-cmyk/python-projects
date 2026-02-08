import time
import speech_recognition as sr
import pyttsx3
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(1)
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, phrase_time_limit=3)

    try:
        return recognizer.recognize_google(audio).lower().strip()
    except sr.UnknownValueError:
        return ""


def hangman():
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
    final="__ "*len(word)
    dict={}
    lives=5
    attempts=0
    while lives>0 and final!=word:
        
        print(f"Word: {final}")
        speak(f"the word is of length {len(word)}.  Please guess a letter.")
        if(lives==1):
            speak("You have 1 life left. Be careful!")
        
        else:
            speak(f"You have {lives} lives left.")
        command=listen()
        
        attempts+=1
        if command in word:
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
        else:            print(f"{name}: {attempts}")
if __name__ == "__main__":
    hangman()
    
import time
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    time.sleep(1)
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, phrase_time_limit=3)

    try:
        text =  recognizer.recognize_google(audio).lower().strip()
        print(f"recognised: {text}")
        return text
    except sr.UnknownValueError:
        print("unknown value in processing the audio")
        return ""
def swg():
    list=["snake","water","gun"]
    import random
    computer=random.choice(list)
    speak("kindly say your name to start the game:")
    name=listen()
    if not name:
        speak("I didn't catch your name. Please say it again.")
        name = listen()
    speak(f"hello {name},welcome to snake water gun game! choose snake, water gun to play the game")
    print(f"welcome {name} to snake water gun game! choose snake, water gun to play the game")
    choice=listen()
    while choice not in list:
        speak("invalid choice, please choose snake, water or gun")
        print("invalid choice, please choose snake, water or gun")
        choice=listen()
    print(f"you chose: {choice}")
    if(computer==choice):
        speak(f"both you and computer chose {choice}. It's a tie!")
        print(f"both you and computer chose {choice}. It's a tie!")
    elif(choice=="snake" and computer=="gun") or (choice=="water" and computer=="snake") or (choice=="gun" and computer=="water"):
        speak(f"You lose! You chose {choice} and the computer chose {computer}.better luck next time")
        print(f"You lose! You chose {choice} and the computer chose {computer}.better luck next time")
    else:
        speak(f"You win! You chose {choice} and the computer chose {computer}. Congratulations!")
        print(f"You win! You chose {choice} and the computer chose {computer}. Congratulations!")
    speak("Do you want to play again? Say yes or no.")
    print("do you want to play again? Say yes or no.")
    again=listen()
    if again=="yes":
        swg()
    else:
        speak("Thanks for playing! Goodbye!")
        print("Thanks for playing! Goodbye!")
    


if __name__ == "__main__":
    swg()
    
    
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import pyautogui

recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wake_word():
 with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio).lower()
        except:
            return ""
if __name__ == "__main__":
    speak("Jarvis is running. Say hey jarvis to activate me.")
    
    while True:
        listen=wake_word()
        if "hey jarvis" in listen:
            print("Jarvis activated!")
            speak("I am awake! How can I help you?")
            while True:
                try:

                    command = wake_word()
                    print(f"You said: {command}")
                    if "open youtube" in command:
                        speak("Opening YouTube")
                        webbrowser.open("https://www.youtube.com")
                    elif "open google" in command:
                        speak("Opening Google")
                    elif "open whatsapp" in command:
                        speak("Opening WhatsApp")
                        os.system("start whatsapp://")
                    elif "open notepad" in command:
                        speak("Opening Notepad")
                        os.system("start notepad.exe")
                    elif"what time is it" in command:
                        from datetime import datetime
                        now = datetime.now().strftime("%H:%M")
                        speak(f"The time is {now}")
                    elif"take a screenshot" in command:
                        import pyautogui

                        screenshot = pyautogui.screenshot()
                        screenshot.save("screenshot.png")

                        speak("Screenshot taken and saved as screenshot.png")
                    elif "exit" in command or "quit" in command:
                        speak("Goodbye!")
                        break
                    else:
                        speak("Sorry, I didn't understand that command.")
                except sr.UnknownValueError:
                    speak("Sorry, I did not catch that. Please try again.")
                except sr.RequestError:
                    speak("Sorry, my speech service is down.")

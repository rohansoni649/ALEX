import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import ctypes

#to extract the current hour and wish accordingly
hour = datetime.datetime.now().hour
if hour>=0 and hour<12:
    pyttsx3.speak("Good Morning")
elif hour>=12 and hour<18:
    pyttsx3.speak("Good Afternoon")
else:
    pyttsx3.speak("Good Evening")

pyttsx3.speak("Hi I am Alex. How May I help you?")

def takeCommand():
    #it takes command from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        #r.pause_threshold = 1
        audio = r.listen(source)
#try-catch will be heplful if the voice is not properly heard by the API
    try:
        print("recognizing......")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception as e:
        print("Can you please say that again......")
        return "None"
    return query
    
if __name__ == "__main__":
    while True:
        #lower case will be taked into consideration for seaching results properly
        query = takeCommand().lower()
        
        #to search in wikipedia 
        if 'wikipedia' in query:
            pyttsx3.speak("Searching wikipedia....")
            #replace the wikipeadia keyword with the blank
            query = query.replace("wikipedia","")
            #extract 2 sentences from the wikipedia page summary
            results = wikipedia.summary(query, sentences=2)
            pyttsx3.speak("According to wikipedia....")
            print(results)
            pyttsx3.speak(results)
        #to open webbrowser
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            webbrowser.open('www.google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('www.stackoverflow.com')
            
        elif 'code' in query:
            #to open vscode program
            # // is used to eliminate any escape charcter (space in between)
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            elif 'how are you' in query:
            pyttsx3.speak("I am fine. Thank You!")
            pyttsx3.speak("How are you?")

        elif 'fine' in query or 'good' in query:
            pyttsx3.speak("It's good to know that you are fine")

        elif "what's your name" in query or "what is your name" in query:
            pyttsx3.speak("Everyone calls me Alex!")

        elif 'exit' in query:
            pyttsx3.speak("Thank you for me giving me your time.")
            pyttsx3.speak("Bye")
            exit()
        
        elif 'who created you' in query or 'who made you' in query:
            pyttsx3.speak("I have been created by Rohan Soni")
        
        #pyjoke is used to get eandom jokes  
        elif 'jokes' in query or 'joke' in query:
            #storing the joke in a variable to make it same for the whole condition
            joke = (pyjokes.get_joke())
            print(joke)
            pyttsx3.speak(joke)
            
            elif 'why you came to this world' in query:
            pyttsx3.speak("Thanks to Rohan. Rest is a secret")

        elif 'who are you' in query:
            pyttsx3.speak("I am Alex.A Virtual Assistant created by Rohan Soni")

        #to change the desktop background (using ctype libaray)
        elif 'change background' in query or 'change my desktop background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0,"C:\\Users\\hp\\Desktop\\Jarvis-The Windows Assistant\\2020-08-28 04.43.58 1.jpg",0)    

        #to lock the device (using ctype library)
        elif 'lock my window' in query or 'lock window' in query: 
            pyttsx3.speak("locking the device") 
            ctypes.windll.user32.LockWorkStation()

        #to empty recycle bin (using winshell library)
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            pyttsx3.speak("Recycle Bin Emptied")
            
            

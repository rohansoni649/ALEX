import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import ctypes
import winshell
import wolframalpha
import time
import subprocess
from twilio.rest import Client 
import speech_recognition as sr


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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rohansoni649@gmail.com', 'rohansoni9610509956') 
    server.sendmail('rohansoni649@gmail.com', to, content)
    server.close()
    
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
            
        elif 'play music' in query:
            music_dir = 'C:\\Users\\hp\\Downloads\\Music'
            #list the contents of the directory
            songs = os.listdir(music_dir)
            ##print(songs)
            #play the first content of the list
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif 'code' in query:
            #to open vscode program
            # // is used to eliminate any escape charcter (space in between)
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            elif 'how are you' in query:
            pyttsx3.speak("I am fine. Thank You!")
            pyttsx3.speak("How are you?")
            
        elif 'email to rohan' in query or 'mail to rohan' in query:
            try:
                pyttsx3.speak("What should I say in mail")
                content = takeCommand()
                to = "rohansoni649@gmail.com"
                sendEmail(to, content)
                pyttsx3.speak("Email has been sent")
            except Exception as e:
                print(e)
                pyttsx3.speak("Sorry Rohan...but I am not able to understand")

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
            
            #to hold the Alex for listening any commands (using time library)
        elif "don't listen" in query or "stop listening" in query: 
            pyttsx3.speak("For how much time you want to stop jarvis from listening commands: ")
            a = int(input("For how much time you want to stop Alex from listening commands (Enter the seconds): "))
            #a = int(takeCommand())
            #print(a)
            time.sleep(a)
            
            elif 'is love' in query:
            pyttsx3.speak("It's the 7th sense that destroys all the sense")
            
            #most asked question from wolframalpha (using wolframalpha library)
        elif "what is" in query or "who is" in query: 
            app_id = '84WKWE-Q7PYVH6EU5'
            client = wolframalpha.Client(app_id) 
            res = client.query(query)  
            try: 
                print (next(res.results).text) 
                pyttsx3.speak (next(res.results).text) 
            except StopIteration: 
                print ("No results")

        elif 'reason for you' in query or 'why you have been created'in query:
            pyttsx3.speak("I have been created for a big mission. I am been programmed not to harm any Human")
            pyttsx3.speak("May be!!")
            
            elif 'write a note' in query:
            pyttsx3.speak("What should I write in the note")
            note = takeCommand()
            # file handling (opening a file in writable format)
            file = open('note.txt','w')
            pyttsx3.speak("Should I include date and time")
            dt = takeCommand()
            if 'yes' in dt or 'sure' in dt or 'include it'in dt:
                srtTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(srtTime)
                file.write(" :- ")
                file.write(note)
                pyttsx3.speak('The note has been created')
            else:
                file.write(note)
                pyttsx3.speak('The note has been created')

        elif 'show notes' in query or 'show note' in query:
            pyttsx3.speak('Showing the notes')
            #file handling (openinng a file in readable format)
            file=open('note.txt','r')
            print(file.read())
        
        elif 'what can you' in query:
            pyttsx3.speak('Alex two point o at your service ')
            
            elif 'send an sms' in query or 'send a message' in query:   
            #(pip install twilio)
            # from twilio.rest import Client
            # Your Account Sid and Auth Token from twilio.com / console 
            account_sid = 'AC66c45659969349c3e90baa16bf59832d'
            auth_token = '3586f53e46d70a42b36b35795c90e399'

            client = Client(account_sid, auth_token) 

            ''' Change the value of 'from' with the number 
            received from Twilio and the value of 'to' 
            with the number in which you want to send message.'''
            pyttsx3.speak('What message you want to send.....')
            msg = takeCommand()
            message = client.messages.create(from_='+18182755710', body = msg, to ='+919610509956') 
            pyttsx3.speak("Message sent succesfully")
            print(message.sid) 

        elif 'I love you' in query:
            pyttsx3.speak("It is difficult to understand")

        elif 'the time' or 'current time' in query:
            #to extract the curren time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            pyttsx3.speak(f'The time is {strTime}')
            exit()
            

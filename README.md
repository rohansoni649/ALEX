# ALEX
Your own Genie which makes your Windows OS experience much easier.

__The Problem it Solves__

ALEX is a friendly voice assistant cum human which not only understands from the Technical aspect but also from Human feelings. It is a Windows OS manager that helps the user to automate their work by using voice commands. It can be helpful for new users to use the operating system without knowing any steps. It is also programmed for the kids to get the answers to the general knowledge-based question.
It makes it easier for the user to interact with their machine just by their voice.
Following are the key features of ALEX:
->Greets the user at the start of the program
->Provide the date and time when prompted 
->Search on Wikipedia 
->Open web browser and websites like Google, Youtube, StackOverflow when specified
->Open Music player and play songs when the user tells it to do
->Open code editor (VS_CODE)
->It has also make jokes if the users tell it 
->Windows feature like Emptying Recycle Bin, changing Desktop Background, Locking the device can be done with the voice commands
->Create a note (.txt file) and ask to add content with a date or not
->Accessible to send mail and text message to a phone just by mentioning the recipient and the body of the mail/message
->Able to answer general knowledge-based question and small math problems like the capital of Countries, squares of numbers, etc

**Challenges we ran into**

The most challenging phases for ALEX were:
1. Able to add the Wikipedia search query, it was not able to extract the correct keyword which needs to be searched. So We replace the Wikipedia word with a blank and the remaining word was that to be searched.
2. Sending mail was an easy task by using the SMTP library but connecting it with the voice was a little tedious task.
3. While adding the notes feature, we were trying to add a feature so that it also includes the time and date for the reminder. But we're not able to figure out the correct function in the date and time Library of the python. StackOverflow was a real helper in the situation.
4. Connecting the whole program with WolframAlpha API that helps to answer the general knowledge-based questions. Youtube tutorials were of great use in this hurdle.

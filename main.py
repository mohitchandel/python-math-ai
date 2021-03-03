import pyttsx3 

talk = pyttsx3.init()
voices = talk.getProperty('voices')
talk.setProperty('voice', voices[1].id)

talk.say("Hi, I am Math teaching AI assistant. Please enter your name") 
talk.runAndWait()
name = str(input("Your name: "))

talk.say( ("hello", name ,"Welcom to your maths table class, please select a number") )
talk.runAndWait()
num = int(input("Select a number less than 100: "))
count = 1

if num >100:
    talk.say("less than 100 is allowed only")
    talk.runAndWait()
else:
    while count <= 10:
        print(count,'X',num,"=",num*count)
        talk.say( (num,"multiply by",count,num*count) )
        talk.runAndWait()
        count+=1
import speech_recognition as sr
import pyttsx3
import csv
ans=[]

r=sr.Recognizer()


# Import the required module for text   
# to speech conversion 
def text_to_speech1():
    
    
  
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Hi! Our coronavirus disease self assessment scan has been developed on the basis of guidelines from the WHO and MHFW, Government of India. \n This interaction should not be taken as expert medical advice. Any information you share with us will be kept strictly confidential.') 
  
    # run and wait method, it processes the voice commands.  
    engine.runAndWait() 
def text_to_speech2():
    
    
  
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('How old are you?')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait() 
def text_to_speech3():
    
    
  
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('What is your gender? male or female')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait() 
    
def text_to_speech4():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Please let us know your current body temperature in degree Fahrenheit (Normal body temperature is 98.6°F): \n face yourself in the thermal camera')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
 
def text_to_speech5():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Are you experiencing any of the symptoms \n Please say yes or no accordingly')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
    
def text_to_speech6():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Dry Cough?')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait() 
    
def text_to_speech7():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Loss or diminished sense of smell')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
    
def text_to_speech7():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Sore Throat')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
    
def text_to_speech8():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Weakness')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
    
def text_to_speech9():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Additionally, please verify if you are experiencing any of the symptoms below \n Please say yes or no accordingly')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
    
def text_to_speech10():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Difficulty in Breathing :')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
    
def text_to_speech11():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Drowsiness')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()

def text_to_speech12():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Please provide your travel and exposure details \n Say yes or no')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()

def text_to_speech13():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('History of travel or meeting in affected geographical area in last 14 days :')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
    
def text_to_speech14():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Close Contact with confirmed COVID in last 14 days :')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
    
def text_to_speech15():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Do you have a history of any of these conditions Say yes or no')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
    
def text_to_speech16():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Diabetes,High Blood Pressure,Heart Disease,Kidney Disease')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
    
def text_to_speech_false():
    
    
  
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init() 
  
    # say method on the engine that passing input text to be spoken 
    engine.say('Your   response   is   not    correct \n Please respond to the question 2 to 3 seconds after the question is asked ')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
def speech_to_text():
    while(1):
        with sr.Microphone() as source:                                            
            print("Speak:")
            audio = r.listen(source)
        try:
            speechString =r.recognize_google(audio)
            parsedCommands = speechString.split(" ")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        response = parsedCommands[0]
        b=response
        return b

text_to_speech1()
text_to_speech2()##age
c=speech_to_text()
while not c.isdigit():
    text_to_speech_false()
    text_to_speech3()
    c=speech_to_text()
ans.append(c)
print(c)
text_to_speech3()##gender
c=speech_to_text()
while c!='female' and c!='mail':
    text_to_speech_false()
    text_to_speech3()
    c=speech_to_text()
if c=='mail':
    c='male'
ans.append(c)
print(c)

text_to_speech4()##temp
c=speech_to_text()
while not c.isdigit():
    text_to_speech_false()
    text_to_speech3()
    c=speech_to_text()
ans.append(c)
print(c)
text_to_speech5()
text_to_speech6()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech6()
    c=speech_to_text()
ans.append(c)
print(c)
text_to_speech7()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech7()
    c=speech_to_text()
ans.append(c)
print(c)
text_to_speech8()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech8()
    c=speech_to_text()
ans.append(c)
print(c)
text_to_speech9()
text_to_speech10()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech10()
    c=speech_to_text()
ans.append(c)
print(c)
text_to_speech11()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech11()
    c=speech_to_text()
ans.append(c)
print(c)
text_to_speech12()
text_to_speech13()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech13()
    c=speech_to_text()
ans.append(c)
print(c)
text_to_speech14()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech14()
    c=speech_to_text()
ans.append(c)
print(c)
text_to_speech15()
text_to_speech16()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech16()
    c=speech_to_text()
ans.append(c)

print(c)



print(ans)
with open(r'/home/pi/Desktop/dataframe.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(ans)
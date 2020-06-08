import speech_recognition as sr
import pyttsx3
import csv
ans=[]
recognizer = sr.Recognizer()


def Recog(recognizer, Microphone):
    while(1):
        speech = sr.Microphone()
        with speech as source:
            print("speak:")
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        response = {
         "success": True,
         "error": None,
         "transcription": None
        }

#     # try recognizing the speech in the recording
#     # if a RequestError or UnknownValueError exception is caught,
#     #   update the response object accordingly
        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
         # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable/unresponsive"
        except sr.UnknownValueError:
         # speech was unintelligible
            response["error"] = "Unable to recognize speech"
        return response
def speech_to_text():
    
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    response = Recog(recognizer, mic)
    b=response['transcription']
    return b

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
    engine.say('Please answer the questions below in \nyes or no ')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
   
def text_to_speech3():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init()
 
    # say method on the engine that passing input text to be spoken
    engine.say('Are you experiencing any of the symptoms \nFever\nDiarhea\nLoss of smell or taste\n cough or sore throat \n breathing difficulty or sob ')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
   
def text_to_speech4():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init()
 
    # say method on the engine that passing input text to be spoken
    engine.say('Do you have any History of travel in public transport like flight or train or bus recently')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
   
def text_to_speech5():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init()
 
    # say method on the engine that passing input text to be spoken
    engine.say('Did you have any contact with positive case or their contacts')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
   
def text_to_speech6():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init()
 
    # say method on the engine that passing input text to be spoken
    engine.say('Did you recently attended a gathering or a crowd')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
   
def text_to_speech7():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init()
 
    # say method on the engine that passing input text to be spoken
    engine.say('Did you have any exposure to the containment area')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
   
def text_to_speech8():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init()
 
    # say method on the engine that passing input text to be spoken
    engine.say('Were you tested for covid before')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
   
def text_to_speech9():
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init()
 
    # say method on the engine that passing input text to be spoken
    engine.say('Does anyone from your family have any symptoms')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
 
 
   
def text_to_speech_false():
   
   
 
    # init function to get an engine instance for the speech synthesis  
    engine = pyttsx3.init()
 
    # say method on the engine that passing input text to be spoken
    engine.say('Your   response   is   not    correct \n Please respond to the question 2 to 3 seconds after the question is asked ')
    # run and wait method, it processes the voice commands.  
    engine.runAndWait()
   
r=sr.Recognizer()
x=0
y=0
ans=[]
text_to_speech1()
text_to_speech2()
text_to_speech3()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech3()
    c=speech_to_text()
if c=='yes':
    x=1
ans.append(c)
print(c)
 
text_to_speech4()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech4()
    c=speech_to_text()
if c=='yes':
    y=1
ans.append(c)
print(c) 
text_to_speech5()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech5()
    c=speech_to_text()
if c=='yes':
    y=1
ans.append(c)
print(c) 
 
text_to_speech6()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech6()
    c=speech_to_text()
if c=='yes':
    y=1
ans.append(c)
print(c) 
 
text_to_speech7()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech7()
    c=speech_to_text()
if c=='yes':
    y=1
ans.append(c)
print(c) 
text_to_speech8()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech8()
    c=speech_to_text()
if c=='yes':
    y=1
ans.append(c)
print(c) 
text_to_speech9()
c=speech_to_text()
while c!='yes' and c!='no':
    text_to_speech_false()
    text_to_speech9()
    c=speech_to_text()
if c=='yes':
    y=1
ans.append(c)
print(c) 
if x==0 and y==0:
    ans.append('Green')
    ans.append('Clear History')
elif x==1 and y==1:
    ans.append('Red')
    ans.append('Covid Suspect')
else:
    ans.append('Yellow')
    ans.append('Suspected History')
print(ans)
 
         

       

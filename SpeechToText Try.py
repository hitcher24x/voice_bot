import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Hey Badi Say Something!')
    audio = r.listen(source)

try:
    print('GoogleThinks you said:\n' + r.recognize_google(audio))

except:
    pass


import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print('Say something...')
    audio = r.listen(source)

query = r.recognize_google(audio, language='ru-RU')
print('You said: ' + query.lower())
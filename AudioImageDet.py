"""AudioImageDet.py Module: """

# Imports
import cv2
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

try:
    print("You said: " + r.recognize_google(audio))
except Exception as e:
    print(e)

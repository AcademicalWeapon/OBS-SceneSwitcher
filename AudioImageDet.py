"""AudioImageDet.py Module: """

import cv2
import speech_recognition as sr
import SceneSwitch

# Sets the Microphone up
r = sr.Recognizer()


def LoadKeywords(file_path):
    """Loads the keywords.txt File containing the Keywords. (Custom keywords can be added in the keywords.txt file)"""
    with open(file_path, 'r') as file:
        keywords = [line.strip() for line in file.readlines()
                    if not line.startswith('#')]
    return keywords


def AudioDetection(keywords):
    """Function listens to audio to detect certain keywords"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        while True:
            try:
                audio = r.listen(source)
                recognized_text = r.recognize_google(audio)
                print("Detected: " + recognized_text)
                for keyword in keywords:
                    if keyword.lower() in recognized_text.lower():
                        SceneSwitch.SwitchScene("STANDBY")
                        break
                else:
                    print("No keywords mentioned.")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {0}".format(e))

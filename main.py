# This is a sample Python script.
import speech_recognition as sr
import pocketsphinx as ps
import pyaudio as pa

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    #Sample code below edit to customize
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("start")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

        try:
            data = r.recognize_google(audio)
            print(data)
        except:
            print("Please try again")
    #Code above here is sample
    #Test ssh key

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


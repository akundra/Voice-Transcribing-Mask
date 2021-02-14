# This is a sample Python script.
import speech_recognition as sr


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    #Sample code below edit to customize
    r = sr.Recognizer()

    with sr.Microphone(sample_rate=44100, device_index=2) as source:
        #r.adjust_for_ambient_noise(source, duration=1)
        print("start")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

        try:
            data = r.recognize_sphinx(audio)
            print(data)
        except sr.UnknownValueError:
            print("Sphinx could not understand")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
    #Code above here is sample
    #Test ssh key

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


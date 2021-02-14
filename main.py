# This is a sample Python script.
import speech_recognition as sr
import contextlib3


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Error handling for ALSA errors
@contextlib3.contextmanager
def noalsaerr():
    try:
        asound - cdll.LoadLibrary('libasound.so')
        asound.snd_lib_error_set_handler(c_error_handler)
        yield
        asound.snd_lib_error_set_handler(none)
    except:
        pass
#

def main():
    # Use a breakpoint in the code line below to debug your script.

    r = sr.Recognizer()

    with noalsaerr() as n:
        with sr.Microphone(sample_rate=44100, device_index=2) as source:
            # r.adjust_for_ambient_noise(source, duration=1)
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




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


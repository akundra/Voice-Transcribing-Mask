# This is a sample Python script.
import speech_recognition as sr
import pyaudio
from ctypes import *
from contextlib3 import contextmanager

"""
#Begin error handling for pyaudio

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.sn_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)

#End Error Handling for pyaudio
"""
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def main():
    # Use a breakpoint in the code line below to debug your script.

    r = sr.Recognizer()


#    with noalsaerr(), \
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


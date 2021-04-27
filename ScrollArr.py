import sys
from luma.core.interface.serial import spi
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1322
import time
from PIL import ImageFont
from luma.core.bitmap_font import bitmap_font
from io import BytesIO

serial = spi(device=0, port=0)
device = ssd1322(serial)


# getBuffer()
#
# description: This function takes the stdin from the command line and stores it in an array.
#
#
# arguments: buffArr (string array): An array of strings written to and updated by the
#                                    voice recognition software.
#            i (int): The string postion within the imported buffer array buffArr. The
#                     NewData flag & end of previous buffer triggers i += 1 externally.
#
# returns: The new buffer of type string

def getBuffer():
    buffer = input()

    return buffer


# getFont()
#
# description: This function reads any trutype font seeded in the same directory
#              as the program and outhputs an ImageFont object which can be used
#              in drawng to the screen. Font size is also adjustale. Default
#              argument values are currently set.
#
# arguments: fontType: A truetype font file (.ttf) to be used with luma.oled
#                      library draw.text() method.
#            fontSize : This parameter contorls the physcial size of text on the
#                      screen. Should range from 20-40. The smaller, the harder
#                      to read. The larger the higher latency. Experiment for
#                      optimization.
#
# returns:   font: An ImageFont object.

def getFont(fontType="News Gothic MT Regular.ttf", fontSize=35):
    file = open(fontType, "rb")
    bytes_font = BytesIO(file.read())
    font = ImageFont.truetype(bytes_font, fontSize)
    file.close()

    return font


# getString()
#
# description: This function takes the buffer and chunks it into a string of set
#              length. An input parameter for start postion in buffer will be
#              passed in and handled from external code.
#
# arguments:   i (int): The postion in the current buffer. Kept track of externally.
#              buffer (string): The current buffer as a singular string value
#              chunklen (int): The length of the chunk to be scrolled across the buffer.
#                              Physically, this must be equal to or longer than the screen
#                              length.
#
# returns:     A string of length chunklen to be used in text scrolling

def getString(i, buffer, chunklen):
    try:
        string = buffer[i]
    except:
        print("Buffer ends1")
        return ""

    j = i + chunklen  # to consolidate, j could be called chunklen

    while i < j - 1:  # add chunklen to range
        try:
            string += buffer[i + 1]
        except:
            print("Buffer ends2")
            return string  # buffer ended, return the string
        i += 1

    return string


# textScroll()
#
# description: This function is called once in main() to scroll the text. It is
#              the culminating function that ties together the others into a
#              cohesive flow.
#
# arguments: --
#
# returns: --

def textScroll():
    x, y = 264, 15

    sleepMode = False  # this is the flag that sets screen to optimize power consumption
    # sleep mode called when string1 < chunklength && x == -string1len (from ImageDraw module)
    font = getFont()

    chunklen = 18  # sets length of text chunking (can experiment with smoothness: the smaller the faster)
    chunks = 100  # sets number of max chunks
    # maxbuff = chunks * chunklen  # use later for testing if last buffer

    # file = open("words.txt", "r")  # open file ONCE before while loop
    buffer = getBuffer()

    sloop = 0  # string looper to obtain strings from buffer
    newBuf = False  # only matters at second new buff

    string1 = getString(sloop, buffer, chunklen)  # get first string from buffer
    sloop += len(string1)  # could be chunklen + 1

    string2 = getString(sloop, buffer, chunklen)  # get second string from buffer
    sloop += len(string2)

    string = string1 + string2  # concatenate strings for smooth scrolling

    print(string)

    print(string2)

    while not sleepMode:

        with canvas(device) as draw:

            draw.text((x, y), string, fill=None, font=font)

        s1len, s1high = draw.multiline_textsize(string1, font=font)

        x -= 4

        if x <= -s1len:

            # Check if when s1 scrolls off if there is no more incoing string data
            if string2 == "\n":
                deltaBuf = False  # to calculate a change in buffer
                ts = time.perf_counter()  # set present time

                # Try to get new form of buffer or new buffer until file is changed, then use buffer
                while not deltaBuf:
                    prevbuffer = buffer
                    newbuffer = getBuffer()
                    tp = time.perf_counter() - ts  # difference between present time and start of no text
                    # print(tp)
                    # if tp >= 10:
                    # clear buffer
                    # search new
                    # if not found in 1 minute, exit program?
                    # get new buffer
                    # signal jump out

                    if newbuffer != "":
                        deltaBuf = True
                        buffer = prevbuffer + newbuffer  # append new words to previous buffer for new buffer
                        print(sloop)
                        print(prevbuffer)
                        string1 = getString(sloop, buffer, chunklen)
                        sloop += len(string1)
                        string2 = getString(sloop, buffer, chunklen)
                        sloop += len(string2)
                        print(string1)
                        print(string2)
                        newBuf = True
                print("reached")

            if len(string1) < chunklen:
                if newBuf:
                    newBuf = False
                    x = 264
                else:
                    string1 = string2
                    x = 0
                string2 = "\n"
                string = string1  # dont calculate OR add another string cuz end.
            else:
                if newBuf:  # Let's bypass normal operations coming out of finding new buffer.
                    newBuf = False
                    string = string1 + string2
                    x = 264
                else:
                    string1 = string2
                    string2 = getString(sloop, buffer, chunklen)
                    sloop += len(string2)
                    string = string1 + string2
                    x = 0  # Reset

            print(string)
            print(len(string1))
            print(len(buffer))

    # file.close()

    return


def main():
    for line in sys.stdin:
        if 'start_transcribe' == line.rstrip():
            break
    textScroll()


if __name__ == "__main__":
    main()

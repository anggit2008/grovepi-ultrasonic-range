from grovepi import *
#unwanted

ultra = 6

while 1:

    val = ultrasonicRead(ultra)

    if val >= 3:

        if val <= 10:

            print "in range"

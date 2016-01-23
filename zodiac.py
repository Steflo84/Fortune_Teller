#!/user/bin/python
import random

#  _____                            _
# / ____|                          | |
#| |     ___  _ __ ___  _ __  _   _| |_ ___ _ __
#| |    / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__|
#| |___| (_) | | | | | | |_) | |_| | ||  __/ |
# \_____\___/|_| |_| |_| .__/_\__,_|\__\___|_|
#     /\       | |     | |   | |
#    /  \   ___| |_ _ _|_|__ | | ___   __ _  ___ _ __
#   / /\ \ / __| __| '__/ _ \| |/ _ \ / _` |/ _ \ '__|
#  / ____ \\__ \ |_| | | (_) | | (_) | (_| |  __/ |
# /_/    \_\___/\__|_|  \___/|_|\___/ \__, |\___|_|
#                                      __/ |
#                                     |___/

#Author: Jeremiah Milbauer
#Version: 1.10.2016

#Created for the CMSC 16200 Wiki at the University of Chicago

#handle potential errors with the string.

# getMonth (String) -> Int
def getMonth(dStr):
    month = dStr[0:2]
    return int(month)

# getDay (String) -> Int
def getDay(dStr):
    day = dStr[3:5]
    return int(day)

# getYear :: (String) -> Int
def getYear(dStr):
    year = dStr[6:]
    return int(year)

# getSign :: (Int, Int, String) -> String
def getSign(m, d, s):
    if s == "Astrology":
        sign = getAstrologySign(m, d)
    else:
        sign = "Undetermined"
    return sign

# getSign :: (Int, Int) -> String
def getAstrologySign(m, d):
    if m == 1: #January
        if d < 20:
            sign = "Capricorn"
        else:
            sign = "Aquarius"
    elif m == 2: #February
        if d < 19:
            sign = "Aquarius"
        else:
            sign = "Pisces"
    elif m == 3: #March
        if d < 20:
            sign = "Pisces"
        else:
            sign = "Aries"
    elif m == 4: #April
        if d < 20:
            sign = "Aries"
        else:
            sign = "Taurus"
    elif m == 5: #May
        if d < 21:
            sign = "Taurus"
        else:
            sign = "Gemini"
    elif m == 6: #June
        if d < 21:
            sign = "Gemini"
        else:
            sign = "Cancer"
    elif m == 7: #July
        if d < 23:
            sign = "Cancer"
        else:
            sign = "Leo"
    elif m == 8: #August
        if d < 23:
            sign = "Leo"
        else:
            sign = "Virgo"
    elif m == 9: #September
        if d < 23:
            sign = "Virgo"
        else:
            sign = "Libra"
    elif m == 10: #October
        if d < 23:
            sign = "Libra"
        else:
            sign = "Scorpio"
    elif m == 11: #November
        if d < 22:
            sign = "Scorpio"
        else:
            sign = "Sagittarius"
    elif m == 12: #December
        if d < 22:
            sign = "Sagittarius"
        else:
            sign = "Capricorn"
    else:
        sign = "Undetermined"
    return sign

# getFortune :: (String) -> String
def getFortune(s):
    filename = s.lower() + "fortunes.txt"
    fortuneFile = open(filename)
    fortunes = fortuneFile.read().splitlines()
    index = random.randrange(0, len(fortunes), 1)
    fortune = fortunes[index]
    return fortune

decorationString = "~*~*~"
decoration = " " + decorationString + " "
titleString = """
  _____                            _
 / ____|                          | |
| |     ___  _ __ ___  _ __  _   _| |_ ___ _ __
| |    / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__|
| |___| (_) | | | | | | |_) | |_| | ||  __/ |
 \_____\___/|_| |_| |_| .__/_\__,_|\__\___|_|
     /\       | |     | |   | |
    /  \   ___| |_ _ _|_|__ | | ___   __ _  ___ _ __
   / /\ \ / __| __| '__/ _ \| |/ _ \ / _` |/ _ \ '__|
  / ____ \\\__ \ |_| | | (_) | | (_) | (_| |  __/ |
 /_/    \_\___/\__|_|  \___/|_|\___/ \__, |\___|_|
                                      __/ |
                                     |___/
"""#there's a pretty nasty esape character in there so it looks offset in the source code.

def repl():
    #READ
    print "Press enter 'q' to quit."
    print "Please enter your birthday. mm/dd/yyyy"
    birthday = raw_input("> ")
    if birthday == "q":
        quit()

    #EVAL
    system = "Astrology"
    month = getMonth(birthday)
    day = getDay(birthday)
    year = getYear(birthday)
    sign = getSign(month, day, system)
    fortune = getFortune(sign)

    #PRINT
    print "\nBecause you were born %s/%s/%s," % (month, day, year),
    print "Your " + system + " sign is %s." % sign
    print "Your fortune is: \n"
    print decoration + fortune + decoration + "\n"

    #LOOP
    repl()

def main():
    print "\n" * 10
    print "Welcome to the:"
    print titleString
    repl()

main()

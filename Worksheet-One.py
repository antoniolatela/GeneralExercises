import time
import sys

class fontcolor:
    green = '\033[93m'
    answer = '\033[95m'
    stdout = '\033[0m'



class WS_O:

    def __init__ (self):
        None

    def printfun (self, *args):
        for i in args:
            for i in i:
                sys.stdout.write (i)
                sys.stdout.flush()
                time.sleep(0.02)
            print (end=' ')
        print(end='\n')

    def one(self):
        q = fontcolor.green + "In a print statement, what happens if you " \
                              "leave out one of the parentheses, or both?" + fontcolor.stdout
        a = fontcolor.answer + "Get an error." + fontcolor.stdout
        self.printfun(q, a)

    def two(self):
        q = fontcolor.green + "If you are trying to print a string, what happens " \
                              "if you leave out one of the quotation marks, or both?" + fontcolor.stdout
        a = fontcolor.answer + "Get an error." + fontcolor.stdout
        self.printfun(q, a)

    def three(self):
        q = fontcolor.green + "You can use a minus sign to make a negative number like -2. " \
                              "What happens if you put a plus sign before a number? What about 2++2?" + fontcolor.stdout
        a = fontcolor.answer + "Get {0}".format(str(int(2++2))) + fontcolor.stdout
        self.printfun(q, a)

    def four(self):
        q = fontcolor.green + "In math notation, leading zeros are ok, as in 02. What happens if you try this in " \
                              "Python?"+ fontcolor.stdout
        a = fontcolor.answer + "Get an error." + fontcolor.stdout
        self.printfun(q, a)

    def five(self):
        q = fontcolor.green + "What happens if you have two values with no operator between them?"+ fontcolor.stdout
        a = fontcolor.answer + "Get an error." + fontcolor.stdout
        self.printfun(q, a)

    def six (self, hh, min, sec):
        q = fontcolor.green + "How many seconds are there in {0} hours, {1} minutes {2} seconds?".format(hh, min, sec)+ fontcolor.stdout
        a = fontcolor.answer + "{0} seconds.".format(str(int(hh * 3600 + min * 60 + sec))) + fontcolor.stdout
        self.printfun(q, a)

    def seven(self, km):
        q = fontcolor.green + "How many miles are there in {} kilometres? Hint: there are 1.61 kilometres in a mile.".format(km)+ fontcolor.stdout
        a = fontcolor.answer + "{0} Miles.".format(str(round(km/1.61, 2))) + fontcolor.stdout
        self.printfun(q, a)

WS_O().seven(10)
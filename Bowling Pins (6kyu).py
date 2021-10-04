# https://www.codewars.com/kata/585cf93f6ad5e0d9bf000010/train/python

def bowling_pins(arr) :
    pins = "{7} {8} {9} {10}\n" + \
            " {4} {5} {6}\n" + \
             "  {2} {3}\n" + \
               "   {1}   "

    return pins.format(*(" " if i in arr else "I" for i in range(11)))

print(bowling_pins([5]))
# I I I I
#  I   I
#   I I
#    I
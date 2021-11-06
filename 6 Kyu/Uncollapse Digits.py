# https://www.codewars.com/kata/5a626fc7fd56cb63c300008c/train/python

def uncollapse(digits):
    # The library of string that we want to add space between
    dig = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    # Loop through all of the string to find matching string from the library
    for word in dig :
        # Add space after we find same string from the library
        digits = digits.replace(word, word + " ")

    # Excluding the last space on the string using [:-1]
    return digits[:-1]

"""
Example : threetwoone
we have dig variable as a library on what string to find

by using 
for word in dig

we can find same string in dig and add space after it
with .replace(before, after) we can replace the value with new value

in this case we want to add space after the value so we using word + " "
so the string become -> 'three two one '
notice at the end of the string theres a space

so we will return string[:-1] to exclude the space at the end
"""
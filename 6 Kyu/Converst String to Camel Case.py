# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

def to_camel_case(text):
    #replace '-' between word to '_' and split the word with '_' as the seperator
    text = text.replace("-","_").split("_") 

    # Capitalized each word, except the first word
    for i in range (1,len(text)) :
        text[i] = text[i].capitalize()

    # Return all text in list to become one string
    return ''.join(text)
    
"""
Example we have : the_stealth-warrior
by using .replace('-', '_') text become -> 'the_stealth_warrior
next, we use .split('_') to split the text to -> ['the', 'stealth', 'warrior']

We want to capitalized the all the words except the 1st word
so we use range (1, len(text) so the index start from 1
and we caplitalized using .capitalize() function

Return using ''.join(text) to put all the text into one line of string instead of list
"""
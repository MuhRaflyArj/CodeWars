# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    return len(set(i for i in text.lower() if text.lower().count(i) > 1))

"""
Example : abcdeaB
we want to count how many value that occur more than once in a string
first of all we want to string to be lowercase, so we use .lower()

we want to make a set (so theres no duplicate) for value that occur more than once
so we use i for i text.lower() if text.lower().count(i) > 1

i for i text.lower(), so i is assign to every value in string and 
if there any uppercase in the string, it will turn into lowercase

if text.lower().count(i) > 1, so we only return i that occur more than 1 time
using .count() function

since we have set, we dont have duplicate value

we return the length of the set as the answer, 
cause it only asked how many value that occur more than once
"""

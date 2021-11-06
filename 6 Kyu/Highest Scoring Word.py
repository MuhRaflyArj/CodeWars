# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

def high(x):
    # The Library for alphabeth, index as score for every alphabeth
    # x.split so each word become a value in a list
    alphabeth, x = "abcdefghijklmnopqrstuvwxyz", x.split()


    count = [0] * len(x) # Declare 0 as many words at x

    # Loop through every value in list x
    for i in range (len(x)) :
        for char in x[i] :
            # Add score to list count, the count index correspond to index at x
            count[i] += (alphabeth.index(char) + 1)
    print(count)
    # new Var called a, to rank the score of each word
    a = sorted(count)

    # From var a, we can find which word have highes score
    # And then trace back the index using .index()
    return x[count.index(a[-1])]

print(high('man i need a taxi up to ubud'))

"""
Example : man i need a taxi up to ubud
using .split() we have -> ['man', 'i', 'need', 'a', 'taxi', 'up', 'to', 'ubud']
using 'for i in range(len(x))' loop, we loop through every value in x

'for char in x[i]' is used to loop every character in a value
using the .index() function we can ouput the character index at alphabeth as a score

we have list called count, and after the loop we have 
count = [28, 9, 28, 1, 54, 37, 35, 48]
the index at count represent the score of word in var x

so we know that 'need' have 28 score, because 'need' is placed at index no 2
and index no 2 at count have value 28, from this we can find highest score using sorted()

a new var called a is declared which contain sorted value of count

from this we can find at which index biggest value at count which correspond to index at x
using .index() we can find which index highest score at and return that index in var x
"""
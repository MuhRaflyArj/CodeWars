# https://www.codewars.com/kata/60a1aac7d5a5fc0046c89651/train/python

def last_survivors(string):
    alphabeth = list(map(chr, range(97, 123))) # all letters in alphabeth
    alphabeth.append('a') # append the fist letter
    res = [i for i in string] # List of individual character of string

    # Loop as many times as length of string   
    for f in range (len(string)) :      
        for item in res :

            # If a value in string equal or more than 2
            if res.count(item) >= 2 :

                itemIndex = alphabeth.index(item) # Index of alphabeth

                # Remove the value 2 times              
                res.remove(item); res.remove(item)

                # Add new value which Index of alphabeth + 1 (the letter after)          
                res.append(alphabeth[itemIndex+1])

    # Sort the value in alphabetical order
    res = sorted(res)            
    return ''.join(res) # Join all of the value in res as a one string

"""
Example : zzzab
using .count() we know that z have appear 3 times in the string

with .index() we know what index of z is, and we can delete two z
and input new value which is letter after z, in this case we go back to letter a

so the string become azab
because of the loop, we know that we have two a letter and delete those two a letter
and replace it with b

now we have cz
because theres no letters that have appear two times or more, that is the final output
"""
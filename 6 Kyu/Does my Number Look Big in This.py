# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

def narcissistic( value ):
    return sum(int(i)**len(str(value)) for i in str(value)) == value

"""
Example = 371
using int(i) for in in str(value) we have a list that consist of every digit in the value
Convert it to string so it can be iterate and assign it to integer of the single digit

now we have [3, 7, 1]

using '**len(str(value)' we multitply every value by the length of string value
in this case the length is 3

so now we have [3**3, 7**3, 1**3] which equal to [9, 343, 1]
if the sum of the list is equal to the value at beggining the number is narcissistic

in this case 9 + 343 + 1 is equal to 371

so we return the value of summerized value of the list is equal to value (sum(list) == value)
which will return of boolean, which in this case is True
"""

# https://www.codewars.com/kata/566fc12495810954b1000030/train/python

def nb_dig(n, d):
    return ''.join([str(i**2) for i in range(n+1) if str(d) in str(i**2)]).count(str(d))

"""
For example : n = 10, d = 1

'for i in range(n+1)' is to print all of the digit from 0 to n
so we got -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
but the i is squared (i**2) so the list is -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

by using 'if str(d) is in str(i**2) to filter if there any 1 in the value
(convert it to string so it can see it digit by digit)
so now we got ['1', '16', '81', '100'] because there's 1 in every value

by using ''.join, the value become a string '11681100'
from there we can count how many '1' is appear in the string using .count()
and return the .count() as the answer
"""
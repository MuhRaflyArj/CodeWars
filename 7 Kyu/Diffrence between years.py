# https://www.codewars.com/kata/588f5a38ec641b411200005b/train/python

def how_many_years (date1,date2):
    return abs(int(date1.split("/")[0])-int(date2.split("/")[0]))

"""
Example : 
date1 = '1997/10/10'
date2 = '2015/10/10'

Split date 1 and 2 and take the first value with .split()[0]
and convert it to integer

now we have date1 = 1997, date2 = 2015

(date1 - date2) to know the difference -> (1997 - 2015)
which equal to -18

use abs() to make the result positive
so the final result is 18
"""


# https://www.codewars.com/kata/5f47e79e18330d001a195b55

def base_finder(seq):
    return len(set(''.join(seq)))

"""
Example : [ "1", "2", "3", "4", "5", "6", "10", "11", "12", "13" ]
''.join() to put together into one string -> '12345610111213'

set() to eleminate duplicate -> {'5', '1', '3', '0', '6', '4', '2'}

len() to return length of the set -> 7
so the list above have 7 different basis
"""

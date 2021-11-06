# Delete occurrences of an element if it occurs more than n times
# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

def delete_nth(order,max_e):
    res = []
    for num in order:
        if max_e > res.count(num): 
            res.append(num)
    return res
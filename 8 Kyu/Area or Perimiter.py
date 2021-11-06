# https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python

def area_or_perimeter(l , w):
    return l * w if l == w else l*2 + w*2

"""
If the value of l and the value of w is equal, we should return area
which the formula is l * w

if the valure of l and the value of w is NOT equal, we should return the perimeter
which the formula is l*2 + w*2
"""
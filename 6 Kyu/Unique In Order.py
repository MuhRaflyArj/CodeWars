# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(iterable):
    iterable = [i for i in iterable]; iterable.append(" ")
    res = [iterable[i-1] for i in range (1, len(iterable)) if iterable[i-1] != iterable[i]]
    return res
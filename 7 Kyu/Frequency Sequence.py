# https://www.codewars.com/kata/585a033e3a36cdc50a00011c/train/python

def freq_seq(s, sep):
    return sep.join([str(s.count(i)) for i in s])
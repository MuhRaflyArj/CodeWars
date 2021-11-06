# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
    return ''.join([i.replace(i, ")") if word.lower().count(i) > 1 else i.replace(i, "(") for i in word.lower()])
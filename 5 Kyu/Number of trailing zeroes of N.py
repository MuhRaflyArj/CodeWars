# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python

def zeros(n):
    res, i = 0, 1
    while (n > 0) and (n/(5**i) >= 1):
        res += int(n/(5**i)); i += 1
    return res
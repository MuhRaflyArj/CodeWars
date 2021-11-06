# https://www.codewars.com/kata/56b3b27cadd4ad275500000c/train/python

def word_count(s):
    exc = ["a", "the", "on", "at", "of", "upon", "in", "as"]
    alphabeth = "abcdefghijklmnopqrstuvwxyz "
    for char in s.lower() :
        if char not in alphabeth : s = s.replace(char, " ")
    return len([i for i in s.lower().split() if i not in exc])
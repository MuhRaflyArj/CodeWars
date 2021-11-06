# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

def is_pangram(s):
    alphabeth = "abcdefghijklmnopqrstuvwxyz"
    return len(set([i for i in s.lower() if i.lower() in alphabeth])) == 26
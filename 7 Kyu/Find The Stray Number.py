# https://www.codewars.com/kata/57f609022f4d534f05000024/train/python

def stray(arr):
    return ([i for i in arr if arr.count(i) == 1])[0]

"""
By using list comperhension we can find which value that only appear once in the list

since there's only one value in the list we can return it as integer by ([])[0]
"""
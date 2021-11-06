# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

def sort_array(source_array):
    odd_array = sorted([i for i in source_array if i % 2 == 1], reverse=True)
    return [i if i % 2 == 0 else odd_array.pop() for i in source_array]
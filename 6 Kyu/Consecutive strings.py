# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

def longest_consec(strarr, k):
    if len(strarr) <= 0 or k <= 0 or k > len(strarr) : return ""
    arr = []
    a, b = k, 0
    while a != len(strarr)+1 :
        array = []
        for i in range (b, a) :
            array.append(strarr[i])
            
        arr.append(''.join(array))
        a += 1; b += 1
    length = [len(i) for i in arr]
    return arr[length.index(max(length))]
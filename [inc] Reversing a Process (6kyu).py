# https://www.codewars.com/kata/5dad6e5264e25a001918a1fc/train/python
"""
Tidak dapat menemukan "Impossible to decode"
"""

def decode(r):
    alphabeth = "abcdefghijklmnopqrstuvwxyz"
    num,res, endRes = [], [], []

    for char in r :
        if char not in alphabeth :
            num.append(char)
        else :
            res.append(char)
    num = int(''.join(num))

    for char in res :
        index = alphabeth.index(char)
        i = 0
        formula = i * num % 26
        while formula != index :

            formula = i * num % 26
            i += 1
        if i == 0 :
            endRes.append(alphabeth[i])
        else :
            endRes.append(alphabeth[i-1])

    print(len(res), len(endRes))
    return ''.join(endRes)


print(decode("761328qockcouoqmoayqwmkkic"))
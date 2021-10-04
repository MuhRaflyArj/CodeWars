# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
def high(x):
    alphabeth, x = "abcdefghijklmnopqrstuvwxyz", x.split(),
    count = [0] * len(x)
    for i in range (len(x)) :
        for char in x[i] :
            count[i] += (alphabeth.index(char) + 1)

    a = sorted(count)
    return x[count.index(a[-1])]


print(high('what time are we climbing up the volcano')) # volcano
print(high('man i need a taxi up to ubud')) #taxi
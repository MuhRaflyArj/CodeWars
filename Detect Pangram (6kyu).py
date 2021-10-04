# https://www.codewars.com/kata/5a626fc7fd56cb63c300008c/train/python

def uncollapse(digits) :
    dig = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    res, resAppend = [], []

    for i in range (len(digits)) :       
        if (''.join(resAppend)) in dig :
            res.append(str(''.join(resAppend)))
            resAppend.clear(); resAppend.append(digits[i])            
        else :
            resAppend.append(digits[i])
    
    res.append(str(''.join(resAppend)))
    return " ".join(res)
    


print(uncollapse("sevenzeroseventwosixfive")) #seven zero seven two six five
print(uncollapse("onethreefourfiveeighttenoneseven")) #one three four five eight ten one seven
print(uncollapse("threefivetwoninezerozeroonethreesix")) #three five two nine zero zero one three six
print(uncollapse("zeroeightseveneighttwofivefivetwozeronineninenine")) #zero eight seven eight two five five two zero nine nine nine
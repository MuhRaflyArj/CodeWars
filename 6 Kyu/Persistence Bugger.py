# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

def persistence(n):   
    count, numList, res = 0, [], 1
    while True :      
        strN = str(n)

        if len(strN) == 1 :
            break

        for i in range(len(strN)) :
            numList.append(int(strN[i]))
        for j in numList :
            res = res * j  
              
        n = res; count += 1   
    return count
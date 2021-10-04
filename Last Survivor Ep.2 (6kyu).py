# https://www.codewars.com/kata/60a1aac7d5a5fc0046c89651/train/python

def last_survivors(string):
    alphabeth = list(map(chr, range(97, 123)))
    alphabeth.append('a')
    res = []
    
    for char in string :
        res.append(char)
       
    for f in range (len(string)) :      
        for item in res :
            if res.count(item) >= 2 :
                itemIndex = alphabeth.index(item)               
                res.remove(item); res.remove(item)          
                res.append(alphabeth[itemIndex+1])

    res = sorted(res)            
    return ''.join(res)
    
    


print(last_survivors("abzz"))
# c
print(last_survivors("zzzba"))
# cz
print(last_survivors("xsdlafqpcmjytoikojsecamgdkehrqqgfknlhoudqygkbxftivfbpxhxtqgpkvsrfflpgrlhkbfnyftwkdebwfidmpauoteahyh"))
# acdeghlmnqrvyz
# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
def duplicate_count(text):
    res, count = [], 0
    for item in text :
        if item.isupper() :
            res.append(item.lower())
        else :
            res.append(item)
    res = sorted(res)
    for item in res :
        for item in res : 
            if res.count(item) > 1 :
                for i in range (res.count(item)) :
                    res.remove(item)
                count += 1
    return count
     
print(duplicate_count("xQmHxHB79JdSjVjScRhksFmFEzc0QoXYEx1YzzrHtzKN8Y3e41")) # 14
print(duplicate_count("Indivisibilities")) # 2
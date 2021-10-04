def duplicate_count(text):
    res, count = [], 0
    for item in text :
        res.append(item)
    
    for item in res :
        if item.isupper() :
            res.append(item.lower())
    res = sorted(res)
    print(res)
    for item in res :
        if res.count(item) > 1 :
            for i in range (res.count(item)) :
                res.remove(item)
            count += 1
    return count
     
print(duplicate_count("DMSokgXGG7ZeHeCtCuXmB6XIycbJ0QMpLZSx66ZghiFBnzt2xJ"))
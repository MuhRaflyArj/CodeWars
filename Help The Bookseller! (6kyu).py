# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python
def stock_list(listOfArt, listOfCat) :
    a, b = listOfArt, listOfCat
    name, num, count, res = [], [], [0] * len(b), []
    for item in a :
        item = item.split()
        name.append(item[0]); num.append(int(item[1]))
    for i in range (len(name)) :
        x = name[i]
        for j in range(len(b)) :
            if x[0] == b[j] :
                count[j] += num[i]
    for i in range (len(b)) :
        res.append(f"({b[i]} : {count[i]})")
    
    if sum(count) == 0 :
        return ""
    else :
        return ' - '.join(res)

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600", "CCOK 215", "NGUEN 1255"]
c = ["A", "B"]
print(stock_list(b, c))
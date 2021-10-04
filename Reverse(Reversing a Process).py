def code(n, num) :
    alphabeth = "abcdefghijklmnopqrstuvwxyz"
    res = []
    for item in n :
        x = alphabeth.index(item)
        number = x * num % 26
        res.append(alphabeth[number])

    return ''.join(res)

print(code("qockcouoqmoayqwmkkic", 761328))


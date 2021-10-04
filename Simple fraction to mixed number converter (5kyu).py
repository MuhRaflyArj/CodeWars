def mixed_fraction (s) :
    s = s.split("/")
    a, b = int(s[0]), int(s[1])

    return a + b 


print(mixed_fraction('-22/-7'))
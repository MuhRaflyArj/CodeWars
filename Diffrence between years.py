# https://www.codewars.com/kata/588f5a38ec641b411200005b/train/python

def how_many_years (date1,date2):
    return abs(int(date1.split("/")[0])-int(date2.split("/")[0]))

print(how_many_years ('1997/10/10', '2015/10/10')) # 18
print(how_many_years ('2015/10/10', '1990/10/10')) # 25
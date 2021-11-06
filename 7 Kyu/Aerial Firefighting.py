# https://www.codewars.com/kata/5d10d53a4b67bb00211ca8af/train/python

def waterbombs(fire, w):
    return sum([-(-(len(item))//w) for item in fire.split("Y")])
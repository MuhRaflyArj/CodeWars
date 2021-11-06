# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python

def queue_time(customers, n):
    tills = [0] * n
    for time in customers :
        tills[tills.index(min(tills))] += time
    return max(tills)
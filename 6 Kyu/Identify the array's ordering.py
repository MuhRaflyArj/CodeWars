# https://www.codewars.com/kata/57f669477c9a2b1b9700022d/train/python

def order_type(arr):
    a = []
    for item in arr :
        if type(item) == int : # Convert int type value to str          
            item = str(item)
        # List of length every value in arr
        a.append(len(item))
    
    # Return Constant if length of a is 0 or the value of a is all the same
    if len(a) == 0 or a.count(a[0]) == len(a) :
        return "Constant"

    # Return Decreasing if sorted list (with decending order) is equal to original list
    elif sorted(a, reverse = True) == a :
        return "Decreasing"

    # Return Increasing if sorted list (with ascending order) is equal to original list
    elif sorted(a) == a :
        return "Increasing"

    # Return Unsorted if none of above are true
    else :
        return "Unsorted"
# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python
def stock_list(listOfArt, listOfCat) :
    # assign var listOfArt and listOfCat as a and b
    a, b = listOfArt, listOfCat

    # Declare empty list for name, the number of pages, sum of pages, and result
    name, num, count, res = [], [], [0] * len(b), []


    for item in a :
        #Split the two book name and pages to two different list
        item = item.split()
        # Assign name and pages to two different list with same index
        name.append(item[0]); num.append(int(item[1]))

    # Check if name of book is in category   
    for i in range (len(name)) :
        # Assign Var x to a book name at index i
        x = name[i]
        for j in range(len(b)) :
            # Check if the beginning of the name equals one of letter in category
            if x[0] == b[j] :
                # If the name match a letter in category, add the pages to the list
                count[j] += num[i]


    for i in range (len(b)) :
        # Append a new string to list res, with format "{category} : {sum of pages}"
        res.append(f"({b[i]} : {count[i]})")
    print(res)
    # If count == 0 will return ''
    if sum(count) == 0 :
        return ""
    # Join all value in string with ' - ' as seperator
    else :
        return ' - '.join(res)

"""
Example : 
listOfArt = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
listOfCat = ["A", "B"]

using "for item in a", we will assign var item to every value in listOfArt.
Then split the item with .split() so item become -> ['ABAR', '200']
Append item[0] to list called name, and Append item[1] as integer to list called num

After the for loop is compeleted, we have var list
name = ['ABAR', 'CDXE', 'BKWR', 'BTSQ', 'DRTY']
num = [200, 500, 250, 890, 600]
Notice the index at name correspond to index at num

Using loop "for j in range" we can check if the first letter of name is the same
letter at listOfCat

If a match found, the value of num is summarized to count at index correnspond to a right letter at list b
so we have
b = ['A', 'B']
count = ['200', '1140']
which b[0] have count[0] pages

from there we just put it together to become a string to list called res
res = ['(A : 200)', '(B : 1140)']

from here we can just use ' - '.join(res)
which will output a string (A : 200) - (B : 1140)
"""
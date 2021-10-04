#  https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python

def title_case(title, minor_words=''):
    title, minor_words = title.split(" "), minor_words.lower().split(" ") 
    res = []
    for word in title :
        if word.lower() in minor_words :
            res.append(word.lower()); res.append(" ")
        else :
            res.append(word.lower().capitalize()); res.append(" ")
            
    res[0] = res[0].capitalize()

    return ''.join(res[:-1])    

print(title_case('THE WIND IN THE WILLOWS', 'The In')) # The Wind in the Willows
print(title_case('a clash of KINGS', 'a an the of')) # A Clash of Kings
print(title_case("the quick brown fox")) # The Quick Brown Fox


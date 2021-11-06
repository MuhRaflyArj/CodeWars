def sum_of_a_beach(beach):
    beach = beach.lower().replace('sun', '-').replace('water', '-').replace('fish', '-').replace('sand', '-')
    return beach.count('-')

"""
Convert the string into lowercase by .lower()

Replace matching string with - using .replace(valueBefore, valueAfter)

return the count of - by using .count(value)
"""
def high_and_low(numbers):
    a = [int(i) for i in numbers.split(" ")]
    return f"{max(a)} {min(a)}"

"""
Example = '1 2 3'
split the number using .split(" ") so it become -> ['1', '2', '3']
and convert it to integer by using int()
so now it become -> [1, 2, 3]

now just return min and max value using min() and max()
"""
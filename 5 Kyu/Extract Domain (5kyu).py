# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


"""
Example : http://google.com
We use url.split("//") so the var become list -> ['http:', 'google.com']

From the list we take index -1 (in this case that would be 'google.com')

We split again using url.split('.') so it became -> ['google', 'com']
and we just take index [0] from the list as the answer

in some case we have link with www.domain.com
so in between .split('//') and .split('.') we add .split('www.')
and take index[-1] from the list

dont forget to add index after .split() function so we can use another .split()
because .split() will not work on list

ex : var.split(value)[index] so it will return value at the index, not list
"""

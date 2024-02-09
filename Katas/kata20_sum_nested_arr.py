"""
Implement a function to calculate the sum of the numerical values in a nested list. For example :

sum_nested([1, [2, [3, [4]]]]) -> 10
"""

def getSum(lst):
    total = 0

    for j in range(len(lst)):
        if type(lst[j]) == list :
            total+= getSum(lst[j])
        else:
            total += lst[j]   

    return total

# Example usage:
my_list = [1, [2, [3, [4]]]]
result = getSum(my_list)
print("Sum of the list:", result)

"""
import re

def sum_nested(lst):
    return sum(map(int, re.findall('\d+', str(lst))))
"""
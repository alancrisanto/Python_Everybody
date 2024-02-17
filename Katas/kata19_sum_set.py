"""
DESCRIPTION:
Given a list of integers values, your job is to return the sum of the values; however, if the same integer value appears multiple times in the list, you can only count it once in your sum.

For example:

[ 1, 2, 3] ==> 6

[ 1, 3, 8, 1, 8] ==> 12

[ -1, -1, 5, 2, -7] ==> -1

[] ==> None
Good Luck!
"""

def unique_sum(lst):
  mySet = set()

  for x in lst:
      mySet.add(x)

  if len(mySet) == 0:
    return None
  else:
    return sum(mySet)

print(unique_sum([-1, -1, 5, 2, -7]))

"""
Solution 01:
def unique_sum(lst):
    return sum(set(lst)) if lst else None
-----------------------------------------------

Solution 02
def unique_sum(lst):
    if lst:
      return sum(set(lst)) 
"""
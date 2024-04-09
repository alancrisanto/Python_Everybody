"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""

a = [ 0, 0, 0.55, 0, 0 ]

def find_uniq(arr):
  myDict = dict()

  for x in arr:
    myDict[x] = myDict.get(x, 0) + 1

  for k, v in myDict.items():
    if v == 1:
      return k

print(find_uniq(a))


"""
-----------------------------------------------------------------------------------
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

-------------------------------------------------------------------------------------
def find_uniq(arr):
    return [x for x in set(arr) if arr.count(x) == 1][0]

-------------------------------------------------------------------------------------
def find_uniq(arr):
        return min(set(arr),key=arr.count)

-------------------------------------------------------------------------------------
from collections import Counter

def find_uniq(arr):
    return next(k for k,v in Counter(arr).items() if v == 1)
    
-------------------------------------------------------------------------------------
"""
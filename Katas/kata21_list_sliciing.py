"""
Background
Moving average of a set of values and a window size is a series of local averages.

Example:

Values: [1, 2, 3, 4, 5]
Window size: 3

Moving average is calculated as:


1, 2, 3, 4, 5
|     |
^^^^^^^
(1+2+3)/3 = 2


1, 2, 3, 4, 5
    |     |
    ^^^^^^^
    (2+3+4)/3 = 3


1, 2, 3, 4, 5
      |     |
      ^^^^^^^
      (3+4+5)/3 = 4

Here, the moving average would be [2, 3, 4]
"""

def moving_average(values,n):
    
  if n == 0 or len(values) < n:
    return None
  
  TotalAvr = list()

  for x in range(len(values) - n + 1):
    if n <= len(values):
      arr = values[x:x+n]
      avr = float(sum(arr) / len(arr))
      TotalAvr.append(avr)
    else:
      break
    # n += 1

  return TotalAvr

print(moving_average([1,2,3,4,5],3))


"""
---- 01-----------------------------------------------------------------------
from statistics import mean

def moving_average(values, n):
    if n and n <= len(values):
        return [mean(values[i : i + n]) for i in range(len(values) - n + 1)]

------------------------------------------------------------------------------

----02------------------------------------------------------------------------
def moving_average(a, n):
    if 0 < n <= len(a): return [sum(a[i:i+n]) / n for i in range(len(a) - n + 1)]

    
"""
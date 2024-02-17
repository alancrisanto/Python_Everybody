"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)
"""

def solution(number):

  arr = list()

  if number < 0:
    return 0
  
  for x in range(number):
    if x % 3 == 0 and x % 5 == 0:
      arr.append(x)
    elif x % 3 == 0:
      arr.append(x)
    elif x % 5 == 0:
      arr.append(x)
  
  return sum(arr)


print(solution(15))
    
# --- Clever Solution 
# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
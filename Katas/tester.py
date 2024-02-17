# ----------- kata 01-------------------

# txt = "to"
# words = txt.split(" ")

# for i in range(len(words)):
#   if len(words[i]) >= 5:
#     words[i] = words[i][::-1]

# print(" ".join(words))

# ------------ Kata 02 --------------------------
# Solution 01
# newStr = list()
# def double_char (s):
#   for x in range(len(s)):
#     print(s[x])
#     newStr.append(s[x] + s[x])

# double_char("Hello World")
# print("".join(newStr))

# Best solution 01
# def double_char_best (s):
#   return "".join( x * 2 for x in s)

# print(double_char_best("Hello Wworld"))

# ------- Kata 03 ---------------------------------
"""
It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry about strings with less than two characters. 'eloquent', 'loquen'
"""

# Solution 01
# def remove_char (s):
#   word = ""
#   for x in range(len(s)):
#     if x != 0 and x != (len(s) -1):
#       word += s[x]
#   return word


# Best Solution 02

# def remove_char (s):
#   return s[1: -1]

# print(remove_char("espectacular"))

# --------------- Kata 04 -----------------------
"""

Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).
The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.
Mind the input validation.

# Example
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6
# Input validation
# If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.

"""
# ***Solution 01

# def sum_array(arr):
#   highest = None
#   lowest = None
#   total = None


#   if arr is None:
#     total = 0
#   elif len(arr) <= 1:
#     total = 0
#   else:
#     for x in arr:
#       if lowest is None and highest is None:
#         lowest= x
#         highest = x 
#       elif x > highest:
#         highest = x
#       elif x < lowest:
#         lowest = x
      
#     if highest in arr and lowest in arr:
#       arr.remove(highest)
#       arr.remove(lowest)
#       total = sum(arr)
  
#   return total

# **** Solution 04
# def sum_array(arr):
#   if arr == None or len(arr) <3:
#     return 0
#   else:
#     return sum(arr) - max(arr) - min(arr)
  
# *** solution 04:
def sum_array(arr):
  try:
    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr)
  except:
    return 0

print(sum_array([3, 5, 10, 10, 8]))


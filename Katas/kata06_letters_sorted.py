"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

a = "abcdefghijklmnopqrstuvwxyz"
b = "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
  a3 = "".join(sorted(set(a1 + a2)))
  print(a3)
longest(a, b)
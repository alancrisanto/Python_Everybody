"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s):
  if len(s) % 2 != 0:
    s = s + "_"

  return list(s[i:i+2] for i in range(0, len(s), 2))


a = "abc"

print(solution(a))

""""
-------------------------------------------------------------------------------------------------
def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]

-------------------------------------------------------------------------------------------------
  if len(s) % 2 != 0:
    s = s + "_"

  return list(s[i:i+2] for i in range(0, len(s), 2))
  
-------------------------------------------------------------------------------------------------
import re

def solution(s):
    return re.findall('..', s + '_')
-------------------------------------------------------------------------------------------------
"""
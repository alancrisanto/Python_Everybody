"""
What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""

def valid_braces(string):
  arr = list()
  op = ["(", "{", "["]
  cl = [")", "}", "]"]

  for x in string:
    if x in op:
      arr.append(x)
    elif x in cl:
      if not arr:
        return False
      current = arr.pop()
      if current == "(":
        if x != ")":
          return False
      if current == "{":
        if x != "}":
          return False
      if current == "[":
        if x != "]":
          return False
  
  if arr:
    return False
  else:
    return True
  
"""
-----------------------------------------------------------------
def validBraces(string):

  while '()' in string or '[]' in string or '{}' in string:
      string = string.replace('{}','')
      string = string.replace('()','')
      string = string.replace('[]', '')
  
  return not string
-----------------------------------------------------------------
def validBraces(s):
    for i in range(len(s)//2):
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    return len(s) == 0
-----------------------------------------------------------------
def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0 

-----------------------------------------------------------------
def validBraces(s, previous = ''):
  while s != previous: previous, s = s, s.replace('[]','').replace('{}','').replace('()','')
  return not s

-----------------------------------------------------------------
def validBraces(s):
    pairs = ['{}', '()', '[]']
    while any(pair in s for pair in pairs):
        for pair in pairs: 
            s = s.replace(pair, "")
    return s == ""
-----------------------------------------------------------------

"""


  

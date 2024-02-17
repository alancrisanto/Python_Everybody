"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
  txt = ""
  for x in s:
    if x == x.upper():
      txt += " " + x
    else:
      txt += x
  return txt

print(solution(""))

# Clever Solutions
# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)
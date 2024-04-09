"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""

def count(s):   
    chs = dict()
    
    for x in s:
      chs[x] = chs.get(x, 0) + 1
    
    return chs


a = ""
print(count(a))

""""
----------------------------------------------------------------------------------
def count(string):
  
    return {i: string.count(i) for i in string}
----------------------------------------------------------------------------------

----------------------------------------------------------------------------------
"""
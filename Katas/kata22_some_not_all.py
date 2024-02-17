"""
Some but not all
Description
Your task is to create a function that given a sequence and a predicate, returns True if only some (but not all) the elements in the sequence are True after applying the predicate

Examples
some('abcdefg&%$', str.isalpha)
>>> True

some('&%$=', str.isalpha)
>>> False

some('abcdefg', str.isalpha)
>>> False

some([4, 1], lambda x: x>3)
>>> True

some([1, 1], lambda x: x>3)
>>> False

some([4, 4], lambda x: x>3)
>>> False
"""

def some_but_not_all(seq, pred): 
  arrBool = list()  
  for x in seq:
    arrBool.append(pred(x))

  if arrBool.count(True) == len(arrBool) or True not in arrBool:
    return False
  else:
    return True
    
txt = "&%$"

print(some_but_not_all([1, 1], lambda x: x>3))

"""
01---------------------------------------------------------------

def some_but_not_all(seq, pred): 
    return any(map(pred, seq)) and not all(map(pred, seq))

02----------------------------------------------------------------

def some_but_not_all(seq, pred): 
    return 0 < sum(map(pred, seq)) < len(seq)

"""
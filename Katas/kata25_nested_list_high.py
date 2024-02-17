"""
DESCRIPTION:
A nested list (or array in JavaScript) is a list that appears as a value inside another list,

[item, item, [item, item], item]
in the above list, [item, item] is a nested list.

Your goal is to write a function that determines the depth of the deepest nested list within a given list.
return 1 if there are no nested lists. The list passed to your function can contain any data types.

A few examples:

list_depth([True])
return 1

list_depth([])
return 1

list_depth([2, "yes", [True, False]])
return 2

list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1])
return 6

list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]])
return 2

"""

def list_depth(lst):
    if type(lst) != list:
        return 0
  
    if not lst:
        return 1

    sub_list_depth = [list_depth(x) for x in lst]

    return 1 + max(sub_list_depth, default=0)

print(list_depth([2, "yes", [True, False]]))


"""
01----------------------------------------------------------------
def list_depth(l):
    depths = [1]
    for x in l:
        if isinstance(x, list):
            depths.append(list_depth(x) + 1)
    return max(depths)

02 ----------------------------------------------------------------
def list_depth(l):
    if l == []:
        return 1
    if isinstance(l, list):
        return 1 + max(list_depth(item) for item in l)
    else:
        return 0
"""

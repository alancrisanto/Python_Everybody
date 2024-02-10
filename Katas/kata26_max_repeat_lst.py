"""
Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0

Example
input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5 
The most frequent number in the array is -1 and it occurs 5 times.

"""

def most_frequent_item_count(lst):
  most_frequent = 0
  for x in lst:
    count = lst.count(x)
    if count > most_frequent:
      most_frequent = count
    
  return most_frequent


print(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]))


"""
01 ---------------------------------------------------------------------------
def most_frequent_item_count(collection):
    if collection:
        return max([collection.count(item) for item in collection])
    return 0

02 ---------------------------------------------------------------------------

def most_frequent_item_count(collection):
    return max(collection.count(i) for i in collection) if collection else 0
    
"""
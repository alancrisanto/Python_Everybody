"""
Create a function that receives a (square) matrix and calculates the sum of both diagonals (main and secondary)

Matrix = array of n length whose elements are n length arrays of integers.

3x3 example:

sum_diagonals( [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
] ) == 30 # 1 + 5 + 9 + 3 + 5 + 7
"""

A = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
] 

B = [[]] 

def sum_diagonals(matrix):

  print(len(matrix))

  sum1 = sum(row[i] for i, row in enumerate(matrix) if len(row) > 0)
  sum2 = sum(row[len(row) -1 - i] for i, row in enumerate(matrix) if len(row) > 0)

  return sum1 + sum2

sum_diagonals(B)

"""
01 Solution-----------------------------------------------

import numpy as np

def sum_diagonals(matrix):
    return np.trace(matrix) + np.trace(matrix[::-1])

def sum_diagonals(mx):
    l = len(mx)
    return sum(x[i] + x[l-i-1] for i,x in enumerate(mx)) if l and mx[0] else 0

"""
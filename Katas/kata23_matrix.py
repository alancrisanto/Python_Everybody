"""
DESCRIPTION:
Task
Given a matrix, find its submatrix obtained by deleting the specified rows and emptying the specified columns.

Input/Output
[input] 2D integer array matrix

2-dimensional array of integers.

1 ≤ matrix.length ≤ 10,

1 ≤ matrix[0].length ≤ 10,

0 ≤ matrix[i][j] ≤ 9.

[input] integer array rowsToDelete

Array of indices (0-based) of rows to be deleted.

0 ≤ rowsToDelete.length ≤ 5,

0 ≤ rowsToDelete[i] < matrix.length.

[input] integer array columnsToDelete

Array of indices (0-based) of columns to be deleted.

0 ≤ columnsToDelete.length ≤ 5,

0 ≤ columnsToDelete[i] < matrix[0].length.

[output] 2D integer array

Example
For


matrix = [  [1, 0, 0, 2]
          , [0, 5, 0, 1]
          , [0, 0, 3, 5]
          ]

rowsToDelete = [1]
columnsToDelete = [0, 2]
the output should be

[ [0, 2]
, [0, 5]
]
"""

matrix = [  [1, 0, 0, 2]
          , [0, 5, 0, 1]
          , [0, 0, 3, 5]
          ]
				
rowsToDelete = [1]
columnsToDelete = [0, 2]

def construct_submatrix(matrix, rows, cols):
  if len(rows) > 0:
    for i in sorted(rows, reverse=True):
        matrix.pop(i)

  matrix.pop(rows[0])
  for lst in matrix:
    for x in sorted(cols, reverse=True):
        del lst(x)
  print(matrix)

"""
01----------------------------------
def construct_submatrix(m, r, c):
    return [[k for j,k in enumerate(i) if j not in c] for i in [j for i,j in enumerate(m) if i not in r]]

02-------------------------------------------
def construct_submatrix(matrix, rows_to_delete, cols_to_delete):
    for r in sorted(rows_to_delete, reverse=True):
        matrix.pop(r)
    for c in sorted(cols_to_delete, reverse=True):
        for m in matrix:
            m.pop(c)
    return matrix

    
    
"""

construct_submatrix(matrix, rowsToDelete, columnsToDelete)
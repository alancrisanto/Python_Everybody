"""
DESCRIPTION:
Create an identity matrix of the specified size( >= 0).

Some examples:

(1)  =>  [[1]]

(2) => [ [1,0],
          [0,1] ]

        [ [1,0,0,0,0],
        [0,1,0,0,0],
(5) =>  [0,0,1,0,0],
        [0,0,0,1,0],
        [0,0,0,0,1] ]   
"""

def get_matrix(n):

  matrix = list()

  for x in range(n):
    matrix.append([])
    for j in range( n ):
      if x == j:
        matrix[x].append(1)
      else:
        matrix[x].append(0)

  
  for i in matrix:
    print(i)

get_matrix(3)

"""
01 -------------------------------------------------------------

def get_matrix(n):
    return [[1  if i==j else 0 for i in range(n)] for j in range(n)]

02 --------------------------------------------------------------
"""

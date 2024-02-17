"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

"""

def accum(st):
  arr = list()
  count = 1

  for x in st:
    arr.append((x*count).capitalize())
    count += 1

  print("-".join(arr))
accum("cwAt")

# def accum(s):
  # return '-'.join((a * i).title() for i, a in enumerate(s, 1))
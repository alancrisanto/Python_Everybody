"""
Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
"""
s = "Hello"

def repeat_str(rep, string):
  txt = string * rep
  print(txt)

repeat_str(5, s)
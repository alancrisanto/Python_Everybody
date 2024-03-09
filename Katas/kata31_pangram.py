"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

"""
import string

# txt = "The quick brown fox jumps over the lay dog"
txt = "Cwm fjord bank glyphs vext quiz"

def is_pangram(s):
  letters = string.ascii_lowercase
  return all(x in s.lower() for x in letters)

print(is_pangram(txt))

"""
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())
"""
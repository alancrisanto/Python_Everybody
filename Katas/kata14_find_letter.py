"""

Create a function that takes in a sentence and a character to find. Return a dictionary of each word in the sentence, with the number of the specified character as the value.

find_occurrences("Hello World", "o") ➞ {
  "hello" : 1,
  "world" : 1
}

find_occurrences("Create a nice JUICY function", "c") ➞  {
  "create" : 1,
  "a" : 0,
  "nice" : 1,
  "juicy" : 1,
  "function" : 1
}

find_occurrences("An APPLE a day keeps an Archeologist AWAY...", "A") ➞ {
  "an" : 1,
  "apple" : 1,
  "a" : 1,
  "day" : 1,
  "keeps" : 0,
  "archeologist" : 1,
  "away..." : 2
}
"""

def find_occurrences(txt, letter):
  mydict = dict()
  count = 0
  arr = txt.split()

  for x in arr:
    for y in x:
      if letter.lower() == y.lower():
        count +=1
        mydict[x.lower()] = count
      else:
        mydict[x.lower()] = count
    count = 0

  print(mydict)

find_occurrences("a function create juice", "c")

def find_occurrences(txt, search_char):
  a = txt.lower().split()
  dic = {}
  for word in a:
    for char in word:
      dic[word] = word.count(search_char.lower()) 
  return dic
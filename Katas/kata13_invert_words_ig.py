"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
pig_it('O tempora o mores !') # Oay emporatay oay oresmay !
"""
txt = "O tempora o mores !"
print(txt[0:1])
print(txt[:-1])


def pig_it(text):
  spltText = text.split()

  for x in range(len(spltText)):
    if spltText[x].isalpha(): 
      spltText[x] = spltText[x][1:] + spltText[x][0:1]   + "ay"

  return " ".join(spltText)

print(pig_it(txt))

# ---- Solution 01

# ef pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

"""
Task
In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 
Rules
1.  The input string will always be lower case but maybe empty.

2.  If the character in the string is whitespace then pass over it as if it was an empty seat
Example
wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
"""
def wave(people):
    return list(people[:i].lower() + people[i].upper() + people[i + 1:].lower() for i in range(len(people)) if people[i] != " ")


a = "two words"
b = " gap "
print(wave(b))

"""
---------------------------------------------------------------------------------------------------------
def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]

---------------------------------------------------------------------------------------------------------
def wave(s):
    return [s[:i].lower() + s[i:].capitalize() for i in range(len(s)) if s[i] != " "]
---------------------------------------------------------------------------------------------------------
"""
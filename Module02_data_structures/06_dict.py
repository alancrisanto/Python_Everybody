# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Output cwen@iupui.edu 5

name = input("Enter file: ")
# Create a new dictionary
mydict = dict()
# Variable for the highest email sender
countSender = None
highCount = None

try:
    fh = open(name)
except:
    print("Invalid file")
    quit()

# Iterate through the file
for line in fh:
  if line.startswith("From:"):
    # create a list with the split words
    words = line.split()
    # Add the name to the dictionary
    mydict[words[1]] = mydict.get(words[1], 0) + 1

for key, value in mydict.items():
  if highCount is None or value > highCount:
    countSender = key
    highCount = value

print(countSender, highCount)

# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0

# Use a try / except to handle error
try:
  fh = open(fname)
except:
  print("Could not open file")
  quit()

# Iterate trough the file lines
for line in fh:
  if line.startswith("X-DSPAM-Confidence:"):
    count += 1
    pos = line.find("0")
    num = float(line[pos: len(line)])
    total += num

print("Average spam confidence", float(total / count))





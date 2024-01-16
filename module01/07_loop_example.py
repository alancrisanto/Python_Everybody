count = 0
sum = 0

while True:
  sval = input("Enter a value: ")
  if sval == "done":
    break
  
  try:
    fval = float(sval)
  except:
    print("Invalid value")
    continue

  count += 1
  sum += fval

print(sum, count, sum/count)

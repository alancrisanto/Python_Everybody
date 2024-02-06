count = 0
total = 0

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
  total += fval

print(total, count, total/count)

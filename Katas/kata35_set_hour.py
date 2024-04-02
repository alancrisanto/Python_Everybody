"""
The time should be in HH:MM format.

Examples:

digits: 1, 9, 8, 3 => result: "19:38"
digits: 9, 1, 2, 5 => result: "21:59" (19:25 is also a valid time, but 21:59 is later)
Notes
Result should be a valid 24-hour time, between 00:00 and 23:59.
Only inputs which have valid answers are tested.
"""

def latest_time(digits):
  """
  This function receives 4 digits and returns the latest time of day that can be built with those digits.

  Args:
      digits: A list of 4 integers representing the digits for the time.

  Returns:
      A string representing the latest time in HH:MM format.
  """
  # Generate all possible permutations of the digits
  from itertools import permutations
  permutations = list(permutations(digits))

  # Try to convert each permutation to a valid time string
  best_time = None
  for perm in permutations:
    hours = int("".join([str(d) for d in perm[:2]]))
    minutes = int("".join([str(d) for d in perm[2:]]))
    # Check if the time is valid (between 00:00 and 23:59)
    if 0 <= hours <= 23 and 0 <= minutes <= 59:
      if best_time is None or (hours, minutes) > best_time:
        best_time = (hours, minutes)

  # If no valid time is found, return None
  if best_time is None:
    return None

  return f"{best_time[0]:02d}:{best_time[1]:02d}"

# Test cases
print(latest_time([1, 9, 8, 3]))  # Output: 19:38
print(latest_time([9, 1, 2, 5]))  # Output: 21:59
print(latest_time([0, 0, 0, 0]))  # Output: 00:00


"""
01 Solution -------------------------------------------------------------------------------------------------
from itertools import permutations
def latest_clock(*args):
    return '{}{}:{}{}'.format(*max(p for p in permutations(args) if p[:2] < (2, 4) and p[2:] < (6, 0)))

    
02 Solution -------------------------------------------------------------------------------------------------
def late_clock(*a):
    for h in range(23, -1, -1):
        for m in range(59, -1, -1):
            x = f'{h:02}'
            y = f'{m:02}'
            s = list(map(int,list(x + y)))
            if sorted(s)==sorted(a):
                return f'{x}:{y}'
"""
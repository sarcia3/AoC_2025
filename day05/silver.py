import sys


ranges = []
for line in sys.stdin:
  if line ==  "\n":
    break
  ranges.append([int(val) for val in line[:-1].split('-')])

res = 0
for line in sys.stdin:
  num = int(line[:-1])
  for [lb, ub] in ranges:
    if lb <= num and num <= ub:
      res += 1
      break

print(res)

  

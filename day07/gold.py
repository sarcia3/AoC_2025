import sys

curr = dict()
for line in sys.stdin:
  for (i, char) in enumerate(line):
    if char == 'S':
      curr[i] = 1
    else: curr[i] = 0
  break;

for line in sys.stdin:
  new = curr.copy()
  for (i, char) in enumerate(line[:-1]):
    if char == '^' and i in curr:
      if i > 0:
        new[i-1]+=curr[i]
      if i < len(line)-2:
        new[i+1]+=curr[i]
      new[i] = 0
  curr = new

res = sum([curr[i] for i in curr])
print(res)





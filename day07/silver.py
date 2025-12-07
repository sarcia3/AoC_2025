import sys

curr = set()
for line in sys.stdin:
  for (i, char) in enumerate(line):
    if char == 'S':
      curr.add(i)
  break;
res = 0
for line in sys.stdin:
  new = curr.copy()
  for (i, char) in enumerate(line[:-1]):
    if char == '^' and i in curr:
      res += 1
      if i > 0:
        new.add(i-1)
      if i < len(line)-2:
        new.add(i+1)
      new.remove(i)
  curr = new

print(res)





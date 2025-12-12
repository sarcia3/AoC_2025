import sys



types = []

for i in range(0, 6):
  thrash = input()
  r1 = [int(a == '#') for a in input()]
  r2 = [int(a == '#') for a in input()]
  r3 = [int(a == '#') for a in input()]
  thrash = input()
  types.append([r1, r2, r3])

sumbad = 0
res = 0
for line in sys.stdin:
  line = line[:-1]
  line = line.split(" ")
  dimns = line[0][:-1].split("x")
  dimns = [int(d) for d in dimns]
  vals = [int(v) for v in line[1:]]
  num = (-sum([vals[i] * sum([sum(types[i][j]) for j in range(len(types[i]))]) for i in range(len(vals))]) + dimns[0] * dimns[1])
  if (max(dimns)//5) * (min(dimns)//4) >= sum(vals)//2 or num > 0:
    res += 1 
    print(1)
print(res)

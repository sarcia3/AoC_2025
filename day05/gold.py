import sys


ranges = []
for line in sys.stdin:
  if line ==  "\n":
    break
  ranges.append([int(val) for val in line[:-1].split('-')])


ranges.sort()

res = 0
c_max = -1
for i in range(0, len(ranges)):
  res += max(ranges[i][1] - max(ranges[i][0], c_max+1) + 1, 0)
  c_max = max(c_max, ranges[i][1])

print(res)

  

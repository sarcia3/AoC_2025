import sys
import numpy as np

res=0

def bg_l(ln, arr):
  if ln == 0:
    return [max(arr), np.argmax(arr)]
  return [max(arr[:-ln]), np.argmax(arr[:-ln])]
for line in sys.stdin:
  arr = [int(a) for a in line[:-1]]
  last = 0
  rs = ""
  for i in range(11, -1, -1):
    tmp = bg_l(i, arr[last:])
    rs += str(tmp[0])
    last = last+ tmp[1]+1
  res+=int(rs)

print(res)
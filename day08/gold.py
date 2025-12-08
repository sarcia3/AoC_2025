import sys
from math import sqrt
from functools import cmp_to_key
from itertools import count
boxes = []
for line in sys.stdin:
  line = line[:-1]

  boxes.append([int(coord) for coord in line.split(',')])

def compare(lhs, rhs):
  return sqrt(sum([(boxes[lhs[0]][i] - boxes[lhs[1]][i]) ** 2 for i in range(0, 3)])) - sqrt(sum([(boxes[rhs[0]][i] - boxes[rhs[1]][i]) ** 2 for i in range(0, 3)]))

pairs = []
for i in range(len(boxes)):
  for j in range(i+1, len(boxes)):
    pairs.append((i, j))

pairs = sorted(pairs, key=cmp_to_key(compare))

num = 1000

left = len(boxes)
P = [i for i in range(len(boxes))]
R  = [1] * len(boxes)
def union(a, b):
  global P
  global R
  def find(pos):
    if P[pos] != pos:
      P[pos] = find(P[pos])
    return P[pos]

  a, b  = find(a), find(b)
  if a != b:
    global left
    left -= 1

  if R[a] < R[b]:
    P[a] = b
    return
  else:
    P[b] = a
    R[a] += (R[a] == R[b])
    return


for i in count():
  union(pairs[i][0], pairs[i][1])
  if left == 1:
    print(boxes[pairs[i][0]][0]* boxes[pairs[i][1]][0])
    break

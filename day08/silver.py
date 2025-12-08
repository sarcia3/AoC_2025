import sys
from math import sqrt
from functools import cmp_to_key

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

graph = [[] for _ in range(len(boxes))]
for i in range(num):
  lhs, rhs = pairs[i]
  graph[lhs].append(rhs)
  graph[rhs].append(lhs)

group = [-1] * len(graph)

sizes = []
def dfs(v):
  if group[v] != -1:
    return

  stack = [v]
  group[v] = v
  res = 1
  while len(stack):
    w = stack.pop()
    for u in graph[w]:
      if group[u] == -1:
        stack.append(u)
        group[u] = v
        res += 1
  
  sizes.append(res)


for v in range(len(graph)):
  dfs(v)

sizes.sort(reverse=True)
res = sizes[0] * sizes[1] * sizes[2]

print(res)
import sys
from collections import defaultdict
graph = defaultdict(list)
rgraph = defaultdict(list)

for line in sys.stdin:
  line = line[:-1].split()

  src = line[0][:-1]

  for dest in line[1:]:
    graph[src].append(dest)

def calc(v):
  if(v == "out"): 
    return 1
  return sum([calc(w) for w in graph[v]])

print(calc("you"))
  


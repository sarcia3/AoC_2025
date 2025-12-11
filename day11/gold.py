import sys
from collections import defaultdict
graph = defaultdict(list)
rgraph = defaultdict(list)

for line in sys.stdin:
  line = line[:-1].split()

  src = line[0][:-1]

  for dest in line[1:]:
    graph[src].append(dest)

vis=set()
vals = dict()
def calc(v, end):
  global graph
  if(v == end): 
    return 1
  if v == "out":
    return 0
  vis.add(v)
  res = 0;
  for w in graph[v]:
    if w not in vis:
      if w not in vals:
        ret = calc(w, end)
        vals[w] = ret
      res += vals[w] 
  vis.remove(v)
  return res

a = calc("svr", "fft") 
vis = set()
vals = dict()
b= calc("fft", "dac")
vis = set()
vals = dict()
c = calc("dac", "out")
vis = set()
vals = dict()
d = calc("svr", "dac") 
vis = set()
vals = dict()
e = calc("dac", "fft") 
vis = set()
vals = dict()
f = calc("fft","out")
  
print(a*b*c + d*e*f)


import sys

points = []
for line in sys.stdin:
  line = line[:-1]
  points.append([int(i) for i in line.split(',')[::-1]])
def solve(points):  
  x_to_pos = dict()
  x_tmp = [p[0] for p in points]
  x_tmp = sorted(set(x_tmp))
  for i, x in enumerate(x_tmp):
    x_to_pos[x] = i
  y_to_pos = dict()
  y_tmp = [p[1] for p in points]
  y_tmp = sorted(set(y_tmp))
  for i, y in enumerate(y_tmp):
    y_to_pos[y] = i

  greens = []
  vis = [[0 for _ in range(len(points))] for __ in range(len(points))]
  points.append(points[0])
  for i in range(len(points)-1):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    x1, x2 = [x_to_pos[x1], x_to_pos[x2]]
    y1, y2 = [y_to_pos[y1], y_to_pos[y2]]

    if x1 == x2:
      for y in range(min(y1, y2), max(y1, y2) + 1):
        greens.append([x1, y])
        vis[x1][y] = 1
    else:
      for x in range(min(x1, x2), max(x1, x2) + 1):
        greens.append([x, y1])
        vis[x][y1] = 1

  points.pop()
# (13, 120)
  def dfs(vx, vy):
    stack = [[vx, vy]]
    vis[vx][vy] = 1
    def add(x, y):
      if(vis[x][y] != 1):
        stack.append([x, y])
        vis[x][y] = 1
    while len(stack):
      x, y = stack.pop()
      add(x-1, y)
      add(x+1, y)
      add(x, y-1)
      add(x, y+1)
  
  if(len(points) > 20):
    dfs(13, 120)
  else: dfs(1, 2)
  presum= [[0 for _ in range(len(points))] for __ in range(len(points))]
  presum[0][0] = (vis[0][0] == 1)
  for i in range(1, len(points)):
    presum[i][0] = presum[i-1][0] + (vis[i][0] == 1)
    presum[0][i] = presum[0][i] + (vis[0][i] == 1)
  
  for x in range(1, len(points)):
    for y in range(1, len(points)):
      presum[x][y] = presum[x-1][y] + presum[x][y-1] - presum[x-1][y-1] + (vis[x][y] == 1)

  for x in vis:
    for y in x:
      print(y, end="")
    print()
  res=0
  for i in range(len(points)):
    for j in range(i+1, len(points)):
      ix, iy = points[i] 
      jx, jy = points[j] 
      indix = x_to_pos[ix]
      indjx = x_to_pos[jx]
      indiy = y_to_pos[iy]
      indjy = y_to_pos[jy]
      def get_n_green(x1, y1, x2, y2):
        x1, x2 = [min(x1, x2), max(x1, x2)]
        y1, y2 = [min(y1, y2), max(y1, y2)]
        left = 0
        top = 0
        diag = 0
        if x1 > 0:
          left = presum[x1-1][y2]
        if y1 > 0:
          top = presum[x2][y1-1]
        if x1 > 0 and y1 > 0:
          diag = presum[x1-1][y1-1]
        return presum[x2][y2] - left - top + diag
      if (abs(indix-indjx)+1) * (abs(indiy-indjy)+1) == get_n_green(indix, indiy, indjx, indjy):
       res = max(((abs(ix-jx)+1)*(abs(iy-jy)+1)), res)
  return res

print(solve(points))

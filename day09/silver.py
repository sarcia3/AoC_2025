import sys

points = []
for line in sys.stdin:
  line = line[:-1]
  points.append([int(i) for i in line.split(',')])

res = 0
for i in range(len(points)):
  for j in range(i+1, len(points)):
   ix, iy = points[i] 
   jx, jy = points[j] 
   res = max( abs((ix-jx+1)*(iy-jy+1)), res)

print(res)

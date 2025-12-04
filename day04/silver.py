import sys

arr = []
for line in sys.stdin:
  arr.append(line)
  arr[-1] = "." + arr[-1] + "."

arr.insert(0, str(["," for i in range(len(arr[0]))]))
arr.append(str(["," for i in range(len(arr[0]))]))

res = 0
for i in range(len(arr)):
  for j in range(len(arr[i])):
    if(arr[i][j] == '@'):
      cnt = -1
      for hor in [-1, 0, 1]:
        for ver in [-1, 0, 1]:
          cnt += int(arr[i+hor][j+ver] == '@')
      if cnt < 4:
        res += 1


print(res)

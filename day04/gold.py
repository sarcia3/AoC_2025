import sys

arr = []
for line in sys.stdin:
  arr.append(list(line))
  arr[-1].append(".")
  arr[-1].insert(0, ".")

arr.insert(0, (["," for i in range(len(arr[0]))]))
arr.append((["," for i in range(len(arr[0]))]))

res = 0
oldres = res-1
while oldres < res:
  oldres = res
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if(arr[i][j] == '@'):
        cnt = -1
        for hor in [-1, 0, 1]:
          for ver in [-1, 0, 1]:
            cnt += int(arr[i+hor][j+ver] == '@')
        if cnt < 4:
          res += 1
          arr[i][j] = '.'
  print(oldres, res)



print(res)

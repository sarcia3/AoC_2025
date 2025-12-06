import sys

arr = []
bigres = 0
for line in sys.stdin:
  if line[0] != '+' and line[0] != '*':
    arr.append([int(num) for num in line[:-1].split()])
  else:
    line = line[:-1].split()
    for i in range(len(line)):
      if(line[i] == '+'):
        res = 0;
        for j in range(len(arr)):
          res += arr[j][i]
        bigres += res 
      else:
        res = 1; 
        for j in range(len(arr)):
          res *= arr[j][i]
        bigres += res 
print(bigres)



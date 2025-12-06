import sys

arr = []
bigres = 0
for line in sys.stdin:
  if line[0] != '+' and line[0] != '*':
    line = line[:-1] + ' '
    arr.append(line)

  else:
    line = line[:-1] + "  "
    last = (0, 0)
    for i in range(len(line)):
      if(line[i] == '+'):
        last = (0, i)
      if(line[i] == '*'):
        last = (1, i)
      if line[i] == ' ' and (i == len(line)-1 or  line[i+1] != ' '):
        digits = []
        for x in range(last[1], i):
          curr = ""
          for y in range(len(arr)):
            curr = curr+arr[y][x]
          curr = curr.split()
          curr.append(0)
          digits.append(int(curr[0]))
        if last[0] == 0 :
          res = 0;
          for num in digits:
            res += num
          bigres += res 
        if last[0] == 1 :
          res = 1;
          for num in digits:
            res *= num
          bigres += res 
print(bigres)



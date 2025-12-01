# reconstruction
x = ""
curr = 50;
res = 0
while True:
  x = input();

  old = curr
  if(x[0] == 'L'):
    curr = curr- int(x[1:])
  else: curr = curr + int(x[1:])

  curr = curr % 100
  if curr == 0:
    res = res + 1
  print(res, curr)


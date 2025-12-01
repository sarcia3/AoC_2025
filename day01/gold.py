x = ""
curr = 50;
res = 0
while True:
  x = input();

 # old = curr
 # if(x[0] == 'L'):
 #   curr = curr- int(x[1:])
 # else: curr = curr + int(x[1:])

  chg = int(x[1:])

  while(chg != 0):
    old = curr
    if(x[0] == 'L'):
      curr =curr- min(99, chg)
    else: curr =curr+ min(99, chg)

    if (old != 0 and curr <=0):
      res = res + 1
    if (curr >= 100):
      res = res + 1
    curr = curr % 100
    chg = chg - min(99, chg)
  print(res, curr)


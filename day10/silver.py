import sys
from itertools import permutations, count
relres = 0
cnt = 0
for line in sys.stdin:
  print(cnt)
  cnt += 1
  line = line[:-1].split()

  goal = line[0][::-1]
  goal = int("".join([str(int(goal[i] == '#')) for i in range(1, len(goal)-1)]), 2)

  buttons = []
  for i in range(1, len(line)-1):
    button = ["0"] * 30
    for light in range(1, len(line[i])-1, 2):
      button[int(line[i][light])] = "1"
    button = "".join(button)
    buttons.append(int(button[::-1], 2))
  
  res = 500
  to_perm = [0] * len(buttons)
  for bitmask in range(0, 2 ** len(buttons)):
    curr = 0
    mask = bitmask
    t = 0

    while mask:
      if mask % 2 == 1:
        curr ^= buttons[t]
      t += 1
      mask //=2
    if curr == goal:
      res = min(res, bitmask.bit_count())
  relres += res
#  for res in count():
#    curr = 0
#    for perm in permutations(to_perm):
#      curr = 0
#      for i in range(len(perm)):
#        if perm[i] == 1:
#          curr ^= buttons[i]
#      if curr == goal:
#        break
#    if curr == goal:
#      relres += res
#      break
#    to_perm[res] = 1
#

print(relres)

    




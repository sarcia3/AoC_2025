# code quality is horrible and the solve is probably overcomplicated, but I just wanted to be done with this
# I did not use LLms
import sys
from collections import defaultdict
import numpy as np
import scipy 
relres = 0
cnt = 0

print(scipy.__version__)
relres=0
for line in sys.stdin:
  res = 100000000000000
  print(cnt)
  cnt += 1
  line = line[:-1].split()
  
  goal = [int(val) for val in line[-1][1:-1].split(",")]

  buttons = [[0] * len(goal) for _ in range(len(line)-2)]
  for i in range(1, len(line)-1):
    for j in range(1, len(line[i])-1, 2):
      buttons[i-1][int(line[i][j])] = 1
    #buttons.append([int(line[i][pos]) for pos in range(1, len(line[i])-1, 2)])

  def bfs(v):
    known = dict()
    queue = [[0 for _ in v]]
    known[tuple([0 for _ in v])] = 0
    while len(queue):
      top = queue.pop()
      for button in buttons:
        new = list(top)
        bad = 0
        for pos in button:
          new[pos] += 1
          if new[pos] > v[pos]:
            bad = 1
            break
        if bad == 0:
          if tuple(new) not in known:
            queue.insert(0, new)
            known[tuple(new)] = known[tuple(top)] + 1
          if new == v:
            return  known[tuple(v)]

  ### print(np.linalg.matrix_rank(np.matrix(buttons).T) - len(buttons))

  k = int(np.linalg.matrix_rank(np.matrix(buttons).T) )
  bits =0
  for bitmask in range(0, 2**(len(buttons))):
    if bitmask.bit_count() != k:
      continue

    columns = []
    tmpcol= set()
    rest = []
    for i, bit in enumerate(bin(bitmask)[2:]):
      if bit == '1':
        columns.append(buttons[i])
        tmpcol.add(tuple(buttons[i]))
    for i in range(len(buttons)):
      if tuple(buttons[i]) not in tmpcol:
        rest.append(buttons[i])
    rest = list(rest)
    if int(np.linalg.matrix_rank(np.matrix(columns).T) ) == k:
      #print(columns) 
      coefs = np.linalg.lstsq(np.matrix(columns).T, goal)[0]
      dependency_coefs = []
      bounds = []


      to_prod = []
      for guy in rest:
        to_prod.append([])
        #c = np.linalg.lstsq(np.matrix(buttons).T, guy)[0]
        #dependency_coefs.append(c)
        value = 100000
        for j in range(len(guy)):
          if guy[j] != 0:
            value = min(value, goal[j])
        aaaa = value
        for ind in range(0, aaaa+4):
          to_prod[-1].append([val * ind for val in guy])
      zero_vec =[[0 for _ in range(len(goal))]]
      while len(to_prod) < 3:
        to_prod.append(zero_vec)

      for pierwszy in to_prod[0]:
        print(cnt, pierwszy)
        for drugi in to_prod[1]:
          for third in to_prod[2]:
            calosc = [goal[i]-(pierwszy[i] + drugi[i] + third[i]) for i in range(0, len(pierwszy))]
            wyniczex= np.linalg.lstsq(np.matrix(columns).T, calosc)[0]
            #print(np.linalg.lstsq(np.matrix(columns).T, calosc))
            tmp = 0
            for smutna_buzka in wyniczex:
              if smutna_buzka < -0.00001:
                tmp = 1
              if abs(smutna_buzka - round(smutna_buzka)) > 0.001:
                tmp = 1
            if tmp == 0:
              res = min(res, round(sum(wyniczex)) + max(pierwszy) + max(drugi) + max(third))

      print(res)
      relres+=res
      break


  #mx = (110, 0)
  #for i in range(len(goal)):
  #  urres = 0
  #  for button in buttons:
  #    if i in set(button):
  #      urres+=1
  #  mx = min((urres, i), mx)
  #print(scipy.special.comb(mx[0]+ goal[mx[1]]-1, mx[0]-1))
  #distrib = []
  #def gen_distrib(curr, left_ind, left_sum):
  #  curr = curr.copy()
  #  if left_ind == 0:
  #    distrib.append(curr)
  #    return
  #  if left_ind == 1:
  #    curr.append(left_sum)
  #    gen_distrib(curr, 0, 0)
  #    return
  #  curr.append(0)
  #  for val in range(0, left_sum+1):
  #    curr[-1] = val
  #    gen_distrib(curr, left_ind-1, left_sum-val)
  
  #gen_distrib([], mx[0], goal[mx[1]])
  #buttons_w_mx1 = []
  #for button in buttons:
  #  if mx[1] in set(button):
  #    buttons_w_mx1.append(button)
  
  #print(len(distrib))

  #print(len(buttons)- np.linalg.matrix_rank(buttons), "        ", np.linalg.matrix_rank(buttons)-len(goal))
  #print(len(buttons), len(goal))
  #if len(buttons) == np.linalg.matrix_rank(buttons):
    #print(np.linalg.solve(buttons, goal))
  #print(len(buttons)-len(goal))
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

    




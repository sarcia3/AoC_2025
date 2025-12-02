res = 0
cart = input()

id_pairs = cart.split(",")

ids_ip = [id_pair.split('-') for id_pair in id_pairs]

a=0
for idp in ids_ip:
  print(str(a) + "/" + str(len(ids_ip)))
  for id in range(int(idp[0]), int(idp[1])+1):
    id1 = str(id)
    did_work = 0
    for i in range(1, len(id1)):
      for m in range(1, len(id1)//i + 2):
        if id1 == id1[:i]*m:
          did_work = int(id1)
          break
    res += did_work

print(res)
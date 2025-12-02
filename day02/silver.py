res = 0
cart = input()

id_pairs = cart.split(",")

ids_ip = [id_pair.split('-') for id_pair in id_pairs]

for idp in ids_ip:
  for id in range(int(idp[0]), int(idp[1])+1):
    id1 = str(id)
    if id1 == id1[:len(id1)//2]*2:
      res += int(id1)

print(res)

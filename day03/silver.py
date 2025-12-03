import sys

res = 0
for line in sys.stdin:
  arr = [int(a) for a in line[:-1]]
  mx = max(arr[:len(arr)-1])
  was_mx = False
  snd = 0
  for i in range(len(arr)):
    if was_mx:
      snd = max(snd, arr[i])
    if(arr[i] == mx):
      was_mx = True
  res += mx*10 + snd

print(res)
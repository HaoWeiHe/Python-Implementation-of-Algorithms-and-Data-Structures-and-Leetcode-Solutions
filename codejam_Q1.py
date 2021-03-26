
T = int(raw_input())
for number in range(T):
  N = int(raw_input())
  
  if N:
    L = map(int,raw_input().split(" "))
  cost = 0

  for i in range(N -1):
    idx, v = i, L[i]
    for j in range(i + 1, N):
        if L[j] < v: 
            idx = j
            v = L[j]
    L = L[ : i] + L[i : idx+1 ][::-1] + L[idx+1:]
    cost += (idx - i+1)

      
  print("Case #{}: {}".format(number + 1,cost))
    
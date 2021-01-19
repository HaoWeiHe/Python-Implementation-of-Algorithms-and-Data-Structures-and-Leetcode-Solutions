def moveZerosToEnd(lst):

  j = 0 
  for i in range(len(lst)):
    if lst[i]:
      lst[i], lst[j] = lst[j], lst[i]
      j += 1
  return lst
     
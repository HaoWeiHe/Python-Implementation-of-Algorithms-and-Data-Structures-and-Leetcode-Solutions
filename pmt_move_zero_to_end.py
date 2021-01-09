def moveZerosToEnd(arr):
  for i in range(len(arr)):
    if arr[i] == 0 :
      for j in range(i+1, len(arr)+1):
        if j == len(arr) : return arr
        if arr[j] != 0 :
          arr[i], arr[j] = arr[j], arr[i] 
          break
  return arr

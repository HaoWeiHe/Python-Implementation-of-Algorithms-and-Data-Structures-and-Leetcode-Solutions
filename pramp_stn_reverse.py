"""
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]




$We Love Python
nohtyP evoL eW$
              v
            s
        s = v+1
reverse(s:v-1)
reverse(s:v-1)
reverse(s:v-1)
"""
#space complex: O(1)
#Time complex: O(N)

def reverse_words(arr):

  def helper(l,r): # O(1)
    while  l < r:
      arr[l], arr[r] = arr[r], arr[l]
      l +=1
      r -=1
 
  arr = [" "]+arr
  helper(0,len(arr)-1)

  s = 0                
  for v in range(len(arr)):
    if arr[v] == " " or v == len(arr) - 1:
      helper(s,v-1) #P["a"," "," ","b"]    
      s = v + 1
  arr.pop()#remove $
  return arr



  

def partition(nums, l,r): #[6,5,9,0,8,2,4,7]
    cmp_ele = nums[r-1]
    i = l 
    for v in range(l, r):
        if nums[v] <= cmp_ele:
            nums[v], nums[i] = nums[i], nums[v]
            i += 1
    
    return i

def quickSort(arr, l, r):
    if l >= r:
        return
    
    p = partition(arr, l, r)
    

    quickSort(arr, l, p-1 )
    quickSort(arr, p, r)
    return arr
        
# [6,5,0,2,4,7,8,9]
nums = [6,5,9,0,8,2,4,7]
print(quickSort(nums, 0 , len(nums)))

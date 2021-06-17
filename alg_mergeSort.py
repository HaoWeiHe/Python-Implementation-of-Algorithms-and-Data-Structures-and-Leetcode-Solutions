"""
        538462714
     5384   62714
    53  84
  5  3

  35 
"""

def mergeSort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr)/2

    left_arr = mergeSort(arr[:mid])
    right_arr  = mergeSort(arr[mid:])

    i, j = 0, 0 
    ans = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            ans.append(left_arr[i])
            i += 1
        else:
            ans.append(right_arr[j])
            j += 1

    if i != len(left_arr):
        ans += left_arr[i:] 

    if j != len(right_arr):
        ans += right_arr[j:]
    return ans



def Merge_Sort2(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]
​
        Merge_Sort(left_array)
        Merge_Sort(right_array)
​
        right_index = 0;
        left_index = 0;
        merged_index = 0;
        while right_index < len(right_array) and left_index < len(left_array):
            if(right_array[right_index] < left_array[left_index]):
                array[merged_index] = right_array[right_index]
                right_index = right_index + 1
            else:
                array[merged_index] = left_array[left_index]
                left_index = left_index + 1
​
            merged_index = merged_index + 1
​
        while right_index < len(right_array):
            array[merged_index] = right_array[right_index]
            right_index = right_index + 1
            merged_index = merged_index + 1
​
        while left_index < len(left_array):
            array[merged_index] = left_array[left_index]
            left_index = left_index + 1
            merged_index = merged_index + 1
​

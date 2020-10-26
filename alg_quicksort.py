def Merge_Sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        # print(mid, array[:mid], array[mid:])
        left_array = array[:mid]
        right_array = array[mid:]
        print(right_array)
        Merge_Sort(left_array)
        Merge_Sort(right_array)
        
        right_index = 0
        left_index = 0
        merged_index = 0
       
        
        while right_index < len(right_array) and left_index < len(left_array):
            if(right_array[right_index] < left_array[left_index]):
                array[merged_index] = right_array[right_index]
                right_index = right_index + 1
            else:
                array[merged_index] = left_array[left_index]
                left_index = left_index + 1

            merged_index = merged_index + 1

        while right_index < len(right_array):
            array[merged_index] = right_array[right_index]
            right_index = right_index + 1
            merged_index = merged_index + 1
        while left_index < len(left_array):
            array[merged_index] = left_array[left_index]
            left_index = left_index + 1
            merged_index = merged_index + 1
        # print(merged_index)
        # print(left_array, right_array, array)

Numbers = [41, 33, 17, 80, 61, 5, 55]
print(Numbers)
Merge_Sort(Numbers)
print(Numbers)

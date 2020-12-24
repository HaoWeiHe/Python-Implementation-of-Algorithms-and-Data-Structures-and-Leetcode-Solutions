class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        [9,9,9,0,0,0]
             i     p
        [2,5,6]
             j
        """

        p = m + n -1
        i,j = m-1, n-1
        
        while i >=0 and j >=0:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
        num1[:j+1] = nums2[:j+1] 
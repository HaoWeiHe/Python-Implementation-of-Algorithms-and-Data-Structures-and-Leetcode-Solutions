class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        total = len1+len2
        tmp = 0
        term = 0
        tag = False
        if len1==0 or len2==0:
            nums1.append(0)
            nums2.append(0)
        if len1==1 and len2==1:
            return (nums1[0]+nums2[0])/2
        
        if total%2==1 :
            term = int(total/2)
        else:
            term = int(total/2)+1
            tag = True
        i,j,fin= 0, 0, list()
        
        while(tmp <= term):
        
            if j == len2:
                fin.append(nums1[i])
                i+=1
                tmp+=1
                continue
            
            if i < len1 and nums1[i] < nums2[j]:
                
                fin.append(nums1[i])
                i += 1
            else:
                fin.append(nums2[j])
                j += 1
            tmp += 1
        
        if tag:
            return (fin[-3]+fin[-2])/2
        else:
            return fin[-1]
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        return self.merge(A,B)
    
    def merge(self,A,B):
        total_len = len(A) + len(B)
        q,r = divmod(total_len, 2)
        ans= set()
        if r == 0:
            ans = set([q-1,q])
        else:
            ans = set([q,q])
        i, j = 0, 0 
        piv = 0
        flag = q
        res = 0
        tmp = 0
        while i< len(A) and j < len(B):
            if A[i] < B[j] :
                tmp = A[i]
                i += 1
            else:
                tmp = B[j]
                j += 1
            
            if piv > flag:
                break

            if piv in ans:
                if r !=0:
                    res = tmp *2
                else:
                    res += tmp
            piv += 1
        while i < len(A):
            tmp = A[i]
            if piv > flag:
                break

            if piv in ans:
                if r !=0:
                    res = tmp *2
                else:
                    res += tmp
            i += 1
            piv += 1
        while j < len(B):
            tmp = B[j]
            if piv > flag:
                break

            if piv in ans:
                if r !=0:
                    res = tmp *2
                else:
                    res += tmp
            j += 1
            piv += 1   
        return res/2.0
            
            
                
            
        
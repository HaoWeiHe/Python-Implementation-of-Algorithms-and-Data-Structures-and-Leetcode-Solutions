class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        [1,2,3,4]
        {1:2,2:3,3:4,4:-1}
        
        
        nums2 [1,3,4,2]
        d {1:3,3:4}
        for e in nums:
            ans.append(d[e])
        
        [1,3,4,2]
               v
    s   [4,2]
    d = {1:3,3:4 }
    
        """
        s,d = [],{}
        for v in nums2:
            while s and v > s[-1]:
                d[s.pop()] = v
            s.append(v)
        ans = []
        for v in nums1:
            if v in d:
                ans.append(d[v])
            else:
                ans.append(-1)
        return ans
        
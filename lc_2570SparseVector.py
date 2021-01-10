class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nonzero = {}
        for idx, v in enumerate(nums):
            self.nonzero[idx] = v
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0 
        for k in self.nonzero:
            if k in vec.nonzero:
                res += self.nonzero[k] * vec.nonzero[k]
                
        return res
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
class SparseVector2:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.v = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0 
        for i in range(len(self.v)):
            res += self.v[i]*vec.v[i]
        
        return res
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dup = set()
        res = set()
        for i,v1 in enumerate(nums):
            if v1  in dup: continue
            dup.add(v1)
            seen = set()
            for j, v2 in enumerate(nums[i+1:]):
                c  = - (v1+ v2)
                if c in seen:
                    res.add(tuple(sorted((v1, v2, c))))
                seen.add(v2)
        return res
    
 
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        
        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            # i, j = idx +1 , len(nums)-1
            j = idx + 1
            i = idx
            seen = set()
            while j < len(nums):
                complement = -(nums[i] + nums[j] )
                if complement in seen :
                    res.append([nums[i], nums[j], complement])
                    while j + 1 < len(nums) and nums[j] == nums[j1]:
                        j +=1
      			
            	seen.add(nums[j])
            	j += 1
            
        return res
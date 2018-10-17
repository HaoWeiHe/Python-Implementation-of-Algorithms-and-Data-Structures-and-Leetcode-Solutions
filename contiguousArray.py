class Solution(object):
    def findMaxLength(self, nums):
        
        tmp, summary,res = [],0,[1,0]
        
        d = dict()
        
        d[0] = -1 #as bundary 
        
        if not nums :
            return 0

        for inx in range(len(nums)):
            elem = nums[inx]
            summary +=-1 if elem == 0 else 1
            currect_elem = summary 
            if currect_elem in d:
                nearlest_same_elem = d[currect_elem]
                
                if res[1] - res[0] < (inx - nearlest_same_elem) :
                    res = [nearlest_same_elem+1, inx]
            else:
                d[currect_elem] = inx
        

    

        return (res[1]-res[0]+1) 
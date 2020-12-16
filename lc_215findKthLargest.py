class Solution(object):
    def findKthLargest(self, nums, k):
        k = len(nums)-k+1
        
        def sort(l,r,lst,k):
            if l < r:
                p = random.randint(l,r)
                lst[p], lst[r] = lst[r], lst[p]
                mid = partition(l,r,r,lst)
                
                """
                [3,2,1,5,6,4] 
                k = 3
                01|2345, r = 1, l = 0, length = r - l +1 = 2
                1 - 0 = 2
                k - (r-l+1) = 3 - 2 = 1
                """
                if k < r - l + 1  :
                    sort(l, mid-1, lst, k)
                if k > r - l + 1 :
                    sort(mid+1,r,lst, k - (r-l+1))
                    
        def partition(lo,hi,p,lst):
            x = lst[p]
            l = lo -1
            for r in range(lo,hi):
                if lst[r] < x:
                    l +=1
                    lst[l], lst[r]  = lst[r], lst[l]
            l +=1 
            lst[l], lst[hi] = lst[hi], lst[l]
            return l
        sort(0,len(nums)-1,nums,k)
        return nums[k]
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[~(k-1)]
        sort(0,len(nums)-1,nums,k)
        
        return nums[k]
        
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[~(k-1)]
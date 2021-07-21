class Solution(object):
    def topKFrequent(self, nums, k):
        """
        [1,1,1,2,2,3], k = 2
        nlogn
        counter()
        pop most common
        
        1:3, 2:2, 3:1, sort and print 
        3,1 -> nlong
        """
        c = Counter(nums)
        return [e[0] for e in c.most_common(k)]
        
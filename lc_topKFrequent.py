import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        print(count)#Counter({1: 3, 2: 2, 3: 1})
        
        h = []
        for val, freq in count.items() :
            heapq.heappush(h,(freq,val))
            if len(h) > k : heapq.heappop(h)
        
        ans =[]
        while h:
            ans.append(heap.heappop(h))
        return ans
            
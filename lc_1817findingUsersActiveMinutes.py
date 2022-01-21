class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        [[0,5],[1,2],[0,2],[0,5],[1,3]]
        {0:{5,2},1:{2,3}}
        ans = [0] *k, 
        [len(key)-1] + 1
        
        """
        d = defaultdict(set)
        for log in logs:#[[0,5],[1,2],[0,2],[0,5],[1,3]]
            user, num = log
            d[user].add(num) #{0:{5,2},1:{2}}
        ans = [0] * k 
        for v in d.values(): 
            if len(v) <= k:
                ans[len(v)-1] += 1 
        return ans
        
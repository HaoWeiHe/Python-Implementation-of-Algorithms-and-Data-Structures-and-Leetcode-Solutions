class Solution(object):
    def countArrangement(self, n):
        """
        [] -> 
            [1]  ([],[1])
            
    2 -> []
           -> [2],[]
        [1]
           ->  [2,1], [1,2]
        
        """
        

        dp = []
        def check(lst):
            for idx, val  in enumerate(lst):
                idx = idx + 1
                if (val > 0 and idx%val == 0) or (idx > 0 and val%idx ==0):
                    continue
                return False
            return True
        #[1,2,3]
        """
        [ 1,2,3] ,[1,3,2]
         ^
         [4,1,2,3],[1,4,2,3] [1,2,3,4], 
        """
        def permutation(n):
            dp = [[[]]]
            # [[1,2,3],[2,3,4]]
            for i in range(1, n+1):
                can = []
                lst = dp[-1]
                for ele in lst:
                    for idx in range(len(ele)+1):
                        can.append(ele[:idx] + [i] + ele[idx:])
                dp.append(can)
            
            return dp

        ans = 0 
        for ele in permutation(n)[-1]:
            if check(ele):
                ans += 1
        return ans

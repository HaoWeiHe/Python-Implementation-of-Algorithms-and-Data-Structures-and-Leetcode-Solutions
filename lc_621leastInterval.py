class Solution(object):
    def leastInterval(self, tasks, n):
        """
        ["A","A","A","B","B","B"]
        1) have idle
        A _ _ A _ _ A 
        A _ _ A _ _ -> n * (Count_max-1) 
        base: (n+1) * (Count_max-1)
        extra: 2 #Count_max ( counter =  3 have 2 elements)
        
        or 
        2) do not have idle
        ["A","A","A","B","B","B","C","C","C","D","D","D"]
        all can fill, so len(tasks)
        
        
        """
        #A = 3,B = 3
        C = collections.Counter(tasks)
        
        ele, max_counter = C.most_common(1)[0]
        extra = 0 
        for e, c in C.items():
            if c == max_counter:
                extra +=1
        return max(len(tasks), (n+1)*(max_counter-1)+ extra )lc

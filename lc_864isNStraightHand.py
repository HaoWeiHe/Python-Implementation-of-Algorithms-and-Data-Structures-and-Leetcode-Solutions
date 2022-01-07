class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
            [1,2,3,6,2,3,4,7,8]
                 V
            {1:1 2:2,3:2 4:1 6:1,7:1, 8:1}
            [1234678]
            
            {1:0 2:1,3:1 4:1 6:1,7:1, 8:1}
            
            [1234678]
              v
             s = [2,3] fist = 2
            
            {1:0 2:0,3:0 4:0 6:1,7:1, 8:1}
            
            [1234678]
                   v   
             s = [], fist = idx move groupsize which is 6
             reapeat until pointer == len(hand)
             
             
             [1,2,3,6,2,3,4,7,8]
             {1:1 2:2 3:2 4:1}
             
        """
        candidate = sorted(list(set(hand))) #[1,2,3,4,6,7,8]
        inverse_dict = { val :idx for idx, val in enumerate(candidate) } #{1:0 2:1 3:2}
        C = Counter(hand)  #{1:1 2:2,3:2 4:1 6:1,7:1, 8:1}
        # inverse_dict = {1,0, 2:1}
        first_idx = 0
        while first_idx < len(candidate):
            s = []
            for inc in range(groupSize):
                cur_val = candidate[first_idx] + inc 
                if cur_val not in C or C[cur_val] == 0:
                    return False
                if C[cur_val] >= 2: 
                    s.append(inverse_dict[cur_val]) #s store index
                C[cur_val] -=1 
            if len(s) > 0 :
                first_idx = s[0] # first_idx = 1
            else:
                first_idx += groupSize #2 + 3 = 5 
        return True if sum(C.values()) == 0 else False
        
       
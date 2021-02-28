class Solution(object):
    def insert(self, its, target):
        """
       [[1,2],[3,5],[6,7],[8,10],[12,16]]
top = [1,2]   [1,5]
1. res = [1,2]    
target = 4,8
2. res = [1,2] [3,8], change = 1
                        oncechange top maters
3. res = [1,2] [3,8] 
                top = [3,8]
    
4. res = [1,2] [3,8] 
                top = [3,8]
                +     8,10
                ========
                       3,10
5. res = [1,2]  [3,10] 
 
        """
        
        
# [[1,2],[3,5],[6,7],[8,10],[12,16]]
# [4,8]

        if not its:return [target]
      
        res =[]
        c = False
        
        for ele in its:
            curi, curj = ele
            
            if not c :
                if curi <= target[0]  <= curj or target[0] <= curi <= target[1] :
                    ele = [min(ele[0], target[0]), max(ele[1], target[1])]
                    c = 1
                res.append(ele)           
            else:
                top = res.pop()
                if curi <= top[1] <= curj or top[0] <= curj <= top[1]:
                    top = [min(top[0], ele[0]), max(top[1], ele[1])]
                    res.append(top)
                else:
                    res.append(top)
                    res.append(ele)
        if not c:
            for idx,ele in enumerate(res):
                if ele[0] > target[1]:
                    return res[:idx] + [target] + res[idx:]
        
            return res + [target] 
        return res        
                
        
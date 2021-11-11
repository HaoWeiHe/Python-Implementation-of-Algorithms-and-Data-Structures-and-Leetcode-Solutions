from collections import defaultdict
class Solution(object):
    def countOfAtoms(self, formula):
        """
        
        "K4 (ON(SO3)2) 2"
            ^
        if not (: start to cound
         K4 +{ON {S:1,O:3}2 } 2 
         
        
        "Mg(OH)2 (O(H)2)2 H2O"
    time =              2
                            {O:1} if not idx ==0, 
                            if char: time * chr
                            {O:1} + {H:1}
                   (O(H)2), 2 
                    O(H)2, 2
                    {H:1}
         if idx == 0:
            return       
  
        
        """
        def add(d1, d2,t = 1):
            ans = defaultdict(int)
            keys = list(set(d1.keys() + d2.keys()))
            for k in keys:
                if k in d1:
                    ans[k] += d1[k] 
                if k in d2:
                    ans[k] += d2[k]
            
            return ans

        def dfs(lst, pre_times):
            if not lst:
                return {}
            times = 0

            counter = 0 
            i = len(lst) -1
            d,tmp_res = {}, {}

            while i >= 0 :
                cur_ele = lst[i]
                if cur_ele == ")":
                    counter += 1
                    j = i - 1

                    while counter > 0 and j >= 0 :
                        if lst[j] == ")":
                            counter += 1
                        if lst[j] == "(":
                            counter -= 1
                        if counter == 0:
                            break
                        j -= 1

                    tmp_res = dfs(lst[j+1:i], max(1,times)*pre_times)
                    d = add(d,tmp_res)
                    i = j -1
                    times = 0
                    continue
                
                elif cur_ele.isdigit():
                    j = i - 1
                    while lst[j].isdigit():
                        j -= 1
                    times = int(lst[j+1:i+1]) 
                    
                    i = j+1
                else:
                    ele = ""
                    if cur_ele.islower():
                        ele = lst[i-1] + cur_ele
                        i -= 1
                    else:
                        ele = cur_ele
                    d = add(d,{ele: max(1,times) * pre_times})
                    times = 0
                i -= 1
            
            return d
        res = dfs(formula, 1)

        ans = ""
        for ele in sorted(res.items(), key = lambda (x,y):x):
            
            ans += ele[0] + str(ele[1]) if ele[1] != 1 else ele[0]
        return ans
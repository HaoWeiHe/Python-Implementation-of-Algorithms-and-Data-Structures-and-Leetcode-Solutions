class Solution(object):
    def findMagicIndex(self, lst):
        self.res = float('inf')
        def find_index(low, high):
            if high < low or low < 0 or high >= len(lst):
                return -1
            
            m  = (low +  high) /2 
            if m == lst[m]:
                self.res = min(m,self.res)

            lf = find_index(low, min(m-1, lst[m]))
            if lf >= 0: return lf
            rt =  find_index(max(m+1, lst[m]), high)
            return rt
        
        find_index(0, len(lst)-1)
        return self.res
        
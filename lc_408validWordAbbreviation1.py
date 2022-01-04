class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
         "i12iz4"
               w
         "internationalization"
                            r
        d = 12 
        if c:
            process +d 
            ++ and check the last == r
            and reset d = 0 
        
    
        return True if r+d == len(word)
        
        "a2e"
           w 
        "apple"
            r   
        
         
        """
        d, w, r, flag = 0, 0, -1, False
        for ele in abbr:
           
            if ele.isdigit():
                if flag and d == 0:
                    return False
                d = d*10 + int(ele)
                flag = True
            else:
                r += d
                if flag and d ==0:
                    return False
                if r + 1 >= len(word) or word[r+1] != ele:
                    return False
                r += 1
                d = 0
                flag = False
        return True if r + d == len(word) -1 else False
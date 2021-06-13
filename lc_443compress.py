class Solution(object):
    def compress(self, chars):
        """
        ["a","a","a","b","b","a","a"]
     r                        v          
     w                    v
          a   3   b   2   a   2
     c    1   2   3   1   2   1    2
         
        
        """
        def write(w, r, c):
            chars[w] = chars[r-1]
            w += 1
            if c == 1:
                return w
            for e in str(c):
                chars[w] = e
                w += 1
            return w
        
        r, w,c  = 0, 0, 1
        for r in range(1, len(chars)):
            if chars[r] == chars[r-1]:
                c += 1
            else:
                w = write(w, r, c)
                c = 1
                
        w = write(w, len(chars), c)
       
        return w 
    
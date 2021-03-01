class Solution(object):
    def compress(self, chars):
        """
       ["a","a","a","b","b","a","a"]
    r                        v
    w    a   3   v
    d = {a:3}        {b = 2}
    idx -1 
        """
        res = ""
        if not chars:return res
        r,w,d = 0,0,{}
        for idx,c in enumerate(chars):
            
            if idx == 0:
                d[c]= 1
                continue
            
            if c not in d :
                chars[w] = chars[idx-1]
                w +=1
                
                if d[chars[idx-1]] > 1:
                    num = str(d[chars[idx-1]])
                    for e in num:
                        chars[w] = e
                        w +=1 
                d = {c:1}
            else:
                d[c] += 1
       
        chars[w] = chars[-1]
        w += 1
        
        if d[chars[-1]] > 1:
            num = str(d[chars[-1]])
            for e in num:
                chars[w] = e
                w +=1 
        return w
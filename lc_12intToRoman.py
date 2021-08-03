class Solution(object):
    def intToRoman(self, num):
        """
         58
         50 L
         8  V
         1- 5
         3  |||
         
        """

        d = {"I":1,
             "V":5,
             "X":10,
             "L":50,
             "C":100,
             "D":500,
             "M": 1000,
             "IV":4,
             "IX":9,
             "XL":40,
             "XC":90,
             "CD":400,
             "CM":900
             }
      # (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        def insert(num, start):
            """
            #58
            50 -> L  (6) #1 to  13
            8 -> V   (6 ) #6 to 13
            28
            div28%10 = 2
            
            """
        def insert(num):
            
            for e in d:
                val, s = e
                if val <= num:
                    return val, s
    
        d = [(e[1],e[0]) for e in  sorted(d.items(), key  = lambda (x,v):v, reverse = True)]
        res = ""
        
        while num:
           
            v,s = insert(num)
            q,r = divmod(num, v)
            res = res + q*s
            num = r
        return res

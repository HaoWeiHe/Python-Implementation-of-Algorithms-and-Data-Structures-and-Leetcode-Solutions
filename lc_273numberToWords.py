class Solution(object):
    def numberToWords(self, num):
      
        """
        1 234 567-thouthand 891
        
        1. split num to chunk (3 nums a chunk)
        2. pass each chunk  to helper
        3. concat the step2
        """
        
        def one(num):
            switcher = {
                    1: 'One',
                    2: 'Two',
                    3: 'Three',
                    4: 'Four',
                    5: 'Five',
                    6: 'Six',
                    7: 'Seven',
                    8: 'Eight',
                    9: 'Nine'
                }
            return switcher.get(num)
       
        def two_less_20(num):
            switcher = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return switcher.get(num)
        
        
        def ten(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
      
            return switcher.get(num)
                 
        res =[]
        lvl = ["","Thousand","Million","Billion"]
        if num ==0:
            return "Zero"
        
        def helper(chunk,level):
           
            if chunk == 0: return ""
            a,b  = divmod(chunk, 100)
            tmp = []
            if a :
                tmp.append(one(a) + " Hundred")

            if b :
                if 0 < b < 10:
                    tmp.append(one(b))
                elif b < 20:
                    tmp.append(two_less_20(b))
                else:
                    a,b = divmod(b,10)
                    tmp.append(ten(a))
                    if b:
                        tmp.append(one(b)) 
            # print(" ".join(tmp))
            return " ".join(tmp) + " "+ lvl[i] if i else " ".join(tmp) 
            
        i, level = 0,0

        
        while 1:
            chunk, rem = divmod(num,1000)
            if rem:
                res.append(helper(rem,level))
            
            num = chunk
            level += 1
            if chunk ==0:
                break
            i +=1
        
        return " ".join(res[::-1])

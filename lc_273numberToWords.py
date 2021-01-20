class Solution(object):
    def numberToWords(self, num):
      
        """
        1 234 567 891
        
        1. split num to chunk 
        2. pass each chunk  to converter
        3. concat the step2
        """
        if num == 0: 
            return "Zero"

        def under20(num):
            lst = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten","Eleven", "Twelve", "Thirteen", "Fourteen","Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            return lst[num-1] 
        def under100(num):
            lst = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            return lst[num]

        chunk_lvl = ["Hundred", "Thousand","Million","Billion"]
        chunks = [100,1000,1000 ** 2, 1000 ** 3]


        def converter(num):
            
            if num == 0:
                return ""
            if num < 20:
                return " "+ under20(num)
            if num < 100:
                return " "+ under100(num / 10 -2) + converter(num % 10) 
            
            for i in range(3,-1,-1):
                if num >= chunks[i]:
                    return converter(num / chunks[i]) + " " + chunk_lvl[i] + converter(num % chunks[i])
            return ""
        return converter(num)[1:]

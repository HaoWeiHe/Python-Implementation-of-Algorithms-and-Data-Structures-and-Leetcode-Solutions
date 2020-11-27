class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        i12iz4n
        il2iz5

        """
        i = 0
        num = 0
        for e in abbr:
            if e == "0" and not num:
                return False

            if e.isdigit():
                num = num*10 + int(e)
            else:
                
                i += num  
                if i > len(word)-1:
                    return False
                    
                if word[i] !=e:
                    return False
                num = 0  
                i +=1 
        
        if abbr[-1].isdigit():
            return i == len(word) - int(abbr[-1])
            
        return i == len(word)
w = "abbreviation"
a  = "a10n"
print(Solution().validWordAbbreviation(w,a))
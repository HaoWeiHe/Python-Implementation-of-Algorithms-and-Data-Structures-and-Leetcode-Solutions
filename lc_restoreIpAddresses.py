class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #2.5525511135
        self.res =[]
        
            
        def dfs(point_number ,record,i):
            
            if i ==len(s) and  point_number ==5: 
                # print(reco)
                self.res.append(record[:-1])
                return 
            if point_number > 4: return 
            
            for idx in range(i,min(len(s),i+4)):
                # print(record+s[i:idx+1], s[i]!="0",s[i],i)
                if s[i] == '0': #1.01.23 reco
                    dfs(point_number+1, record+s[i:idx+1]+".", idx+1)
                    break
                elif 0 < int(s[i:idx+1]) < 256 :
                    dfs(point_number+1, record+s[i:idx+1]+".", idx+1)
        dfs(1,"",0)
        return self.res
s = "101023"
Solution().restoreIpAddresses(s)
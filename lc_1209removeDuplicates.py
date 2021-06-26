class Solution(object):
    def removeDuplicates(self, s, k):
        """
        until no more k continous char exist
            deeedbbcccbdaa#
            1123d
            differnt,
                c< k:
                append previos
                    [d]
                c > k
                append prev *(c /k)
            
            
        """
        if k ==1:
            return ""
        if not s:
            return ""
        
        def dfs(s):
            s = s+"#"
            tmp, pre = [], s[0]
            c, change = 1, False
            
            for i,cur in enumerate(s):
                if i == 0:
                    continue        #"deeeedbbcccbdaa" > [d,d,b,b,b,d,a,a] > dedbbbdaa
                elif s[i] == s[i-1]:
                    c+=1
                else:
                    if c >= k:
                        change = True
                    tmp.append((c % k) * pre)
                    pre = cur
                    c = 1
            if change:
                return dfs("".join(tmp))
            return s[:-1]
        return dfs(s)
            
                

                
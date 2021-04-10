class Solution(object):
    def decodeString2(self, lst):
        """
        3[a2[bc]]
        s = 3[a2[bc
        s = 3[abcbc
        """
        s = []
        for e in lst:
            if e == "]":
                top = e
                lst = []
                while top!= "[":
                    top = s.pop()
                    lst.append(top)
                lst = lst[:-1]
                num = ""
                while s and s[-1].isdigit():
                    top = s.pop()
                    num =  top + num
                    
                tmp = int(num)*lst
                while tmp:
                    s.append(tmp.pop())
                num = 0
            else:
                s.append(e)
        return "".join(s)
                
    def decodeString(self, s):
        """
         
        "a2[c]3[b]"
         a + 2*dfs()+ 3*dfs()
         while i < len(lst):
            e = list[i]
            e.isalpha: concat to ans, i+= 1
            e.num: prepare to check the bundary lst
                    concat num* dfs(bundary lst)
                    update i to bundary lst index +1

        """
        def dfs(lst):
            def helper(i):
                c = 0 
                ans = ""

                while True: #3[a2[c]]
                    e = lst[i]
                    
                    if e == "[":
                        c += 1
                    elif e == "]":
                        c -= 1
                    
                    ans += e
                    i += 1
                    if c == 0:
                        break
                
                return i, ans[1:-1]
                    

            i = 0 
            ans = ""
            flag = 0
            num = 0 
            while i < len(lst):
                
                e = lst[i]
                if e.isalpha():
                    ans += e
                    i += 1
                elif e.isdigit():
                    num = 10*num + int(e)
                    flag = 1
                    i += 1
                elif flag:
                    i, newLst = helper(i)
                    
                    ans += num * dfs(newLst)
                    flag = 0
                    num = 0 

            return ans
        return dfs(s)

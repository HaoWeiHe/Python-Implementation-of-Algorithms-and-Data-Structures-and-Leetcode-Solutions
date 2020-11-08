
class Solution(object):
    def countSubstrings(self, s):
        N = len(s)
        res = 0
        for center in xrange(2*N - 1):
            # aba 3/2 1, 2
            # abba 4/2, 2, 2
            lf = center /2
            rt = lf + center%2
            while lf >=0 and rt < N and s[lf] == s[rt]:
                res +=1 
                lf -=1
                rt +=1
        return res


    def countSubstrings_sol1(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isPalindromic(ele):
            left, right = 0, len(ele)-1
            counter = 0
            while left < right and ele[left] == ele[right]:
                counter += 1
                left += 1
                right -= 1
            return counter == ceil(len(ele)/2)
        record = set()
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i+1,n+1):
                if s[i:j] in record:
                    res +=1
                else:
                    if isPalindromic(s[i:j]):
                        res += 1
                        record.add(s[i:j])        
        return res

s = "aba"
Solution().countSubstrings(s)
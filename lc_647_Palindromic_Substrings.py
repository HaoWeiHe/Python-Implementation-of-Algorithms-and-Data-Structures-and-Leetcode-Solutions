class Solution(object):
    def countSubstrings(self, s):
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
                    res +=1# record[s[i:j]]
                else:
                    if isPalindromic(s[i:j]):
                        res += 1
                        record.add(s[i:j])        
        return res
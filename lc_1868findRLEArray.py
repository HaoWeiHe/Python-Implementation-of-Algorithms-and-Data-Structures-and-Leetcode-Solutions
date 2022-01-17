class Solution(object):
    def findRLEArray(self, encoded1, encoded2):
        """
        encoded1 = [[1,3],[2,1],[3,2]]
                                 ^
        encoded2 = [[2,3],[3,3]]
                           ^
                           
        encoded1 = [[1,3],[2,1],[3,2]]
                                 i
        encoded2 = [[2,3],[3,2]]
                           j
        ans [[2,min(3,3)], [6,1],[9,2]]
            6!= 2, append
            else, add the last
            
        """
        n1,n2 = len(encoded1), len(encoded2)
        i, j = 0, 0 
        ans = []
        while i < n1 and j < n2:
            v1, c1 = encoded1[i]
            v2, c2 = encoded2[j]
            _sum, _c = v1*v2, min(c1,c2)
            if ans and v1*v2 == ans[-1][0]:
                ans[-1][1] += _c
            else:
                ans.append([_sum, _c])
            if _c == c1 and _c == c2:
                i += 1
                j += 1
            else:
                if _c == c1:
                    i += 1
                    encoded2[j][1] -= _c
                else:
                    j += 1
                    encoded1[i][1] -= _c
        return ans
        
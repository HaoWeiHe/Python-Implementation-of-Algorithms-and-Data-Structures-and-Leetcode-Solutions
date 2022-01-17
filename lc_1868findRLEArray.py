

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
            v1, freq1 = encoded1[i]
            v2, freq2 = encoded2[j]
            product, min_freq = v1*v2, min(freq1,freq2)
            encoded1[i][1] -= min_freq
            encoded2[j][1] -= min_freq
            if ans and product == ans[-1][0]:
                ans[-1][1] += min_freq
            else:
                ans.append([product, min_freq])
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
        return ans

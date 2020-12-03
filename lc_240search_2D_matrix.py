class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def bs(start, horizen):
            l, r = start, n -1 if horizen else m -1
            while l <= r:
                mid = (l+r) /2
                if horizen:
                    if matrix[i][mid] == target:
                        return 1
                    if matrix[i][mid] < target:
                        l = mid + 1
                    else:
                        r = mid -1
                else:
                    if matrix[mid][i] == target:
                        return 1
                    if matrix[mid][i] < target:
                        l = mid + 1
                    else: 
                        r = mid-1
             
            return 0

        m,n = len(matrix), len(matrix[0])
        for i in range(min(m,n)):
            if bs(i, 1) or bs(i,0):
                return 1
        return 0


matrix = [[1,4],[2,5]]
target = 2
print(Solution().searchMatrix(matrix, target))
            
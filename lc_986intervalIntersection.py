class Solution(object):
    def intervalIntersection(self, A, B):
        """
        sort A,B
        two pinter i, j (i for A, j for B)
        if i.end == b.end: i++ j ++
        if i.end < b.end: i++
        else: j ++
        
        start, end = max(i.s, j.s), min(i.e, j.e)
        if end >= start:
            res.append([start, end])
        
        """
        A.sort(key = lambda x: (x[0],x[1]))
        B.sort(key = lambda x: (x[0],x[1]))
        i,j = 0, 0 
        res = []
        while i < len(A) and j < len(B):
            start, end = max(A[i][0], B[j][0]), min(A[i][1], B[j][1])
           
            if end >= start:
                res.append([start, end])
            if A[i][1] == B[j][1]:
                i +=1
                j +=1
            elif A[i][1] < B[j][1]:
                i +=1
            else: 
                j +=1
        return res
        
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        deeedbbcccbdaa
   lst         [d,e]
   counter     [1,3]
        d 1
        d,e 1,3
        d 2 #cur == top of lst
        d,b 2,2
        d,b,c 2,2,3
        
        """
        lst, counter = [], []
        for e in s:
            if not lst:
                lst.append(e)
                counter.append(1)
                continue
            if e == lst[-1]:
                counter[-1] += 1
                if counter[-1] == k:
                    counter.pop()
                    lst.pop()
            else:
                lst.append(e)
                counter.append(1)
        return "".join([ e*c for e, c in zip(lst, counter)])
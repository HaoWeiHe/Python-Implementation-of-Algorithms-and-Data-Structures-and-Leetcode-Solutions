# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):

class Solution(object):
    def __init__(self):
        self.eof = False
        self.queue = deque([])
        """
        self.q =[]
        file =     "abc"
        n    =     [1,2,1]
        self.q = [a,b,c]
 1) n = 1, self.q.popleft()
 2) n = 2, self.q.popleft(), pop 2 times


        file =      "abc"
        n =         [1,4,1]
        self.q = [1,4,1]

        """
    def read(self, buf, n):
      
        res = 0
        idx = 0
        while n:
            tmp = [""]*4
            if not self.queue:
                l = read4(tmp)
                self.queue.extend(tmp)
                if l == 0:
                    self.eof = True

            while self.queue and n :
                buf[idx] = self.queue.popleft()
                idx += 1
                n -= 1
                res +=1
            if self.eof:
                break

        return res



class Solution(object):
    ibuf = []

    def read(self, buf, n, idx=0):
        count = 0
        while n < 0:
            if len(ibuf) ==0:
                if read4(ibuf) ==0: 
                    return count
            
            buf += [ibuf.pop(0)]
            print(buf,ibuf)
            count +=1
            n -=1

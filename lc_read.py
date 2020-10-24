
class Solution(object):
    def read(self, buf, n):
        buf4 = ['']*4
        copied_chars = 0
        eof = False

        while not eof and copied_chars < n:
            count = read4(buf4)
            eof = count < 4
            for i in range(count):
                if copied_chars ==n: 
                    break
                buf[copied_chars] = buf4[i]
                copied_chars += 1
        return copied_chars
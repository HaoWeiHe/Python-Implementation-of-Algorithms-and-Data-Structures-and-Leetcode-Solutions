
class Solution(object):
    def __init__(self):
        self.q = []
    def read(self, buf, n):
        i = 0
        while i < n:
            if self.q:
                buf[i] = self.q.pop(0)
                i += 1
            else:
                data = ['']*4
                size = read4(data)
                if not size: 
                    break
                self.q += data[:size]
            
        return i
 
 [a,b,c,d,e,]
abc 1,2,3
keep read into q until the size reach n
# class Solution(object):
#     def __init__(self):
        
#         self.acc = [] #"a","bc",""
#         self.remain =[]
      
#     def read(self, buf, n):
       
#         data = [""]*4
#         eof = False
#         total = []
#         idx = 0
#         while self.remain:
#             if len(total) == n: 
#                 break
#             total.append(self.remain.pop(0))

#         #1. n = 1 < 4 
#         while len(total) < n and not eof :

#             data_length = read4(data)

#             if data_length !=4: 
#                 eof = True

#             for idx, e in enumerate(data):
#                 if idx == n : 

#                     self.remain = [e for e in data[idx:] if e !=""]
#                     break
#                 if e!= "" :
#                     total.append(e)
#         self.acc.append("".join(total))
#         for i, v in enumerate(total):

#             buf[i] = v
        
#         return len(self.acc) + idx
#             